# 🤖 AI Siber Güvenlik Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)](https://langchain.com/)

Modern web arayüzü ile AI destekli siber güvenlik analiz chatbot'u. IP adresi ve domain güvenlik analizi, tehdit değerlendirmesi ve PDF rapor oluşturma özellikleri sunar.

## ✨ Özellikler

- 🔍 **Gerçek Zamanlı Güvenlik Analizi**: IP adresi ve domain güvenlik kontrolü
- 🤖 **AI Destekli Değerlendirme**: Google Gemini ile tehdit analizi
- 📊 **PDF Rapor Oluşturma**: Sohbet geçmişini PDF formatında dışa aktarma
- 🌐 **Modern Web Arayüzü**: Responsive ve kullanıcı dostu arayüz
- 🔌 **RESTful API**: Programatik erişim için API endpoints
- 💾 **Oturum Yönetimi**: Çoklu kullanıcı desteği
- 🔒 **Güvenlik Kontrolleri**: IP reputation, WHOIS lookup, domain analizi

## 🛠️ Teknoloji Stack'i

- **Backend**: FastAPI, Python 3.8+
- **AI/ML**: LangChain, Google Gemini
- **Web Framework**: FastAPI, Jinja2 Templates
- **Security APIs**: WHOISXML API, IPData API
- **PDF Generation**: FPDF
- **Development**: Uvicorn, Python-dotenv

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.8 veya üzeri
- API Keys (Google Gemini, WHOISXML, IPData)

### Kurulum

1. **Repository'yi klonlayın**
```bash
git clone https://github.com/yourusername/ai-cybersecurity-chatbot.git
cd ai-cybersecurity-chatbot
```

2. **Virtual environment oluşturun**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

4. **Environment dosyasını oluşturun**
```bash
cp env.example .env
```

5. **API key'lerinizi ekleyin**
```env
WHOISXML_API_KEY=your_whoisxml_api_key_here
IPDATA_API_KEY=your_ipdata_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

6. **Uygulamayı çalıştırın**
```bash
python run.py
```

7. **Tarayıcıda açın**
```
http://127.0.0.1:8000
```

## 📖 Kullanım

### Web Arayüzü

1. Tarayıcıda `http://127.0.0.1:8000` adresini açın
2. IP adresi, domain veya mesaj yazın
3. AI destekli güvenlik analizi alın
4. PDF rapor oluşturun

### API Kullanımı

```bash
# Chat endpoint
curl -X POST "http://127.0.0.1:8000/api/chat/" \
  -H "Content-Type: application/json" \
  -d '{"message": "192.168.1.1 güvenli mi?", "session_id": "test-session"}'

# Health check
curl "http://127.0.0.1:8000/health"
```

### API Dokümantasyonu

Swagger UI: `http://127.0.0.1:8000/docs`

## 📁 Proje Yapısı

```
ai-cybersecurity-chatbot/
├── src/
│   ├── api/                 # FastAPI routers
│   │   ├── __init__.py
│   │   └── chat.py
│   ├── config/              # Konfigürasyon
│   │   └── settings.py
│   ├── core/                # Ana iş mantığı
│   │   ├── state.py
│   │   └── workflow.py
│   ├── models/              # Pydantic modelleri
│   │   └── chat.py
│   ├── services/            # Servis katmanı
│   │   ├── ai_service.py
│   │   ├── pdf_service.py
│   │   └── security_service.py
│   └── main.py              # Ana uygulama
├── templates/               # HTML şablonları
│   └── index.html
├── reports/                 # PDF raporları
├── requirements.txt         # Python bağımlılıkları
├── run.py                   # Çalıştırma scripti
├── README.md               # Bu dosya
├── LICENSE                 # MIT lisansı
├── .env.example            # Environment örneği
└── .gitignore              # Git ignore dosyası
```

## 🔧 Konfigürasyon

### Environment Variables

| Değişken | Açıklama | Varsayılan |
|----------|----------|------------|
| `WHOISXML_API_KEY` | WHOISXML API anahtarı | - |
| `IPDATA_API_KEY` | IPData API anahtarı | - |
| `GOOGLE_API_KEY` | Google Gemini API anahtarı | - |
| `HOST` | Sunucu host adresi | `127.0.0.1` |
| `PORT` | Sunucu portu | `8000` |
| `DEBUG` | Debug modu | `False` |

### API Key'leri Alma

1. **Google Gemini**: [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **WHOISXML**: [WHOISXML API](https://user.whoisxmlapi.com/)
3. **IPData**: [IPData](https://ipdata.co/)

## 🧪 Test

```bash
# Health check
curl http://127.0.0.1:8000/health

# API test
curl -X POST "http://127.0.0.1:8000/api/chat/" \
  -H "Content-Type: application/json" \
  -d '{"message": "test", "session_id": "test"}'
```

## 📝 Özellikler Detayı

### Güvenlik Analizi
- **IP Reputation**: IP adresinin güvenlik skoru
- **Domain WHOIS**: Domain kayıt bilgileri
- **Geolocation**: IP adresinin konum bilgisi
- **Threat Intelligence**: Tehdit istihbaratı

### AI Entegrasyonu
- **Google Gemini**: Gelişmiş AI analizi
- **Context Awareness**: Sohbet geçmişi farkındalığı
- **Multi-language**: Türkçe ve İngilizce destek

### Raporlama
- **PDF Export**: Sohbet geçmişini PDF'e aktarma
- **Session Management**: Oturum bazlı raporlama
- **Custom Formatting**: Özelleştirilebilir rapor formatı

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🙏 Teşekkürler

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [LangChain](https://langchain.com/) - AI/LLM framework
- [Google Gemini](https://ai.google.dev/) - AI model
- [WHOISXML API](https://user.whoisxmlapi.com/) - Domain intelligence
- [IPData](https://ipdata.co/) - IP geolocation

## 📞 İletişim

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

