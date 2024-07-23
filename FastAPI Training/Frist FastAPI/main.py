from fastapi import FastAPI, HTTPException, Path, Query
from enum import Enum

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}
