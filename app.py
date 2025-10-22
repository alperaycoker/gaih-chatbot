import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import markdown
import uuid

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Google API Yapılandırması
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY bulunamadı! .env dosyasını kontrol edin.")

genai.configure(api_key=GOOGLE_API_KEY)

# Global değişkenler
vectorstore = None
user_chains = {}

def load_vector_database():
    """Önceden oluşturulmuş Chroma veritabanını yükle"""
    global vectorstore
    
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=GOOGLE_API_KEY
        )
        
        vectorstore = Chroma(
            persist_directory="chroma_db",
            embedding_function=embeddings,
            collection_name="gaih_qa"
        )
        
        print("✅ Vektör veritabanı başarıyla yüklendi")
        return True
    except Exception as e:
        print(f"❌ Vektör veritabanı yükleme hatası: {e}")
        return False

def create_qa_chain_for_user():
    """Her kullanıcı için RAG tabanlı soru-cevap zinciri oluştur"""
    global vectorstore
    
    if vectorstore is None:
        raise Exception("Vektör veritabanı yüklenmemiş!")
    
    try:
        # LLM yapılandırması
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            temperature=0.57,
            google_api_key=GOOGLE_API_KEY,
            convert_system_message_to_human=True
        )
        
        # Memory yapılandırması
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
        # RAG chain
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 10}
            ),
            memory=memory,
            return_source_documents=True,
            verbose=False
        )
        
        print("✅ Kullanıcı için QA Chain oluşturuldu")
        return qa_chain
    except Exception as e:
        print(f"❌ QA Chain oluşturma hatası: {e}")
        return None

@app.route('/')
def index():
    """Ana sayfa"""
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Chatbot endpoint - Kullanıcı mesajını işle"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        user_id = session.get('user_id', str(uuid.uuid4()))
        
        if not user_message:
            return jsonify({
                'error': 'Lütfen bir mesaj yazın'
            }), 400
        
        # Kullanıcı için chain yoksa oluştur
        if user_id not in user_chains:
            user_chains[user_id] = create_qa_chain_for_user()
            if user_chains[user_id] is None:
                return jsonify({'error': 'Asistan hazırlanamadı'}), 500
        
        qa_chain = user_chains[user_id]
        
        # RAG ile cevap üret
        response = qa_chain({"question": user_message})
        
        bot_answer = response['answer']
        source_docs = response.get('source_documents', [])
        
        # Markdown'ı HTML'e çevir
        bot_answer_html = markdown.markdown(
            bot_answer,
            extensions=['extra', 'codehilite', 'nl2br']
        )
        
        # Kaynak bilgisi ekle
        source_info = []
        for i, doc in enumerate(source_docs[:3], 1):
            source_info.append({
                'id': i,
                'content': doc.page_content[:200] + "...",
                'metadata': doc.metadata
            })
        
        return jsonify({
            'success': True,
            'answer': bot_answer,
            'answer_html': bot_answer_html,
            'sources': source_info,
            'user_id': user_id
        })
        
    except Exception as e:
        print(f"❌ Chat hatası: {e}")
        return jsonify({
            'error': f'Bir hata oluştu: {str(e)}'
        }), 500

@app.route('/clear', methods=['POST'])
def clear_history():
    """Konuşma geçmişini temizle"""
    try:
        user_id = session.get('user_id')
        if user_id and user_id in user_chains:
            del user_chains[user_id]
        
        return jsonify({
            'success': True,
            'message': 'Konuşma geçmişi temizlendi'
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/health')
def health_check():
    """Sağlık kontrolü endpoint"""
    return jsonify({
        'status': 'healthy',
        'vectorstore': vectorstore is not None,
        'active_users': len(user_chains)
    })

# Uygulama başlangıcında vektör veritabanını yükle
with app.app_context():
    print("🚀 Global AI Hub Chatbot başlatılıyor...")
    if load_vector_database():
        print("✅ Chatbot hazır!")
    else:
        print("⚠️ Vektör veritabanı yüklenemedi!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)