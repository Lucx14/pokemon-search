from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pokemon/{pokemon_name}")
def read_item(pokemon_name: str, q: Optional[str] = None):
    return {"pokemon_name": pokemon_name, "q": q}


@app.get("/pokemon/translated/{pokemon_name}")
def translate_item(pokemon_name: str, q: Optional[str] = None):
    return {"pokemon_name": pokemon_name, "q": q}
