from fastapi import FastAPI

app = FastAPI()

products = [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Phone"}]

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def add_product(product: dict):
    products.append(product)
    return {"message": "Product added!"}

