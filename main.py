from fastapi import FastAPI
from methods import rank_doc

app = FastAPI()


@app.post("/search/")
def search_word(word):
    result = rank_doc(word)
    return result
