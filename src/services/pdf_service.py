import os
import uuid
import json
from fpdf import FPDF
from langchain_core.messages import HumanMessage, AIMessage
from src.config.settings import settings

def create_chat_report(messages, session_id=None):
    """Chat geçmişinden PDF raporu oluşturur"""
    try:
        if not messages or len(messages) == 0:
            return "PDF oluşturmak için önce biraz analiz yapmalısınız. Geçmiş konuşma bulunamadı."
        
        pdf = FPDF()
        pdf.add_page()
        
        # Font ekle
        font_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), settings.FONT_PATH)
        if os.path.exists(font_path):
            pdf.add_font("DejaVu", "", font_path, uni=True)
            pdf.set_font("DejaVu", size=12)
        else:
            pdf.set_font("Arial", size=12)
        
        # Başlık
        pdf.cell(200, 10, txt="Chatbot Analiz Raporu", ln=True, align='C')
        pdf.ln(10)
        
        # Session ID
        if session_id:
            pdf.cell(200, 10, txt=f"Session ID: {session_id}", ln=True)
            pdf.ln(5)
        
        # Mesajları ekle
        for msg in messages:
            sender = "Kullanıcı" if isinstance(msg, HumanMessage) else "AI"
            content = msg.content
            
            if isinstance(content, dict):
                content = json.dumps(content, ensure_ascii=False, indent=2)
            else:
                content = str(content)
            
            content = content.replace("\n", "\n ")
            text = f"{sender}: {content}"
            pdf.multi_cell(0, 10, text)
            pdf.ln(2)
        
        # Dosyayı kaydet
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), settings.REPORTS_DIR)
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"report_{uuid.uuid4().hex}.pdf"
        file_path = os.path.join(output_dir, filename)
        pdf.output(file_path)
        
        return f"PDF raporunuz hazır: {filename}"
        
    except Exception as e:
        return f"PDF oluşturulamadı: {str(e)}"
