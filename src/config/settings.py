import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API Keys
    WHOISXML_API_KEY = os.getenv("WHOISXML_API_KEY")
    IPDATA_API_KEY = os.getenv("IPDATA_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # FastAPI Settings
    APP_TITLE = "AI Siber Güvenlik Chatbot"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Server Settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    
    # Model Settings
    GEMINI_MODEL = "gemini-1.5-flash"
    GEMINI_TEMPERATURE = 0.7
    
    # File Settings
    REPORTS_DIR = "reports"
    FONT_PATH = "DejaVuSans.ttf"

settings = Settings()

