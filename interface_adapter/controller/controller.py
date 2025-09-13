from typing import Tuple

from usecases.fetch_url_use_case import FetchUrlUseCase as fu
from usecases.convert_into_beautifulsoup_use_case import (
    ConvertIntoBeautifulSoupUseCase as cibsu,
)
from usecases.get_one_tag_use_case import GetOneTagUseCase as gotu


class Controller:
    def __init__(
        self,
        fetch_url_use_case: fu,
        convert_into_beautifulsoup_use_case: cibsu,
        get_one_tag_use_case: gotu,
    ):
        self.fetch_url_use_case = fetch_url_use_case
        self.convert_into_beatifulsoup_use_case = convert_into_beautifulsoup_use_case
        self.get_one_tag_use_case = get_one_tag_use_case

    def fetch_url(self, url: str) -> Tuple[str, str]:
        return self.fetch_url_use_case.execute(url)
