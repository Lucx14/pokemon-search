from app.lib.pokemon_api_client import PokemonApiClient, ClientError
from unittest.mock import patch
import unittest
import pytest

# Maybe put in something like a test helpers file??
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def my_side_effect(arg):
    raise Exception("Test")


API_ERROR = "Error: Pokemon api error: Test"
NAME_ERROR = "Error: Pokemon NOT FOUND possible name error"


class PokemonApiClientTest(unittest.TestCase):
    @patch("app.lib.pokemon_api_client.requests.get")
    def test_getting_pokemon(self, mock_api_call):
        # Set up a dummy return value for the mocked api call
        mock_api_call.return_value = MockResponse({"name": "test"}, 200)

        endpoint = "test/"
        name_param = "testname/"
        expected_test_url = f"https://pokeapi.co/api/v2/{endpoint}{name_param}"

        # call on the Api CLient
        response = PokemonApiClient(endpoint, name_param).call()

        # test an api call was sent to the expected url
        mock_api_call.assert_called_once_with(expected_test_url)

        assert response != None
        assert response == {"name": "test"}

    @patch("app.lib.pokemon_api_client.requests.get")
    def test_api_failure(self, mock_api_call):
        # set the mock api call to raise an exception
        mock_api_call.side_effect = my_side_effect

        endpoint = "invalid-endpoint/"
        name_param = "testname/"

        # assert we will raise our custom error with message
        with pytest.raises(ClientError, match=API_ERROR):
            PokemonApiClient(endpoint, name_param).call()

    @patch("app.lib.pokemon_api_client.requests.get")
    def test_invalid_pokemon_name(self, mock_api_call):
        # Set up a dummy return value for the mocked api call with a not found status
        mock_api_call.return_value = MockResponse({}, 404)

        # note the url we expect the call to go to based on input
        endpoint = "test/"
        name_param = "invalidtestname/"

        # assert we will raise our custom error with message
        with pytest.raises(ClientError, match=NAME_ERROR):
            PokemonApiClient(endpoint, name_param).call()
