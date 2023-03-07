from typing import Union

from fastapi import FastAPI, Query

from googlesearch import search

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search")
def read_item(query: str = Query(...)):
    results = search(query, num_results=10)
    return results