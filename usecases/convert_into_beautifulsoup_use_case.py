from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class ConvertIntoBeautifulSoupUseCase(ABC):
    @abstractmethod
    def execute(self, html: str) -> BeautifulSoup:
        pass
