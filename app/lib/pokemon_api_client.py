import requests
from ..utils.app_exceptions import PokemonApiException, InvalidNameException


class PokemonApiClient:
    BASE_URI = "https://pokeapi.co/api/v2/"

    def __init__(self, endpoint, params):
        self.endpoint = endpoint
        self.params = params

    def call(self):
        try:
            response = requests.get(f"{self.BASE_URI}{self.endpoint}{self.params}")
        except Exception as err:
            raise PokemonApiException(f"Error: Pokemon api error: {err}") from err

        if response.status_code == 200:
            return response.json()
        if response.status_code == 404:
            raise InvalidNameException("Error: NOT FOUND possible name error")
        raise PokemonApiException("Error: Pokemon api error")
