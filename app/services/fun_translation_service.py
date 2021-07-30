from app.lib.translator_api_client import TranslatorApiClient


class FunTranslationService:
    def __init__(self, style, text):
        self.endpoint = style
        self.text = text

    def call(self):
        response = TranslatorApiClient(self.endpoint, self.text).call()
        return response["contents"]["translated"]
