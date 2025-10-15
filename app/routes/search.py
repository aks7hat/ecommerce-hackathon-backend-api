from fastapi import APIRouter, UploadFile, File, Query
import numpy as np
from app.clients.openai_client import get_text_embeddings, get_image_embedding_from_path
from app.utils.image_utils import save_temp_image
from app.utils.faiss_utils import search
from app.models import SearchResponse
# from app.main import faiss_index, product_metadata
from app.services.index_loader import (
    text_faiss_index, text_product_metadata,
    image_faiss_index, image_product_metadata
)

router = APIRouter()

@router.get("/text", response_model=SearchResponse)
async def search_text(query: str = Query(...)):
    emb = np.array(get_text_embeddings([query]))
    results = search(text_faiss_index, emb, text_product_metadata)
    # print("results text ============ ", results)
    return SearchResponse(results=results)

@router.post("/image", response_model=SearchResponse)
async def search_image(file: UploadFile = File(...)):
    temp_path = save_temp_image(file)
    emb = get_image_embedding_from_path(temp_path)
    product_ids = search(image_faiss_index, np.array([emb]), image_product_metadata)
    return SearchResponse(results=product_ids)
