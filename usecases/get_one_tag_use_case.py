from abc import ABC, abstractmethod
from bs4 import BeautifulSoup as bs


class GetOneTagUseCase(ABC):
    @abstractmethod
    def execute(self, tag_name: str, html: str, soup: bs) -> tuple[str, str]:
        """This function will return a tuple containing the tag and an error message
        Args:
            tag_name (str): The name of the tag
            html (str): The HTML content
            soup (bs): The BeautifulSoup object
        Returns:
            tuple[str, str]: A tuple containing the tag and an error message
        """
        pass
