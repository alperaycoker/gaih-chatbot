# 🤖 Global AI Hub - RAG Chatbot

Bu proje, **Google Generative AI (Gemini)**, **LangChain** ve **ChromaDB** kullanılarak geliştirilmiş bir **RAG (Retrieval-Augmented Generation)** sohbet botudur.  
Bot, `data/soru_cevap.md` dosyasındaki bilgilere dayanarak soruları yanıtlamak üzere tasarlanmıştır.

---

## 🧠 Proje Hakkında

Proje üç ana bileşenden oluşmaktadır:

1. **`create_database.py`**  
   → Markdown dosyasını (bilgi kaynağını) işler, metni parçalara böler ve **ChromaDB** üzerinde bir **vektör veritabanı** oluşturur.

2. **`app.py`**  
   → Flask tabanlı bir web uygulaması sunar ve oluşturulan vektör veritabanını kullanarak RAG mimarisi ile akıllı yanıtlar üretir.

3. **`templates` / `static` klasörleri**  
   → Kullanıcı dostu bir web arayüzü sağlar (HTML, CSS, JS dosyaları).

---

## 🚀 Özellikler

- Markdown dosyasından **Soru-Cevap verilerini** okuma  
- Google'ın `models/text-embedding-004` modelini kullanarak **embedding** oluşturma  
- Verileri **ChromaDB**’de kalıcı şekilde saklama  
- Flask tabanlı **web arayüzü**  
- `gemini-2.0-flash-exp` modelini kullanarak **RAG tabanlı yanıt üretimi**  
- LangChain’in **ConversationalRetrievalChain** yapısı ile konuşma hafızası yönetimi  
- Her kullanıcı için ayrı **sohbet oturumu ve hafıza**  
- Yanıtlarda **kaynak belgeleri gösterme**

---

## 📁 Proje Yapısı

```bash
.
├── .git/                  # Git versiyon kontrolü
├── chroma_db/             # (create_database.py çalışınca oluşur) Vektör veritabanı
├── data/                  # Markdown (soru_cevap.md) dosyalarının konumu
├── static/                # Flask için statik dosyalar (CSS, JS, resimler)
├── templates/             # Flask için HTML şablonları (index.html)
├── venv/                  # Python sanal ortamı
├── .env                   # (Oluşturulmalı) API anahtarları ve ayarlar
├── .env.example           # Örnek .env dosyası
├── .gitignore             # Git tarafından görmezden gelinecek dosyalar
├── app.py                 # Flask web sunucusu ve chatbot mantığı
├── create_database.py     # Vektör veritabanını oluşturan betik
├── README.md              # Bu dosya
└── requirements.txt       # Gerekli Python kütüphaneleri
```
⚙️ Kurulum Adımları
1️⃣ Projeyi Klonlayın
git clone <proje-linkiniz>
cd <proje-dizini>

2️⃣ Sanal Ortam Oluşturun (Önerilir)
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Gerekli Kütüphaneleri Kurun
pip install -r requirements.txt

4️⃣ Ortam Değişkenlerini Ayarlayın
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env


Daha sonra .env dosyasını açıp kendi Google API anahtarınızı girin:

GOOGLE_API_KEY="AIzaSy...YOUR_API_KEY"

5️⃣ Veri Dosyasını Hazırlayın

data/ klasörünün içinde, botun bilgi kaynağı olacak soru_cevap.md dosyasını ekleyin.

🧩 Kullanım
Adım 1: Vektör Veritabanını Oluşturma

Aşağıdaki komut, data/soru_cevap.md dosyasını okuyarak ChromaDB veritabanını oluşturur:

python create_database.py


Bu işlem yalnızca ilk seferde veya veri dosyanızı güncellediğinizde yapılmalıdır.
İşlem tamamlandığında chroma_db/ klasörü oluşacaktır.

Adım 2: Web Uygulamasını Başlatma
python app.py


Tarayıcıdan aşağıdaki adrese giderek sohbet arayüzünü kullanabilirsiniz:

👉 http://localhost:5000

🌐 API Endpoints
Endpoint	Yöntem	Açıklama
/	GET	Ana sohbet arayüzünü (index.html) yükler
/chat	POST	Kullanıcı mesajını alır, bot cevabını JSON döner
/clear	POST	Kullanıcının sohbet geçmişini temizler
/health	GET	Sunucu ve veritabanı durumunu kontrol eder
🧮 Teknik Detaylar
🔹 Veri İşleme (create_database.py)

Embedding Modeli: models/text-embedding-004 (GoogleGenerativeAIEmbeddings)

Parçalama (Chunking): RecursiveCharacterTextSplitter

Chunk boyutu: 2000

Overlap: 300

Veritabanı: Chroma

Koleksiyon adı: gaih_qa

Kalıcı dizin: chroma_db

🔹 Sohbet ve RAG (app.py)

LLM Modeli: gemini-2.0-flash-exp (ChatGoogleGenerativeAI)

Zincir: ConversationalRetrievalChain (LangChain)

Hafıza: ConversationBufferMemory

Her kullanıcı için ayrı olarak user_chains sözlüğünde tutulur

Retriever:

Chroma veritabanı üzerinden çalışır

k=10 (en benzer 10 sonucu alır)

📜 Lisans

Bu proje, Akbank GenAI Bootcamp kapsamında geliştirilmiştir.
Kullanım koşulları için eğitimin yönergelerini dikkate alınız.

👨‍💻 Geliştirici Notu

Bu proje, LangChain ve Gemini API ile RAG mimarisini birleştirerek, doküman tabanlı bilgi sorgulama sistemlerinin nasıl geliştirileceğini göstermeyi amaçlamaktadır.
Geliştirici deneyimini kolaylaştırmak için Flask tabanlı sade bir web arayüzü eklenmiştir.
