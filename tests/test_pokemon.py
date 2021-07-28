# from app.lib.pokemon_api_client import PokemonApiClient, ClientError
from unittest.case import expectedFailure
from app.models.pokemon import Pokemon
from .helpers.dummy_payloads import (
    VALID_PAYLOAD,
    INVALID_DESCRIPTION_PAYLOAD,
    INVALID_HABITAT_PAYLOAD,
)
import unittest


class PokemonTest(unittest.TestCase):
    def test_attributes_with_valid_payload(self):
        pokemon = Pokemon(VALID_PAYLOAD)
        expected_description = "It was created by a scientist after years of horrific gene splicing and DNA engineering experiments."
        assert pokemon.get_name() == "charizard"
        assert pokemon.get_version() == "red"
        assert pokemon.get_description() == expected_description
        assert pokemon.get_habitat() == "mountain"
        assert pokemon.get_is_legendary() == False

    def test_no_english_description(self):
        pokemon = Pokemon(INVALID_DESCRIPTION_PAYLOAD)
        assert pokemon.get_name() == "charizard"
        assert pokemon.get_version() == "red"
        assert pokemon.get_description() == "Unknown"
        assert pokemon.get_habitat() == "mountain"
        assert pokemon.get_is_legendary() == False

    def test_no_habitat(self):
        pokemon = Pokemon(INVALID_HABITAT_PAYLOAD)
        expected_description = "It was created by a scientist after years of horrific gene splicing and DNA engineering experiments."
        assert pokemon.get_name() == "charizard"
        assert pokemon.get_version() == "red"
        assert pokemon.get_description() == expected_description
        assert pokemon.get_habitat() == "Unknown"
        assert pokemon.get_is_legendary() == False
