from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from data import questions, answers

app = FastAPI()

# Model loading
model = SentenceTransformer('all-MiniLM-L6-v2')

# Creating word  embeddings
q_embeddings = model.encode(questions).astype('float32')

# Creating  FAISS index
index = faiss.IndexFlatL2(q_embeddings.shape[1])
index.add(q_embeddings)

@app.get("/")
def home():
    return {"message": "FAQ Semantic Search API"}

@app.get("/search")
def search(query: str):
    query_vec = model.encode([query]).astype('float32')
    distances, indices = index.search(query_vec, 1)

    best = indices[0][0]
    
    return {
        "query": query,
        "matched_question": questions[best],
        "answer": answers[best]
    }