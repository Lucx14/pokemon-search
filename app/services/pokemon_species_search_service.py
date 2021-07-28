from ..lib.pokemon_api_client import PokemonApiClient


class PokemonSpeciesSearchService:
    ENDPOINT_URL = "/pokemon-species/"

    def __init__(self, params):
        self.search_term = params

    def call(self):
        return PokemonApiClient(self.ENDPOINT_URL, self.search_term).call()
