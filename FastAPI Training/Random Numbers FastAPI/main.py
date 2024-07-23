from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"E": "E", "Hi": 200}

@app.get("/random")
async def get_randon():
    random_number = random.randrange(0, 100)
    return {"number": random_number}

@app.get("/random/{limit}")
async def get_randon(limit: int):
    random_number = random.randrange(0, limit)
    return {"number": random_number, "limit": limit}