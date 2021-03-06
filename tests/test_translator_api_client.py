from app.lib.translator_api_client import TranslatorApiClient
from app.utils.app_exceptions import TranslatorApiException
from tests.helpers.payload_helpers import (
    TRANSLATOR_SUCCESS,
    TRANSLATOR_RATE_LIMIT_EXCEEDED,
)
from tests.helpers.mock_helpers import MockResponse, throw_an_exception
from tests.helpers.message_helpers import TRANSLATOR_API_ERROR, TEST_ENDPOINT, QUERY
from unittest.mock import patch
import unittest
import pytest


class TranslatorApiClientTest(unittest.TestCase):
    @patch("app.lib.translator_api_client.requests.get")
    def test_text_translation(self, mock_api_call):
        mock_api_call.return_value = MockResponse(TRANSLATOR_SUCCESS, 200)
        expected_test_url = (
            f"https://api.funtranslations.com/translate/{TEST_ENDPOINT}?text={QUERY}"
        )
        response = TranslatorApiClient(TEST_ENDPOINT, QUERY).call()

        mock_api_call.assert_called_once_with(expected_test_url)

        assert response != None
        assert response == TRANSLATOR_SUCCESS

    @patch("app.lib.translator_api_client.requests.get")
    def test_api_failure(self, mock_api_call):
        # set the mock api call to raise an exception
        mock_api_call.side_effect = throw_an_exception

        # assert we will raise our custom error with message
        with pytest.raises(TranslatorApiException, match=TRANSLATOR_API_ERROR):
            TranslatorApiClient(TEST_ENDPOINT, QUERY).call()

    @patch("app.lib.translator_api_client.requests.get")
    def test_rate_limit_exceeded(self, mock_api_call):
        # Set up a dummy return value for the mocked api call
        mock_api_call.return_value = MockResponse(TRANSLATOR_RATE_LIMIT_EXCEEDED, 429)
        response = TranslatorApiClient(TEST_ENDPOINT, QUERY).call()

        assert response != None
        assert response == {"contents": {"translated": QUERY}}
