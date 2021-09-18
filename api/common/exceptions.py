import json


class OtpNotSentException(Exception):
    pass


class HttpClientErrorException(Exception):
    def __init__(self, response):
        self.value = {'message': json.loads(response.content), 'status': response.status_code}

    def __str__(self):
        """
        Define the __str__ method in case we want to serialize the exception.

        Returns:
            Serializable representation
        """
        return repr(self.value)


class S3PresignedUrlException(Exception):
    def __init__(self, e):
        self.value = e

    def __str__(self):
        """
        Define the __str__ method in case we want to serialize the exception.

        Returns:
            Serializable representation
        """
        return repr(self.value)
