from app.lib.pokemon_api_client import PokemonApiClient
from app.utils.app_exceptions import PokemonApiException, InvalidNameException
from tests.helpers.mock_helpers import MockResponse, throw_an_exception
from tests.helpers.message_helpers import (
    POKE_API_ERROR,
    NAME_ERROR,
    TEST_ENDPOINT,
    TEST_NAME,
)
from unittest.mock import patch
import unittest
import pytest


class PokemonApiClientTest(unittest.TestCase):
    @patch("app.lib.pokemon_api_client.requests.get")
    def test_getting_pokemon(self, mock_api_call):
        mock_api_call.return_value = MockResponse({"name": "test"}, 200)
        expected_test_url = f"https://pokeapi.co/api/v2/{TEST_ENDPOINT}{TEST_NAME}"
        response = PokemonApiClient(TEST_ENDPOINT, TEST_NAME).call()

        mock_api_call.assert_called_once_with(expected_test_url)

        assert response != None
        assert response == {"name": "test"}

    @patch("app.lib.pokemon_api_client.requests.get")
    def test_api_failure(self, mock_api_call):
        # set the mock api call to raise an exception
        mock_api_call.side_effect = throw_an_exception

        # assert we will raise our custom error with message
        with pytest.raises(PokemonApiException, match=POKE_API_ERROR):
            PokemonApiClient(TEST_ENDPOINT, TEST_NAME).call()

    @patch("app.lib.pokemon_api_client.requests.get")
    def test_invalid_pokemon_name(self, mock_api_call):
        # Set up a dummy return value for the mocked api call with a not found status
        mock_api_call.return_value = MockResponse({}, 404)

        # assert we will raise our custom error with message
        with pytest.raises(InvalidNameException, match=NAME_ERROR):
            PokemonApiClient(TEST_ENDPOINT, TEST_NAME).call()
