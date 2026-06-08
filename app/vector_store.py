import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension=768):
        self.index = faiss.IndexFlatL2(dimension)
        self.text_chunks = []
        self.metadata = []

    def add(self, embeddings, chunks, metadata):
        self.index.add(np.array(embeddings).astype("float32"))
        self.text_chunks.extend(chunks)
        self.metadata.extend(metadata)

    def search(self, query_embedding, top_k=5):
        query = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query, top_k)

        results = []

        for i in indices[0]:
            if i < len(self.text_chunks):
                results.append({
                    "text": self.text_chunks[i],
                    "source": self.metadata[i]
                })

        return results