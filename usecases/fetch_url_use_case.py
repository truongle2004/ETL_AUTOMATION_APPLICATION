from typing import Tuple
from abc import ABC, abstractmethod
from requests import Response


class FetchUrlUseCase(ABC):
    @abstractmethod
    def execute(self, url: str) -> Tuple[Response, str]:
        pass
