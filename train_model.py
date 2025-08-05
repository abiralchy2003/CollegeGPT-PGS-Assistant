from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pickle

with open("data/pgs_knowledge.txt", "r",encoding="utf-8") as f:
    lines= [line.strip() for line in f.readlines() if line.strip()]
model=SentenceTransformer("all-MiniLM-L6-v2")
embeddings=model.encode(lines)

nn_model=NearestNeighbors(n_neighbors=1,metric= 'cosine')
nn_model.fit(embeddings)

with open("data/vector_store.pkl", "wb") as f:
    pickle.dump((lines, embeddings, nn_model), f)
print("Training complete. Ready for questions.")
