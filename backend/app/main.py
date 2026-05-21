from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Online Ordering System API")

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/hello/{name}")
def say_hello(name:str) -> dict [str, str]:
    return {"message": f"Hello, {name}!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}




   