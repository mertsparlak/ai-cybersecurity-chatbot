import re
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from src.core.state import GraphState
from src.services.security_service import check_ip_reputation, whois_lookup, extract_ip_from_text, extract_domain_from_text
from src.services.ai_service import get_ai_response
from src.services.pdf_service import create_chat_report

checkpointer = MemorySaver()

def detect_intent(state: GraphState):
    """Kullanıcı mesajından niyeti tespit eder"""
    msg = state['messages'][-1].content.lower()
    
    # PDF export kontrolü
    if "pdf" in msg and "analiz" in msg:
        return {"intent": "export_pdf"}
    
    # IP kontrolü
    ip_patterns = [
        r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'
    ]
    for pattern in ip_patterns:
        if re.search(pattern, msg):
            return {"intent": "ip_check"}
    
    # Domain kontrolü
    domain_pattern = r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    if re.search(domain_pattern, msg) and not re.search(r'@', msg):
        return {"intent": "domain_check"}
    
    return {"intent": "ai_chat"}

def handle_ip(state: GraphState):
    """IP adresi işler"""
    msg = state['messages'][-1].content
    ip = extract_ip_from_text(msg)
    
    if ip:
        result = check_ip_reputation(ip)
        return {"messages": [AIMessage(content=result)]}
    else:
        return {"messages": [AIMessage(content="Geçerli bir IP adresi bulunamadı.")]}

def handle_domain(state: GraphState):
    """Domain işler"""
    msg = state['messages'][-1].content
    domain = extract_domain_from_text(msg)
    
    if domain:
        result = whois_lookup(domain)
        return {"messages": [AIMessage(content=result)]}
    else:
        return {"messages": [AIMessage(content="Geçerli bir domain bulunamadı.")]}

def handle_ai_chat(state: GraphState):
    """AI chat işler"""
    system_prompt = "Sen siber güvenlik uzmanı AI asistansın. IP/domain analizi yapabilir ve Türkçe, profesyonel sohbet edebilirsin."
    response = get_ai_response(state['messages'], system_prompt)
    return {"messages": [AIMessage(content=response)]}

def handle_export_pdf(state: GraphState):
    """PDF export işler"""
    result = create_chat_report(state['messages'])
    return {"messages": [AIMessage(content=result)]}

def create_workflow():
    """LangGraph workflow'unu oluşturur"""
    workflow = StateGraph(GraphState)
    
    # Node'ları ekle
    workflow.add_node("detect_intent", detect_intent)
    workflow.add_node("handle_ip", handle_ip)
    workflow.add_node("handle_domain", handle_domain)
    workflow.add_node("handle_ai_chat", handle_ai_chat)
    workflow.add_node("handle_export_pdf", handle_export_pdf)
    
    # Edge'leri ekle
    workflow.add_edge(START, "detect_intent")
    
    def route_intent(state: GraphState):
        intent = state.get("intent", "ai_chat")
        return intent
    
    workflow.add_conditional_edges("detect_intent", route_intent, {
        "ip_check": "handle_ip",
        "domain_check": "handle_domain",
        "ai_chat": "handle_ai_chat",
        "export_pdf": "handle_export_pdf"
    })
    
    workflow.add_edge("handle_ip", END)
    workflow.add_edge("handle_domain", END)
    workflow.add_edge("handle_ai_chat", END)
    workflow.add_edge("handle_export_pdf", END)
    
    return workflow.compile(checkpointer=checkpointer)

# Global workflow instance
graph = create_workflow()
