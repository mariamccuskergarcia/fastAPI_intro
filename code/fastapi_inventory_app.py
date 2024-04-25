"""fastapi_inventory_app.py
"""
import json
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    tag: str
    price: int
    name: str


@app.get("/")
def root():
    return {"inventory": "app"}


@app.get("/items")
def get_items():
    with open(r"..\data\sample_inventory.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/items/{item_tag}")
def get_item_by_tag(item_tag: str):
    with open(r"..\data\sample_inventory.json", "r") as f:
        data = json.load(f)
    for item in data:
        if item["tag"] == item_tag:
            return item
# if the item tag is not found in the database, raise an exception with status code 404 - not found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
    )


@app.post("/items", status_code=status.HTTP_201_CREATED) # here, we set the default status code to 201 - created
def create_item(item: Item):
    with open(r"..\data\sample_inventory.json", "r") as f:
        data = json.load(f)

    if item not in data:
        data.append(item.model_dump())
        with open(r"..\data\sample_inventory.json", "w") as f:
            json.dump(data, f, indent=4)
        return item
    else:
    # if the item is already present in the database, then we raise an exception with status code 409 - conflict
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Item already exists"
        )

@app.put("/items/{item_tag}")
def update_company_by_ticker(item_tag: str, item: Item):

    with open(r"..\data\sample_inventory.json", "r") as f:
        data = json.load(f)

    updated_item = item.model_dump()
    for n, item in enumerate(data):
        if item["tag"] == item_tag:
            data[n] = updated_item
            with open(r"..\data\sample_inventory.json", "w") as f:
                json.dump(data, f, indent=4)
            return updated_item

@app.delete("/items/{item_tag}")
def delete_company_by_ticker(item_tag: str):

    with open(r"..\data\sample_inventory.json", "r") as f:
        data = json.load(f)

    for n, item in enumerate(data):
        if item["tag"] == item_tag:
            deleted_item = data.pop(n)
            with open(r"..\data\sample_inventory.json", "w") as f:
                json.dump(data, f, indent=4)
            return deleted_item