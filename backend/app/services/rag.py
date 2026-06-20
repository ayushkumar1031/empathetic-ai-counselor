import chromadb

from sentence_transformers import SentenceTransformer


class RAGService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="data/chroma_db"
        )

        self.collection = self.client.get_collection(
            name="empathetic_knowledge_base"
        )

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def retrieve(
        self,
        query,
        emotion_label,
        n_results=3
    ):

        search_query = (
            f"{emotion_label} {query}"
        )

        embedding = self.model.encode(
            search_query
        ).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )

        return results["documents"][0]