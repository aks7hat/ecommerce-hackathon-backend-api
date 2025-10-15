# app/services/index_loader.py
from app.services.indexer import build_or_load_index

# Load both indexes
text_faiss_index, text_product_metadata = build_or_load_index(index_type="text")
image_faiss_index, image_product_metadata = build_or_load_index(index_type="image")
