#!/usr/bin/env python3
"""
AI Siber Güvenlik Chatbot - Ana çalıştırma dosyası
"""

import sys
import os

# Ana dizini Python path'ine ekle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
