from requests import get, Response, RequestException
from typing import Tuple
from usecases.fetch_url_use_case import FetchUrlUseCase


class FetchUrlUseCaseImpl(FetchUrlUseCase):
    def __init__(self):
        pass

    def execute(self, url: str) -> Tuple[Response, str]:
        """
        Fetches the content of the provided URL.

        Returns:
            Tuple[str, str]: A tuple containing the fetched content and an error message.
        """
        # TODO: validate the standard of a url
        print("use case is called")
        if not url:
            return "", "URL cannot be empty or None"
        try:
            response = get(url)
            if response.status_code == 200:
                return response, ""
            else:
                return "", f"Failed to fetch URL: HTTP {response.status_code}"
        except RequestException as e:
            return "", f"An error occurred: {str(e)}"
