# from typing import Dict, List
# from app.models import CartItem

# # Simple in-memory cart store
# carts: Dict[str, List[CartItem]] = {}

# def add_to_cart(user_id: str, product_id: str):
#     if user_id not in carts:
#         carts[user_id] = []
#     carts[user_id].append(CartItem(product_id=product_id))
#     return {"message": f"Added product {product_id} to cart."}

# def view_cart(user_id: str):
#     return {"user_id": user_id, "cart": [item.dict() for item in carts.get(user_id, [])]}

# def clear_cart(user_id: str):
#     carts[user_id] = []
#     return {"message": "Cart cleared."}
