from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from src.config.settings import settings

def get_gemini_model():
    """Gemini AI model'ini döndürür"""
    if settings.GOOGLE_API_KEY:
        return ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=settings.GEMINI_TEMPERATURE
        )
    return None

def get_ai_response(messages, system_prompt=None):
    """AI'dan yanıt alır"""
    gemini_model = get_gemini_model()
    if not gemini_model:
        return "Gemini servisi mevcut değil."
    
    try:
        if system_prompt:
            all_messages = [SystemMessage(content=system_prompt)] + messages
        else:
            all_messages = messages
            
        response = gemini_model.invoke(all_messages)
        return response.content
    except Exception as e:
        return f"Gemini yanıtı alınamadı: {str(e)}"
