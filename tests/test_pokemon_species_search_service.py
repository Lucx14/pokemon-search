import unittest
from unittest.mock import patch
from app.services.pokemon_species_search_service import PokemonSpeciesSearchService


class PokemonSpeciesSearchServiceTest(unittest.TestCase):
    @patch("app.services.pokemon_species_search_service.PokemonApiClient")
    def test_pokemon_species_search(self, client_mock):
        # set up parameters to test with
        endpoint = "/pokemon-species/"
        test_name = "test_name"

        # Set mock return value to help with testing
        client_mock.return_value.call.return_value = "Mocked API client return value"

        # Call the service
        response = PokemonSpeciesSearchService(test_name).call()
        assert response == "Mocked API client return value"

        # Check the Api Client was called with the endpoint and the test name
        client_mock.assert_called_once_with(endpoint, test_name)
