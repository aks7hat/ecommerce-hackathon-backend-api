# app/services/indexer.py
import pandas as pd
import numpy as np
from app.clients.openai_client import get_text_embeddings, get_image_embedding_from_path
from app.utils.faiss_utils import create_index, save_index, load_index

def build_or_load_index(index_type="image"):
    """
    index_type: 'image' or 'text'
    """
    index, metadata = load_index(index_type=index_type)
    if index is not None:
        print(f"✅ Loaded {index_type} FAISS index from disk.")
        return index, metadata

    print(f"⚙️ Building {index_type} FAISS index from products.xlsx ...")
    df = pd.read_excel("data/products_data.xlsx")
    products = df.to_dict(orient="records")

    if index_type == "text":
        texts = [f"{p['name']} {p['description']}" for p in products]
        embeddings = np.array(get_text_embeddings(texts)).astype("float32")
    else:
        embeddings = []
        for p in products:
            try:
                emb = get_image_embedding_from_path(p['image_url'])
            except Exception as e:
                emb = np.zeros(512, dtype="float32")  # fallback
                # print(f"⚠️ Failed to get embedding for image: {p['image_url']}. Error: {e}")
            embeddings.append(emb)
        embeddings = np.vstack(embeddings).astype("float32")

    index = create_index(embeddings)
    save_index(index, products, index_type=index_type)
    print(f"✅ {index_type} FAISS index created and saved.")
    return index, products
