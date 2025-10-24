# 🤖 Global AI Hub Chatbot

*Yapay Zeka Destekli Soru-Cevap Asistanı* | RAG Tabanlı | Gemini 2.0 Flash

Global AI Hub için geliştirilmiş, Retrieval-Augmented Generation (RAG) mimarisi kullanan, Türkçe ve İngilizce destekli akıllı chatbot uygulaması.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Google-Gemini%202.0-orange.svg)](https://deepmind.google/technologies/gemini/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.7-yellow.svg)](https://www.langchain.com/)

---

## 📋 İçindekiler

- [✨ Özellikler](#-özellikler)
- [🏗️ Mimari](#️-mimari)
- [🚀 Kurulum](#-kurulum)
- [💬 Kullanım](#-kullanım)
- [📁 Proje Yapısı](#-proje-yapısı)
- [🔧 Yapılandırma](#-yapılandırma)
- [🧪 Test](#-test)
- [📸 Ekran Görüntüleri](#-ekran-görüntüleri)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)
- [📄 Lisans](#-lisans)

---

## ✨ Özellikler

### 🎯 Temel Özellikler
- *RAG Mimarisi*: Retrieval-Augmented Generation ile hassas ve kaynak tabanlı yanıtlar
- *Semantik Arama*: Chroma vektör veritabanı ile gelişmiş benzerlik araması
- *Konuşma Hafızası*: Kullanıcı bazlı bağlam koruma
- *Çok Dilli Destek*: Türkçe ve İngilizce sorulara doğal yanıtlar
- *Kaynak Gösterimi*: Her yanıt için ilgili kaynak dökümanlar

### 🎨 Kullanıcı Deneyimi
- *Modern Dark UI*: Gradient efektler ve smooth animasyonlar
- *Responsive Tasarım*: Mobil, tablet ve desktop uyumlu
- *Real-time Göstergeler*: Yükleniyor animasyonları ve durum bildirimleri
- *Örnek Sorular*: Hızlı başlangıç için hazır sorular
- *Markdown Desteği*: Zengin metin formatlaması

### 🔧 Teknik Üstünlükler
- *Google Gemini 2.0 Flash*: Son teknoloji dil modeli
- *text-embedding-004*: Yüksek kaliteli embedding modeli
- *Persistent Storage*: Chroma ile kalıcı vektör depolama
- *Session Management*: Kullanıcı bazlı oturum yönetimi
- *Error Handling*: Kapsamlı hata yönetimi ve kullanıcı geri bildirimi

---

## 🏗️ Mimari

┌─────────────────┐
│   Kullanıcı     │
│     Sorusu      │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│         Flask Backend               │
│  ┌──────────────────────────────┐   │
│  │    1. Query Embedding        │   │
│  │    (text-embedding-004)      │   │
│  └──────────┬───────────────────┘   │
│             │                        │
│             ▼                        │
│  ┌──────────────────────────────┐   │
│  │  2. Semantic Search (k=10)   │   │
│  │     Chroma Vector DB         │   │
│  └──────────┬───────────────────┘   │
│             │                        │
│             ▼                        │
│  ┌──────────────────────────────┐   │
│  │   3. Context Retrieval       │   │
│  └──────────┬───────────────────┘   │
│             │                        │
│             ▼                        │
│  ┌──────────────────────────────┐   │
│  │    4. LLM Generation         │   │
│  │    (Gemini 2.0 Flash)        │   │
│  └──────────┬───────────────────┘   │
│             │                        │
│             ▼                        │
│  ┌──────────────────────────────┐   │
│  │   5. Answer + Sources        │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│  Kullanıcıya    │
│     Yanıt       │
└─────────────────┘


---

## 🚀 Kurulum

### Gereksinimler
- Python 3.10 veya üzeri
- Google API Key (Gemini erişimi)
- pip paket yöneticisi

### 1. Projeyi Klonlayın
bash
git clone https://github.com/arda235121/gaih-chatbot.git
cd gaih-chatbot


### 2. Virtual Environment Oluşturun

*Windows:*
bash
python -m venv venv
venv\Scripts\activate


*Linux/Mac:*
bash
python3 -m venv venv
source venv/bin/activate


### 3. Bağımlılıkları Yükleyin
bash
pip install -r requirements.txt


### 4. API Key Yapılandırması

.env dosyası oluşturun:
env
GOOGLE_API_KEY=your_google_api_key_here


*🔑 Google API Key Nasıl Alınır?*

1. [Google AI Studio](https://aistudio.google.com/) adresine gidin
2. Google hesabınızla giriş yapın
3. "Get API Key" → "Create API Key" tıklayın
4. API key'i kopyalayın ve .env dosyasına yapıştırın

⚠️ *Güvenlik:* .env dosyasını asla Git'e commit etmeyin!

### 5. Vektör Veritabanını Oluşturun
bash
python create_database.py


*Beklenen Çıktı:*

============================================================
🚀 Global AI Hub Chatbot - Vektör Veritabanı Oluşturma
============================================================

[1/4] Markdown dosyası yükleniyor...
✅ data/soru_cevap.md dosyası yüklendi

[2/4] Metin chunklara ayrılıyor...
✅ 12 chunk oluşturuldu

[3/4] Vektör veritabanı oluşturuluyor...
✅ Vektör veritabanı başarıyla oluşturuldu: chroma_db

[4/4] Vektör veritabanı test ediliyor...
✅ 3 sonuç bulundu

============================================================
✅ İşlem tamamlandı! Artık app.py'yi çalıştırabilirsiniz.
============================================================


### 6. Uygulamayı Çalıştırın
bash
python app.py


*Sunucu başladı:*

🚀 Global AI Hub Chatbot başlatılıyor...
✅ Vektör veritabanı başarıyla yüklendi
✅ Chatbot hazır!
 * Running on http://127.0.0.1:5000


### 7. Tarayıcıda Açın

http://localhost:5000


---

## 💬 Kullanım

### Örnek Sorular

*Global AI Hub Hakkında:*

- "Global AI Hub nedir?"
- "Misyonunuz nedir?"
- "Ne zaman kuruldunuz?"


*Eğitim Programları:*

- "Hangi eğitimler var?"
- "Ücretsiz kurslar hangileri?"
- "Bootcamp programları hakkında bilgi ver"
- "Python eğitimi var mı?"


*Başvuru ve Kayıt:*

- "Nasıl başvuru yapabilirim?"
- "Kayıt şartları neler?"
- "Yaş sınırı var mı?"


*Teknik Detaylar:*

- "Hangi teknolojiler öğretiliyor?"
- "GPU erişimi var mı?"
- "Hangi araçlar kullanılıyor?"


*Kariyer Desteği:*

- "İş bulma desteği var mı?"
- "Mezunlar nerede çalışıyor?"
- "Staj imkanları var mı?"


---

## 📁 Proje Yapısı

gaih-chatbot/
│
├── app.py                          # Flask uygulaması ve RAG mantığı
├── create_database.py              # Vektör DB oluşturma scripti
├── requirements.txt                # Python bağımlılıkları
├── .env                            # Environment variables (git'e eklenmez)
├── .env.example                    # Environment variables şablonu
├── .gitignore                      # Git ignore kuralları
├── README.md                       # Proje dokümantasyonu
│
├── data/
│   └── soru_cevap.md              # Bilgi tabanı (Markdown)
│
├── chroma_db/                      # Vektör veritabanı (otomatik oluşur)
│   └── [vektör embeddingler]
│
├── static/
│   ├── style.css                  # Modern dark theme CSS
│   └── images/
│       └── logo.png               # Logo (opsiyonel)
│
└── templates/
    └── index.html                 # Chat arayüzü HTML


---

## 🔧 Yapılandırma

### Model Ayarları (app.py)
python
# LLM Yapılandırması
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",    # Model versiyonu
    temperature=0.57,                 # Yaratıcılık (0-1)
    google_api_key=GOOGLE_API_KEY
)

# Retrieval Yapılandırması
retriever = vectorstore.as_retriever(
    search_type="similarity",         # Arama yöntemi
    search_kwargs={"k": 10}           # Döndürülecek chunk sayısı
)


### Chunking Parametreleri (create_database.py)
python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,                  # Her chunk'taki karakter sayısı
    chunk_overlap=300,                # Chunk'lar arası örtüşme
    separators=["\n\n## ", "\n\n", "\n", ". ", " ", ""]
)


### UI Tema Özelleştirme (static/style.css)
css
:root {
    --primary: #6366f1;           /* Ana renk */
    --primary-dark: #4f46e5;      /* Hover durumu */
    --secondary: #8b5cf6;         /* İkincil vurgu */
    --bg-main: #0f172a;           /* Ana arka plan */
    --bg-secondary: #1e293b;      /* Kart arka planı */
    --text-primary: #f1f5f9;      /* Metin rengi */
}


---

## 🧪 Test

### Manuel Test

1. Uygulamayı başlatın
2. http://localhost:5000 adresine gidin
3. Örnek soruları deneyin
4. Çoklu tur konuşma test edin
5. Hata durumlarını test edin (boş mesaj, uzun metinler)

### Veritabanı Testi
bash
python create_database.py


Bu komut otomatik olarak retrieval'ı test eder.

### Health Check Endpoint

http://localhost:5000/health


*Beklenen Yanıt:*
json
{
  "status": "healthy",
  "vectorstore": true,
  "active_users": 0
}


---

## 🐛 Sorun Giderme

### "GOOGLE_API_KEY bulunamadı!"
*Çözüm:* .env dosyası oluşturun ve geçerli API key ekleyin.

### "Vektör veritabanı yüklenemedi!"
*Çözüm:* Önce python create_database.py komutunu çalıştırın.

### "No module named 'X'"
*Çözüm:* pip install -r requirements.txt komutunu çalıştırın.

### Chatbot yanlış cevaplar veriyor
*Çözüm:* 
1. data/soru_cevap.md dosyasını kontrol edin
2. python create_database.py ile veritabanını yeniden oluşturun
3. k değerini artırın (daha fazla chunk)

### Yavaş yanıtlar
*Çözüm:*
1. k değerini azaltın (daha az chunk)
2. chunk_size değerini küçültün
3. İnternet bağlantınızı kontrol edin

---

## 📊 API Endpoints

### POST /chat
Chatbot'a mesaj gönder

*İstek:*
json
{
  "message": "Global AI Hub nedir?"
}


*Yanıt:*
json
{
  "success": true,
  "answer": "Global AI Hub, yapay zeka alanında...",
  "answer_html": "<p>Global AI Hub...</p>",
  "sources": [
    {
      "id": 1,
      "content": "...",
      "metadata": {...}
    }
  ]
}


### POST /clear
Konuşma geçmişini temizle

*Yanıt:*
json
{
  "success": true,
  "message": "Konuşma geçmişi temizlendi"
}


### GET /health
Sistem sağlık kontrolü

*Yanıt:*
json
{
  "status": "healthy",
  "vectorstore": true,
  "active_users": 5
}


---

## 📸 Ekran Görüntüleri

### Ana Sayfa
![Chatbot Ana Sayfa](screenshots/main.png)

### Konuşma Örneği
![Chatbot Konuşma](screenshots/chat.png)

### Mobil Görünüm
![Mobil Görünüm](screenshots/mobile.png)

---

## 🔒 Güvenlik

### Ortam Değişkenleri
.env dosyasını *asla* Git'e commit etmeyin!

.gitignore dosyasında:

.env
.env.local
.env.production


### Rate Limiting (Üretim İçin)
python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: session.get('user_id'),
    default_limits=["100 per hour"]
)


---

## 🚀 Deployment

### Render.com (Ücretsiz)

1. [Render.com](https://render.com) hesabı oluşturun
2. "New" → "Web Service"
3. GitHub repo'nuzu bağlayın
4. Ayarlar:
   - *Build Command:* pip install -r requirements.txt && python create_database.py
   - *Start Command:* gunicorn app:app
5. Environment Variables:
   - GOOGLE_API_KEY: your-api-key

### Railway

1. [Railway](https://railway.app) hesabı oluşturun
2. "New Project" → "Deploy from GitHub repo"
3. Environment Variables ekleyin
4. Deploy!

---

## 📈 Performans İyileştirme

### Response Caching
Redis ile yaygın sorguları önbelleğe alın:
python
import redis
cache = redis.Redis(host='localhost', port=6379)


### Asynchronous Processing
Async kullanarak performansı artırın:
python
import asyncio
response = await qa_chain.ainvoke({"question": query})


---

## 🎓 Öğrenme Kaynakları

- [Gemini API Docs](https://ai.google.dev/docs)
- [LangChain Guide](https://python.langchain.com/docs)
- [Chroma DB Docs](https://docs.trychroma.com/)
- [Flask Tutorial](https://flask.palletsprojects.com/tutorial/)
- [RAG Paper](https://arxiv.org/abs/2005.11401)

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Feature branch oluşturun (git checkout -b feature/harika-ozellik)
3. Değişikliklerinizi commit edin (git commit -m 'Harika özellik eklendi')
4. Branch'inizi push edin (git push origin feature/harika-ozellik)
5. Pull Request açın

---

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 👨‍💻 Geliştirici

*Arda Zerenay*
- GitHub: [@arda235121](https://github.com/arda235121)
- Email: ardazerenay@gmail.com
- LinkedIn: [Profilim](https://linkedin.com/in/arda-zerenay-957993346/)


*Alp Eray Çoker*
- GitHub: [@alperaycoker](https://github.com/alperaycoker)
- Email: alperaycoker@gmail.com
- LinkedIn: [Profilim](https://linkedin.com/in/alperaycoker)

---

## 🙏 Teşekkürler

- *Global AI Hub* - Proje fırsatı için
- *Google* - Gemini API için
- *LangChain* - RAG framework için
- *Chroma* - Vektör veritabanı için
- *Flask* - Web framework için

---

## 🎯 Gelecek Geliştirmeler

- [ ] Tam İngilizce dil desteği
- [ ] Sesli giriş/çıkış
- [ ] Analytics dashboard
- [ ] Kullanıcı kimlik doğrulama
- [ ] Konuşma export (PDF/JSON)
- [ ] Slack/Discord entegrasyonu
- [ ] A/B testing framework
- [ ] Otomatik test suite
- [ ] Docker containerization
- [ ] CI/CD pipeline

---


