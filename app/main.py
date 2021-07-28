from typing import Optional

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pokemon/{pokemon_name}")
def read_item(pokemon_name: str, q: Optional[str] = None):
    response = requests.get("https://pokeapi.co/api/v2/pokemon-species/mewtwo")
    res = response.json()
    pokemon = {}
    pokemon["name"] = res["name"]
    pokemon["description"] = "placeholder"
    pokemon["habitat"] = res["habitat"]["name"]
    pokemon["is_legendary"] = res["is_legendary"]
    return {"pokemon_name": pokemon_name, "q": q, "payload": pokemon}


@app.get("/pokemon/translated/{pokemon_name}")
def translate_item(pokemon_name: str, q: Optional[str] = None):
    response = requests.get("https://pokeapi.co/api/v2/pokemon-species/mewtwo")
    res = response.json()
    pokemon = {}
    pokemon["name"] = res["name"]
    pokemon["description"] = "translation placeholder"
    pokemon["habitat"] = res["habitat"]["name"]
    pokemon["is_legendary"] = res["is_legendary"]
    return {"pokemon_name": pokemon_name, "q": q, "payload": pokemon}
