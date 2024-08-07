from fastapi import FastAPI
from methods import rank_doc
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/search/")
def search_word(word):
    result = rank_doc(word)
    return result
