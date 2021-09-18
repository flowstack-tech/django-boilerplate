import json

import requests

from .exceptions import HttpClientErrorException


class HttpClient(object):
    """General purpose Http Client."""

    @staticmethod
    def process_response(response):
        """
        Process the Http response.

        Args:
            response: requests.response

        Returns:
            response_data: Dict

        Raises:
            Client Error if the error code is greater than 2XX
        """
        if response.ok:
            return json.loads(response.content)
        else:
            raise HttpClientErrorException(response)

    @classmethod
    def get(cls, url, headers, params=None):
        """
        Http GET Request Handler.

        Args:
            url: string
            headers: Dict
            params: Dict

        Returns:
            response: requests.response
        """
        return requests.request('GET', url, params=params, headers=headers)

    @classmethod
    def post(cls, url, data, headers, params=None):
        """
        Http POST Request Handler.

        Args:
            url: string
            data: Dict
            headers: Dict
            params: Dict

        Returns:
            response: requests.response
        """
        return requests.request('POST', url, data=json.dumps(data), params=params, headers=headers)

    @classmethod
    def put(cls, url, data, headers, params=None):
        """
        Http PUT Request Handler.

        Args:
            url: string
            data: Dict
            headers: Dict
            params: Dict

        Returns:
            response: requests.response
        """
        return requests.request('PUT', url, data=json.dumps(data), params=params, headers=headers)

    @classmethod
    def delete(cls, url, headers, params=None):
        """
        Http POST Request Handler.

        Args:
            url: string
            headers: Dict
            params: Dict

        Returns:
            response: requests.response
        """
        return requests.request('DELETE', url, params=params, headers=headers)
