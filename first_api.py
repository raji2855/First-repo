# pyrefly: ignore [missing-import]
import fastapi
# pyrefly: ignore [missing-import]
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{id}")
async def read_user(id: int):
    return {"user_id": id}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    return {"item_id": item_id, "q": q}
    # uv run first_api.py  - it will run the api        