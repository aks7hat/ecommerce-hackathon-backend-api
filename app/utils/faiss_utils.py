import faiss
import os
import pickle
import numpy as np

def get_index_paths(index_type="image"):
    return f"data/faiss_{index_type}.bin", f"data/faiss_{index_type}_metadata.pkl"

def create_index(embeddings: np.ndarray):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def save_index(index, metadata, index_type="image"):
    index_path, meta_path = get_index_paths(index_type)
    os.makedirs("data", exist_ok=True)
    faiss.write_index(index, index_path)
    with open(meta_path, "wb") as f:
        pickle.dump(metadata, f)

def load_index(index_type="image"):
    index_path, meta_path = get_index_paths(index_type)
    if os.path.exists(index_path) and os.path.exists(meta_path):
        index = faiss.read_index(index_path)
        with open(meta_path, "rb") as f:
            metadata = pickle.load(f)
        return index, metadata
    return None, None

def search(index, query_vector: np.ndarray, metadata: list, top_k: int = 3):
    D, I = index.search(query_vector.astype("float32"), top_k)
    return [str(metadata[i]["product_id"]) for i in I[0] if i < len(metadata)]
