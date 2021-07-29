import unittest
from unittest.mock import patch
from app.services.pokemon_species_search_service import PokemonSpeciesSearchService
from .helpers.message_helpers import TEST_NAME, SPECIES_ENDPOINT, MOCK_RETURN


class PokemonSpeciesSearchServiceTest(unittest.TestCase):
    @patch("app.services.pokemon_species_search_service.PokemonApiClient")
    def test_pokemon_species_search(self, client_mock):
        client_mock.return_value.call.return_value = MOCK_RETURN

        response = PokemonSpeciesSearchService(TEST_NAME).call()
        assert response == MOCK_RETURN

        client_mock.assert_called_once_with(SPECIES_ENDPOINT, TEST_NAME)
