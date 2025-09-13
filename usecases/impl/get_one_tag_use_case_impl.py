from bs4 import BeautifulSoup as bs
from usecases.get_one_tag_use_case import GetOneTagUseCase


class GetOneTagUseCaseImpl(GetOneTagUseCase):
    def execute(self, soup: bs, tag: str) -> tuple[bs, str]:
        try:
            return soup.find(tag), ""
        except Exception as e:
            return None, f"An error occurred: {str(e)}"
