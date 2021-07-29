from app.models.pokemon import Pokemon
from .helpers.payload_helpers import (
    VALID_PAYLOAD,
    YODA_PAYLOAD,
    INVALID_DESCRIPTION_PAYLOAD,
    INVALID_HABITAT_PAYLOAD,
)
from .helpers.message_helpers import YODA_STYLE, SHAKESPEARE_STYLE
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

    def test_determines_translation_style_when_shakespeare(self):
        pokemon = Pokemon(VALID_PAYLOAD)
        assert pokemon.translation_style() == SHAKESPEARE_STYLE

    def test_determines_translation_style_when_yoda(self):
        pokemon = Pokemon(YODA_PAYLOAD)
        assert pokemon.translation_style() == YODA_STYLE
