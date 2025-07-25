from bs4 import BeautifulSoup
import requests
import re


def extract_text_from_single_page(website_url):
    """
    The function loads the HTML content of the page with the provided website URL and extracts the text from it.
    If the page contains an article tag, the cursor is moved into it. The current element is searched for all paragraphs.
    The paragraphs are formatted, so that multiple blank spaces are converted into a single blank space.

    :param website_url: URL of the website page that will be used for text extraction.
    :return: List of strings representing the text extracted from the website page.
    """

    try:
        html_code = requests.get(website_url).text
        parsed_html = BeautifulSoup(html_code, "lxml")
        extracted_text = []
        regex_whitespaces = re.compile(r"\s+")

        article = parsed_html.find('article')
        if article:
            parsed_html = article

        paragraphs = parsed_html.find_all('p')
        for paragraph in paragraphs:
            unformatted_text = paragraph.get_text().strip()
            formatted_text = regex_whitespaces.sub(" ", unformatted_text).strip()
            if formatted_text:
                extracted_text.append(formatted_text)

        return extracted_text
    except Exception:
        return []