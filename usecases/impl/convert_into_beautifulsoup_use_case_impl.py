from usecases.convert_into_beautifulsoup_use_case import ConvertIntoBeautifulSoupUseCase

from bs4 import BeautifulSoup


class ConvertIntoBeautifulSoupUseCaseImpl(ConvertIntoBeautifulSoupUseCase):
    def execute(self, html: str) -> tuple[BeautifulSoup, str]:
        try:
            return BeautifulSoup(html, "html.parser"), ""
        except Exception as e:
            return None, f"An error occurred: {str(e)}"
