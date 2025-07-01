from fastapi import FastAPI

app = FastAPI()

Product =[]
@app.post("/product")
def add_product(product:str):
    Product.append(product)
    return Product
@app.get("/product")
def list_all_product():
    return Product
@app.delete("/product")
def remove_item(product:str):
    Product.remove(product)
    return Product