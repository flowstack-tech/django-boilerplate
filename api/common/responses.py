class ErrorResponse:
    """generic error response."""

    def __init__(self, message):
        self.response = {'message': message}

    def get_response(self, data=None):
        """Get serialized response.

        Returns:
            Dict
        """
        if data:
            return {**self.response, **data}
        return self.response


class OkResponse:
    """generic ok response."""

    def __init__(self, message):
        self.response = {'message': message}

    def get_response(self, data=None):
        """Get serialized response.

        Returns:
            Dict
        """
        if data:
            return {**self.response, **data}
        return self.response
