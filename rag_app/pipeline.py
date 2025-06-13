from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain.retrievers import EnsembleRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain.retrievers import ContextualCompressionRetriever
from dotenv import load_dotenv
import time
import os

from langchain_cohere import CohereRerank
import pickle
from langchain.embeddings import OpenAIEmbeddings
# Load environment variables
load_dotenv()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")






# Initialize embedding model



# Load FAISS vector DB
db = FAISS.load_local("load_index/Faiss_db", embeddings= embedding_model, allow_dangerous_deserialization=True)
retriever_vector = db.as_retriever(search_kwargs={"k": 4})

# Load BM25 retriever from pickle
with open("load_index/bm25_index.pkl", "rb") as f:
    bm25_retriever = pickle.load(f)

# Combine BM25 and vector retrievers
hybridRetriever = EnsembleRetriever(
    retrievers=[bm25_retriever, retriever_vector],
    weights=[0.3, 0.7]
)

# Add Cohere reranker
reranker = CohereRerank(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    top_n=2,
    model="rerank-english-v3.0"
)
final_retriever = ContextualCompressionRetriever(
    base_compressor=reranker,
    base_retriever=hybridRetriever
)

# Define the prompt template properly
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer the following question using only the context provided.
If the answer is not in the context, say "I don't know."

Question: {query}
Context: {context}
""")

# Initialize LLM (Groq)
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=1024,
    max_retries=2
)

# Define the chain
chain = (
    RunnableParallel({
        "query": RunnablePassthrough(),
        "context": final_retriever
    })
    | prompt
    | llm
    | StrOutputParser()
)

