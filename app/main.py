from typing import Optional
import uvicorn
from fastapi import FastAPI
import requests
from .lib.pokemon_api_client import PokemonApiClient

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


ENDPOINT_URL = "/pokemon-species/"


@app.get("/pokemon/{pokemon_name}")
def read_item(pokemon_name: str, q: Optional[str] = None):
    res = PokemonApiClient(ENDPOINT_URL, "mewtwo").call()
    pokemon = {}
    pokemon["name"] = res["name"]
    pokemon["description"] = "placeholder"
    pokemon["habitat"] = res["habitat"]["name"]
    pokemon["is_legendary"] = res["is_legendary"]
    return {"pokemon_name": pokemon_name, "q": q, "payload": pokemon}


@app.get("/pokemon/translated/{pokemon_name}")
def translate_item(pokemon_name: str, q: Optional[str] = None):
    res = PokemonApiClient(ENDPOINT_URL, "mewtwo").call()
    pokemon = {}
    pokemon["name"] = res["name"]
    pokemon["description"] = "translation placeholder"
    pokemon["habitat"] = res["habitat"]["name"]
    pokemon["is_legendary"] = res["is_legendary"]
    return {"pokemon_name": pokemon_name, "q": q, "payload": pokemon}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
