import os
from app.vector_store.chroma import os
from app.vector_store.chroma import ChromaVectorStore
from app.openai_api import ask_openai

VECTOR_STORE = ChromaVectorStore("knowledge_base")
VECTOR_STORE.load()

def get_rag_answer(question):
    # Retrieve top-k relevant chunks
    docs = VECTOR_STORE.query(question, top_k=3)
    context = "\n\n".join([doc['text'] for doc in docs])
    citations = [doc['source'] for doc in docs]
    prompt = f"""You are an expert assistant. Use the following context to answer the question concisely and truthfully. Cite sources if possible.

Context:
{context}

Question: {question}
Answer:"""
    answer = ask_openai(prompt)
    source = ", ".join(set(citations))
    return answer, source

def add_document(filename, content):
    text = content.decode("utf-8", errors="ignore")
    VECTOR_STORE.add_document(filename, text)
    return "Document added and indexed."
from app.openai_api import ask_openai

VECTOR_STORE = ChromaVectorStore("knowledge_base")
VECTOR_STORE.load()

def get_rag_answer(question):
    # Retrieve top-k relevant chunks
    docs = VECTOR_STORE.query(question, top_k=3)
    context = "\n\n".join([doc['text'] for doc in docs])
    citations = [doc['source'] for doc in docs]
    prompt = f"""You are an expert assistant. Use the following context to answer the question concisely and truthfully. Cite sources if possible.

Context:
{context}

Question: {question}
Answer:"""
    answer = ask_openai(prompt)
    source = ", ".join(set(citations))
    return answer, source

def add_document(filename, content):
    text = content.decode("utf-8", errors="ignore")
    VECTOR_STORE.add_document(filename, text)
    return "Document added and indexed."