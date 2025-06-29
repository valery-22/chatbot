import os
import chromadb
from chromadb.utils import embedding_functions

class ChromaVectorStore:
    def __init__(self, collection_name):
        # Initialize a persistent ChromaDB client
        self.client = chromadb.PersistentClient(path="chroma_db")
        # Set up embedding function (OpenAI)
        self.collection = self.client.get_or_create_collection(
            collection_name,
            embedding_function=embedding_functions.OpenAIEmbeddingFunction(
                api_key=os.getenv("OPENAI_API_KEY"),
                model_name="text-embedding-ada-002"
            )
        )

    def load(self):
        # For persistent client, collection is loaded on init
        pass

    def add_document(self, source, text, chunk_size=512, overlap=64):
        # Chunk the document text for semantic search
        chunks = []
        for i in range(0, len(text), chunk_size - overlap):
            chunk = text[i:i+chunk_size]
            if chunk.strip():
                chunks.append(chunk)
        # Add each chunk as a separate document with metadata
        for i, chunk in enumerate(chunks):
            self.collection.add(
                documents=[chunk],
                metadatas=[{"source": source}],
                ids=[f"{source}-{i}"]
            )

    def query(self, query_text, top_k=3):
        # Retrieve top_k most relevant document chunks
        results = self.collection.query(
            query_texts=[query_text], n_results=top_k
        )
        docs = []
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            docs.append({"text": doc, "source": meta["source"]})
        return docs