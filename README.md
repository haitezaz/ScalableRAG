![image](https://github.com/user-attachments/assets/30de7c73-8489-4582-913c-ba9f1044bd05)

markdown
Copy
Edit
# 🚀 ScalableRAG – Production-Ready Advanced RAG Pipeline

**ScalableRAG** is a high-performance, production-grade Retrieval-Augmented Generation (RAG) application that combines multiple retrieval and optimization strategies for accurate, low-latency responses. Designed for real-world use cases, it integrates hybrid search, reranking, parallel processing, and more—fully deployed and ready to scale.

> ⚡ Live on Railway  
> 📚 Built using best practices from *The Lean Startup*  
> 🧠 Capable of handling 10,000+ documents with blazing-fast response times

---

## 🧩 Features

- 🔍 **Hybrid Retrieval**: Combines FAISS vector search with local BM25 keyword-based search
- 🧠 **Cohere Reranking**: Boosts relevance by reranking retrieved chunks using Cohere’s `rerank` API
- 📦 **Efficient Storage**: Pre-built FAISS and BM25 indexes stored locally for instant startup
- 🔗 **Parallel Chaining**: LangChain’s Runnable architecture enables fast, multi-retriever execution
- ⚡ **Optimized Latency**: Reduced generation time from ~23s to ~2–4s with parallelism and indexing
- 🌐 **FastAPI Backend**: Clean and extensible REST API for deployment
- 🖼️ **HTML Frontend**: Lightweight, user-friendly interface for query interaction
- 🔐 **Environment Variables**: Securely handles API keys using `.env` and `python-dotenv`
- 🌍 **Railway Deployment**: End-to-end live deployment in a serverless environment
- 📚 **Inspired by Lean Startup**: MVP-first approach to iterative development

---

## 📁 Project Structure

ScalableRAG/
├── rag_app/
│ ├── main.py # FastAPI app with routes
│ ├── pipeline.py # Core RAG logic: retrievers, reranker, chain
│ ├── templates/ # Jinja2 HTML templates
│ │ └── index.html
│ └── static/ # (Optional) static assets
├── load_indeces/ # Pre-computed FAISS and BM25 indexes
├── make.ipynb # (Optional) Used to generate vector stores
├── requirements.txt # All dependencies
└── .env # API keys (not pushed to GitHub)

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/haitezaz/ScalableRAG.git
cd ScalableRAG
2. Create & Activate a Virtual Environment
bash
Copy
Edit
python -m venv rag-env
source rag-env/bin/activate  # On Windows: rag-env\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root directory:

ini
Copy
Edit
OPENAI_API_KEY=your-openai-key
COHERE_API_KEY=your-cohere-key
5. Run the App
bash
Copy
Edit
uvicorn rag_app.main:app --reload
Then open http://localhost:8000 in your browser.

⚙️ How It Works
User Query is received from the HTML frontend.

BM25 & FAISS Retrievers run in parallel to gather relevant chunks.

Cohere API Reranker reorders results by relevance.

OpenAI Embeddings + LLM power the response generation.

Answer is displayed in real time via the web interface.

🛠️ Stack Overview
Component	Tool/Service
Backend	FastAPI
Frontend	Jinja2 HTML
Vector Search	FAISS (locally stored)
Keyword Search	BM25 (locally stored)
Embeddings	OpenAI Embedding Models
Generation	OpenAI GPT Models
Reranking	Cohere Rerank API
Framework	LangChain (core + community)
Deployment	Railway

