from fastapi import FastAPI
from pydantic import BaseModel
from methods import rank_doc, add_document_text

app = FastAPI()


class Document(BaseModel):
    text: str = ""


@app.post("/search/")
async def search_word(word):
    result = rank_doc(word)
    return result


@app.post("/add_document/")
def add_document(document: Document):
    result = add_document_text(document)
    return result
