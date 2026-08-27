import numpy as np

def cosine_sim(a,b):
    return np.dot(a,b)

docs={
    "credit risk ": np.array([0.9 , 0.1 , 0.2 , 0.3]) ,
    " market risk ": np.array([0.2 , 0.9 , 0.1 , 0.4]) ,
    " liquidity risk ": np.array([0.3 , 0.2 , 0.9 , 0.1]) ,
}

query_vec = np.array([0.85 , 0.15 , 0.25 , 0.30])

for name,vec in docs.items():
    print(f"(name) : {(cosine_sim(vec,query_vec)):.3f}")