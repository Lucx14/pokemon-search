import requests
from app.utils.app_exceptions import TranslatorApiException


class TranslatorApiClient:
    BASE_URI = "https://api.funtranslations.com/translate/"

    def __init__(self, endpoint, text):
        self.endpoint = endpoint
        self.text = text

    def call(self):
        try:
            response = requests.get(f"{self.BASE_URI}{self.endpoint}?text={self.text}")
        except Exception as err:
            raise TranslatorApiException(f"Error: Translator api error: {err}") from err

        if response.status_code == 200:
            return response.json()
        if response.status_code == 429:
            return {"contents": {"translated": self.text}}
        raise TranslatorApiException(
            f"Error: Translator api error: {response.status_code}"
        )
