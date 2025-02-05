import chromadb
from chromadb.utils import embedding_functions
import os

class ChromaNewsDB:
    def __init__(self, client_path='news_vector_db'):
        self.client = chromadb.PersistentClient(path=client_path)
        self.embedding_func = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=os.getenv('GEMINI_API_KEY'))
        self.main_collection = self.client.get_or_create_collection(name='news_summaries', embedding_function=self.embedding_func)

    