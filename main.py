from fastapi import FastAPI
from models.product import Product
from controller.products import get_products,create_product,edit_product,delete_product
app = FastAPI()

products = []

@app.get("/products")
def get_products_api():
    return get_products()

@app.post("/products")
def create_product_api(product: Product):
    return create_product(product)

@app.put("/products/{product_id}")
def edit_product_api(product_id:int,product: Product):
    return edit_product(product_id,product)

@app.delete("/products/{product_id}")
def delete_product_api(product_id:int):
    return delete_product(product_id)