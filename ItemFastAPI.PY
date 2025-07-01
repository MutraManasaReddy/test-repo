from fastapi import FastAPI

app= FastAPI()

items = []
@app.post("/item")
def add_item(item:str):
    items.append(item)
    return items
@app.get("/item")
def list_all_items():
    return items
@app.patch("/update-items/{name}")
def update_item(name:str, color : str = None, kg : int = None):
    items = update_item(name)
    if items is None:
        return None
    if name is not None:
        items.name = name
    if color is not None:
        items.color = color
    if kg is not None:
        items.kg = color
@app.delete("/item")
def remove_item(item:str):
    items.remove(item)
    return items   


