import uuid
from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage
from src.models.chat import ChatRequest, ChatResponse
from src.core.workflow import graph

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
async def chat(body: ChatRequest):
    """Chat endpoint'i - kullanıcı mesajını işler ve AI yanıtı döner"""
    try:
        session_id = body.session_id or str(uuid.uuid4())
        user_message = HumanMessage(content=body.message)
        
        config = {"configurable": {"thread_id": session_id}}
        current_state = graph.get_state(config)
        
        if current_state and current_state.values.get("messages"):
            past_messages = current_state.values.get("messages", [])
            updated_messages = past_messages + [user_message]
            result = graph.invoke({"messages": updated_messages, "intent": ""}, config=config)
        else:
            result = graph.invoke({"messages": [user_message], "intent": ""}, config=config)
        
        ai_response = result['messages'][-1].content if result['messages'] else "Bir hata oluştu."
        
        return ChatResponse(
            response=ai_response,
            session_id=session_id,
            status="success"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat hatası: {str(e)}")
