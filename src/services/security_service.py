import requests
import re
from src.config.settings import settings
from src.services.ai_service import get_ai_response
from langchain_core.messages import HumanMessage

def check_ip_reputation(ip: str) -> str:
    """IP adresinin güvenlik durumunu kontrol eder"""
    try:
        url = f"https://api.ipdata.co/{ip}?api-key={settings.IPDATA_API_KEY}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            threat_info = data.get('threat', {})
            threat_desc = "Temiz" if not threat_info else f"Tehdit tespit edildi: {threat_info}"
            result = f"""IP Analizi: {ip}
Ülke: {data.get('country_name', 'Bilinmiyor')}
Şehir: {data.get('city', 'Bilinmiyor')}
Güvenlik: {threat_desc}
ISP: {data.get('org', 'Bilinmiyor')}
Zaman Dilimi: {data.get('time_zone', {}).get('name', 'Bilinmiyor')}"""
            
            # AI değerlendirmesi ekle
            ai_context = f"IP analiz sonucu:\n{result}\nKullanıcıya bu IP hakkında kısa bir değerlendirme yap."
            ai_response = get_ai_response([HumanMessage(content=ai_context)])
            return f"{result}\n\nGemini Değerlendirmesi:\n{ai_response}"
            
        return f"IP kontrolü başarısız (HTTP {r.status_code})"
    except Exception as e:
        return f"IP kontrolü hatası: {str(e)}"

def whois_lookup(domain: str) -> str:
    """Domain WHOIS bilgilerini sorgular"""
    try:
        url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={settings.WHOISXML_API_KEY}&domainName={domain}&outputFormat=JSON"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            whois = data.get("WhoisRecord", {})
            registrant = whois.get("registrant", {})
            result = f"""Domain Analizi: {domain}
Oluşturulma: {whois.get('createdDate', 'Bilinmiyor')}
Güncellenme: {whois.get('updatedDate', 'Bilinmiyor')}
Bitiş: {whois.get('expiresDate', 'Bilinmiyor')}
Registrar: {whois.get('registrarName', 'Bilinmiyor')}
Sahibi: {registrant.get('name', 'Gizli/Korumalı')}
Ülke: {registrant.get('country', 'Bilinmiyor')}"""
            
            # AI değerlendirmesi ekle
            ai_context = f"Domain analiz sonucu:\n{result}\nKullanıcıya bu domain hakkında güvenlik açısından kısa bir değerlendirme yap."
            ai_response = get_ai_response([HumanMessage(content=ai_context)])
            return f"{result}\n\nGemini Değerlendirmesi:\n{ai_response}"
            
        return f"WHOIS sorgusu başarısız (HTTP {r.status_code})"
    except Exception as e:
        return f"WHOIS sorgusu hatası: {str(e)}"

def extract_ip_from_text(text: str) -> str:
    """Metinden IP adresi çıkarır"""
    ip_patterns = [
        r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'
    ]
    for pattern in ip_patterns:
        match = re.search(pattern, text)
        if match:
            return match.group()
    return None

def extract_domain_from_text(text: str) -> str:
    """Metinden domain çıkarır"""
    domain_pattern = r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    match = re.search(domain_pattern, text)
    if match and not re.search(r'@', text):
        return match.group()
    return None
