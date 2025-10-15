from fastapi import FastAPI
from app.routes import search
# from app.routes import livekit  # Uncomment if using LiveKit routes
from app.services.index_loader import (
    text_faiss_index, text_product_metadata,
    image_faiss_index, image_product_metadata
)
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="Ecommerce Hackathon Chatbot API")


app.state.text_faiss_index = text_faiss_index
app.state.text_product_metadata = text_product_metadata
app.state.image_faiss_index = image_faiss_index
app.state.image_product_metadata = image_product_metadata


app.include_router(search.router, prefix="/search", tags=["search"])
# app.include_router(cart.router, prefix="/cart", tags=["cart"])


@app.get("/")
def root():
    return {"message": "Ecommerce Hackathon Chatbot API is running"}
