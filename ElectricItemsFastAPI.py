from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Data model
class ElectricItem(BaseModel):
    name: str
    brand: str
    warranty: str

# In-memory database
electric_items: List[ElectricItem] = []

# POST - Add a new electric item
@app.post("/items/", response_model=List[ElectricItem])
def add_item(item: ElectricItem):
    electric_items.append(item)
    return electric_items

# GET - List all electric items
@app.get("/items/", response_model=List[ElectricItem])
def list_all_items():
    return electric_items

# GET - Get an item by warranty
@app.get("/items/{warranty}", response_model=ElectricItem)
def get_item_by_warranty(warranty: str):
    for item in electric_items:
        if item.warranty == warranty:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# PUT - Update item by warranty
@app.put("/items/{warranty}", response_model=ElectricItem)
def update_item(warranty: str, name: Optional[str] = None, brand: Optional[str] = None):
    for item in electric_items:
        if item.warranty == warranty:
            if name:
                item.name = name
            if brand:
                item.brand = brand
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE - Remove item by warranty
@app.delete("/items/{warranty}", response_model=ElectricItem)
def delete_item(warranty: str):
    for index, item in enumerate(electric_items):
        if item.warranty == warranty:
            return electric_items.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")
