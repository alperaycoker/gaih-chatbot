import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

load_dotenv()

# Google API Key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY bulunamadı!")

def load_markdown_data(file_path="data/soru_cevap.md"):
    """Markdown dosyasından Q&A verilerini yükle"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"✅ {file_path} dosyası yüklendi ({len(content)} karakter)")
        return content
    except FileNotFoundError:
        print(f"❌ {file_path} bulunamadı!")
        return None
    except Exception as e:
        print(f"❌ Dosya okuma hatası: {e}")
        return None

def create_chunks(text, chunk_size=2000, chunk_overlap=300):
    """Metni chunklara ayır"""
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n## ", "\n\n", "\n", ". ", " ", ""],
            length_function=len
        )
        
        chunks = text_splitter.split_text(text)
        
        # Document objelerine çevir
        documents = [
            Document(
                page_content=chunk,
                metadata={
                    "chunk_id": i,
                    "total_chunks": len(chunks),
                    "source": "gaih_faq"
                }
            )
            for i, chunk in enumerate(chunks)
        ]
        
        print(f"✅ {len(documents)} chunk oluşturuldu")
        return documents
    except Exception as e:
        print(f"❌ Chunking hatası: {e}")
        return None

def create_vector_database(documents, persist_directory="chroma_db"):
    """Chroma vektör veritabanı oluştur"""
    try:
        # Embeddings modeli
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=GOOGLE_API_KEY
        )
        
        print("🔄 Vektör veritabanı oluşturuluyor...")
        
        # Chroma DB oluştur
        vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=persist_directory,
            collection_name="gaih_qa"
        )
        
        print(f"✅ Vektör veritabanı başarıyla oluşturuldu: {persist_directory}")
        print(f"📊 Toplam döküman: {len(documents)}")
        
        return vectorstore
    except Exception as e:
        print(f"❌ Vektör veritabanı oluşturma hatası: {e}")
        return None

def test_retrieval(vectorstore, query="Global AI Hub nedir?", k=3):
    """Vektör veritabanını test et"""
    try:
        print(f"\n🔍 Test sorgusu: '{query}'")
        results = vectorstore.similarity_search(query, k=k)
        
        print(f"✅ {len(results)} sonuç bulundu:\n")
        for i, doc in enumerate(results, 1):
            print(f"--- Sonuç {i} ---")
            print(f"İçerik: {doc.page_content[:200]}...")
            print(f"Metadata: {doc.metadata}\n")
        
        return True
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return False

def main():
    """Ana fonksiyon"""
    print("=" * 60)
    print("🚀 Global AI Hub Chatbot - Vektör Veritabanı Oluşturma")
    print("=" * 60)
    
    # 1. Markdown dosyasını yükle
    print("\n[1/4] Markdown dosyası yükleniyor...")
    text = load_markdown_data("data/soru_cevap.md")
    if not text:
        return
    
    # 2. Chunklara ayır
    print("\n[2/4] Metin chunklara ayrılıyor...")
    documents = create_chunks(text, chunk_size=2000, chunk_overlap=300)
    if not documents:
        return
    
    # 3. Vektör veritabanı oluştur
    print("\n[3/4] Vektör veritabanı oluşturuluyor...")
    vectorstore = create_vector_database(documents, persist_directory="chroma_db")
    if not vectorstore:
        return
    
    # 4. Test et
    print("\n[4/4] Vektör veritabanı test ediliyor...")
    test_retrieval(vectorstore, "Global AI Hub nedir?", k=3)
    
    print("\n" + "=" * 60)
    print("✅ İşlem tamamlandı! Artık app.py'yi çalıştırabilirsiniz.")
    print("=" * 60)

if __name__ == "__main__":
    main()