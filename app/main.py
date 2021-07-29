from typing import Optional
from fastapi import FastAPI, Request
from .services.pokemon_species_search_service import PokemonSpeciesSearchService
from .services.fun_translation_service import FunTranslationService
from .models.pokemon import Pokemon
from .utils.app_exceptions import (
    PokemonApiException,
    InvalidNameException,
    TranslatorApiException,
)
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(PokemonApiException)
async def pokemon_api_exception_handler(request: Request, exc: PokemonApiException):
    return JSONResponse(
        status_code=503,
        content={"message": "Service currently unavailable"},
    )


@app.exception_handler(InvalidNameException)
async def invalid_pokemon_name_exception_handler(
    request: Request, exc: InvalidNameException
):
    return JSONResponse(
        status_code=404,
        content={"message": f"{exc.message}"},
    )


@app.exception_handler(TranslatorApiException)
async def translator_api_exception_handler(
    request: Request, exc: TranslatorApiException
):
    return JSONResponse(
        status_code=503,
        content={"message": "Service currently unavailable"},
    )


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
