from fastapi import FastAPI

app = FastAPI(title="Online Ordering System API")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/hello/{name}")
def say_hello(name:str) -> dict [str, str]:
    return {"message": f"Hello, {name}!"}