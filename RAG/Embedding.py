import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b)))

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 = "What is credit risk?"
sentence2 = "Explain the risk of a borrower failing to repay a loan"

vec1=model.encode(sentence1)
vec2=model.encode(sentence2)

print(f"Similarity of two sentences : {(cosine_similarity(vec1,vec2)):.3f}")
print(f"Embedding dimension : {len(vec1)}")