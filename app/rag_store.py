import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.docs import DOCS

# DOCS is already a list of {id, content}
DOCUMENTS = DOCS

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Prepare corpus
texts = [doc["content"] for doc in DOCUMENTS]

# Create embeddings
embeddings = embedding_model.encode(
    texts,
    convert_to_numpy=True
).astype("float32")

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def embed(query: str, top_k: int = 2):
    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    _, indices = index.search(query_embedding, top_k)

    return [DOCUMENTS[i] for i in indices[0]]