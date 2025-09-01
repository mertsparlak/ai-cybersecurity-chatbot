from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from src.config.settings import settings
from src.api import api_router
import os

# FastAPI app oluştur
app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# Static dosyaları serve et
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Template'leri ayarla
templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
if os.path.exists(templates_dir):
    templates = Jinja2Templates(directory=templates_dir)
else:
    templates = None

# API router'ı ekle
app.include_router(api_router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Ana sayfa - web arayüzünü göster"""
    if templates:
        return templates.TemplateResponse("index.html", {"request": request})
    return HTMLResponse("""
    <html>
        <head>
            <title>AI Siber Güvenlik Chatbot</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>AI Siber Güvenlik Chatbot</h1>
            <p>API dokümantasyonu için <a href="/docs">/docs</a> adresini ziyaret edin.</p>
        </body>
    </html>
    """)

@app.get("/health")
async def health_check():
    """Sağlık kontrolü endpoint'i"""
    return {"status": "healthy", "service": "AI Siber Güvenlik Chatbot"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
