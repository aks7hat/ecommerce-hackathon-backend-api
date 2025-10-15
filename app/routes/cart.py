# from fastapi import APIRouter, Form
# from app.services.cart_service import add_to_cart, view_cart, clear_cart

# router = APIRouter()

# @router.post("/add")
# async def add_cart(user_id: str = Form(...), product_id: str = Form(...)):
#     return add_to_cart(user_id, product_id)

# @router.get("/view")
# async def view_user_cart(user_id: str):
#     return view_cart(user_id)

# # @router.post("/checkout")
# # async def checkout(user_id: str = Form(...)):
# #     cart = view_cart(user_id)
# #     if not cart["cart"]:
# #         return {"message": "Your cart is empty."}
# #     clear_cart(user_id)
# #     return {"message": "✅ Order placed successfully (demo checkout)."}
