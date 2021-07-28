import unittest
from unittest.mock import patch
from app.services.fun_translation_service import FunTranslationService
from .helpers.payload_helpers import TRANSLATOR_SUCCESS
from .helpers.message_helpers import YODA_STYLE, TEST_TEXT


class FunTranslationServiceTest(unittest.TestCase):
    @patch("app.services.fun_translation_service.TranslatorApiClient")
    def test_fun_translation(self, client_mock):
        # set mock return value - set up a dummy with real pattern
        client_mock.return_value.call.return_value = TRANSLATOR_SUCCESS

        # Call the service
        response = FunTranslationService(YODA_STYLE, TEST_TEXT).call()
        assert response == "Lost a planet,  master obiwan has."

        # Check the api was called with the style and the text
        client_mock.assert_called_once_with(YODA_STYLE, TEST_TEXT)
