from typing import Optional
import uvicorn
from fastapi import FastAPI
from .services.pokemon_species_search_service import PokemonSpeciesSearchService
from .services.fun_translation_service import FunTranslationService
from .models.pokemon import Pokemon

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pokemon/{pokemon_name}")
def read_item(pokemon_name: str, q: Optional[str] = None):
    data = PokemonSpeciesSearchService(pokemon_name).call()
    pokemon = Pokemon(data)

    return {
        "name": pokemon.get_name(),
        "version": pokemon.get_version(),
        "description": pokemon.get_description(),
        "habitat": pokemon.get_habitat(),
        "is_legendary": pokemon.get_is_legendary(),
    }


@app.get("/pokemon/translated/{pokemon_name}")
def translate_item(pokemon_name: str, q: Optional[str] = None):
    data = PokemonSpeciesSearchService(pokemon_name).call()
    pokemon = Pokemon(data)
    style = pokemon.translation_style()
    text = pokemon.get_description()
    translated_description = FunTranslationService(style, text).call()

    return {
        "name": pokemon.get_name(),
        "version": pokemon.get_version(),
        "description": translated_description,
        "habitat": pokemon.get_habitat(),
        "is_legendary": pokemon.get_is_legendary(),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
