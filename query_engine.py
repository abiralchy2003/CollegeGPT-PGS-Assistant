from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import pickle
import numpy as np

with open("data/vector_store.pkl", "rb") as f:
    lines, embeddings,nn_model=pickle.load(f)
model=SentenceTransformer("all-MiniLM-L6-v2")
def smart_answer(query, threshold=0.4): 
    query_embedding = model.encode([query])
    dist, idx=nn_model.kneighbors(query_embedding)
    similarity=1 -dist[0][0] 
    if similarity<threshold:
        return f"I’m not sure how to answer that."
    return lines[idx[0][0]]
