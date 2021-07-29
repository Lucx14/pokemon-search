class CustomException(Exception):
    """base custom exception"""

    def __init__(self, message="Error: external api error"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class PokemonApiException(CustomException):
    pass


class InvalidNameException(CustomException):
    pass


class TranslatorApiException(CustomException):
    pass
