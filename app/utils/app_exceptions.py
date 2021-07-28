class ClientError(Exception):
    """Exception raised if we are unable to get a response from the api"""

    def __init__(self, message="Error: api error"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
