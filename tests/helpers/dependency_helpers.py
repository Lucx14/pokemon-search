from .payload_helpers import VALID_PAYLOAD
from app.utils.app_exceptions import InvalidNameException, PokemonApiException


async def poke_api_dependency_success():
    return VALID_PAYLOAD


async def poke_api_dependency_invalid_name():
    raise InvalidNameException("Test Error")


async def poke_api_dependency_fail():
    raise PokemonApiException("Test Error")
