from unittest import mock
from fastapi.testclient import TestClient
from .helpers.dependency_helpers import (
    poke_api_dependency_success,
    poke_api_dependency_invalid_name,
    poke_api_dependency_fail,
)
from app.main import app, pokemon_data
from unittest.mock import patch
from .helpers.mock_helpers import throw_translator_api_exception


client = TestClient(app)


def test_successful_pokemon_lookup():
    app.dependency_overrides[pokemon_data] = poke_api_dependency_success
    response = client.get("/pokemon/charizard")
    assert response.status_code == 200
    assert response.json() == {
        "name": "charizard",
        "version": "red",
        "description": "It was created by a scientist after years of horrific gene splicing and DNA engineering experiments.",
        "habitat": "mountain",
        "is_legendary": False,
    }


def test_invalid_name_pokemon_lookup():
    app.dependency_overrides[pokemon_data] = poke_api_dependency_invalid_name
    response = client.get("/pokemon/invalid")
    assert response.status_code == 404
    assert response.json() == {"message": "Test Error"}


def test_pokemon_api_fail():
    app.dependency_overrides[pokemon_data] = poke_api_dependency_fail
    response = client.get("/pokemon/mewtwo")
    assert response.status_code == 503
    assert response.json() == {"message": "Service currently unavailable"}


@patch("app.main.FunTranslationService")
def test_successful_translated_pokemon(mock_translator):
    app.dependency_overrides[pokemon_data] = poke_api_dependency_success
    mock_translator.return_value.call.return_value = "dummy translated text"
    response = client.get("/pokemon/translated/charizard")
    assert response.status_code == 200
    assert response.json() == {
        "name": "charizard",
        "version": "red",
        "description": "dummy translated text",
        "habitat": "mountain",
        "is_legendary": False,
    }


@patch("app.main.FunTranslationService")
def test_translator_service_fail(mock_translator):
    app.dependency_overrides[pokemon_data] = poke_api_dependency_success
    mock_translator.side_effect = throw_translator_api_exception
    response = client.get("/pokemon/translated/charizard")
    assert response.status_code == 503
    assert response.json() == {"message": "Service currently unavailable"}
