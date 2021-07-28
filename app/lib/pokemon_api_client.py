import requests

# maybe extract to a helpers/errors directory to tidy up??
class ClientError(Exception):
    """Exception raised if we are unable to get a response from the pokemon api"""

    def __init__(self, message="Error: Pokemon api error"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class PokemonApiClient:
    BASE_URI = "https://pokeapi.co/api/v2/"

    def __init__(self, endpoint, params):
        self.endpoint = endpoint
        self.params = params

    def call(self):
        try:
            response = requests.get(f"{self.BASE_URI}{self.endpoint}{self.params}")
        except Exception as err:
            raise ClientError(f"Error: Pokemon api error: {err}")

        if response.status_code == 200:
            return response.json()
        else:
            # This will occur if the name is wrong you get a status 404 not found
            raise ClientError("Error: Pokemon NOT FOUND possible name error")
