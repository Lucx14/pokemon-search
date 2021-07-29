from app.utils.app_exceptions import TranslatorApiException


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def throw_an_exception(*args):
    raise Exception("Test")


def throw_translator_api_exception(*args):
    raise TranslatorApiException("Test")
