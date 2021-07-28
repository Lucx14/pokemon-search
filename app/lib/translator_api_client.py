import requests
from ..utils.app_exceptions import ClientError


class TranslatorApiClient:
    BASE_URI = "https://api.funtranslations.com/translate/"

    def __init__(self, endpoint, text):
        self.endpoint = endpoint
        self.text = text

    def call(self):
        try:
            response = requests.get(f"{self.BASE_URI}{self.endpoint}?text={self.text}")
        except Exception as err:
            raise ClientError(f"Error: Translator api error: {err}")

        if response.status_code == 200:
            return response.json()
        # Catch the rate limit error and handle the response
        elif response.status_code == 429:
            return {"contents": {"translated": self.text}}
        else:
            raise ClientError(f"Another error: {response.status_code}")
