from scraper.utils import save_content_to_file
from bs4 import BeautifulSoup
import requests
import os


def extract_content_from_single_article_kurir(website_url):
    """
    Extract content (text) from a single article from the kurir website using BeautifulSoup.

    :param website_url: URL of the article that needs to have its content extracted.
    :return: A list of strings corresponding to the paragraphs in the article.
    """

    html_code = requests.get(website_url).text
    parsed_html = BeautifulSoup(html_code, "lxml")

    news_content = parsed_html.find("div", class_="article-body")

    # Parameter recursive=False eliminates paragraphs from nested tags, such as related news, etc.
    ignore_classes = []
    paragraph_containers = news_content.find_all(["div"], class_="article-rte")
    extracted_text = []

    # For each of the extracted paragraphs, the code extracts the text without formatting tags (strong, a, ...).
    for paragraph_container in paragraph_containers:
        paragraphs = paragraph_container.find_all("p", recursive=False)
        for paragraph in paragraphs:
            if paragraph.find(["p", "div"], class_=ignore_classes):
                continue
            text = paragraph.get_text(separator=" ", strip=True)

            # Converts &nbsp; into a single blank space.
            text = text.replace('\xa0', ' ')
            if text:
                extracted_text.append(text)

    return extracted_text


def get_article_urls_kurir(main_page_url, base_url, max_article_count=10):
    """
    Generates a list of article URLs from the kurir website's newest articles page.

    :param main_page_url: URL of the page, which contains the list of the newest articles.
    :param base_url: Website's base URL used for appending relative hyperlinks.
    :param max_article_count: Maximum number of articles to extract.
    :return: List of strings corresponding to the article URLs.
    """

    # Website specific (the last page on the website is page 9). Each page contains 50 article cards.
    max_page_limit = 9

    current_page_number = 1
    current_article_count = 0
    article_urls = []

    # Iterates through the pages of the article list and extracts article URLs.
    while current_page_number <= max_page_limit and current_article_count < max_article_count:
        current_page_url = "{}/page/{}".format(main_page_url, current_page_number)

        html_code = requests.get(current_page_url).text
        parsed_html = BeautifulSoup(html_code, "lxml")
        article_list = parsed_html.find("div", class_="latest-news-list-feed")

        for article in article_list.find_all("a", class_="in-feed"):
            # If the href is an absolute link, only keep that link, and if it's a relative link, append to the base url.
            if "http" in article.get("href"):
                url = article.get("href")
            else:
                url = base_url + article.get("href")
            article_urls.append(url)
            current_article_count += 1
            if current_article_count >= max_article_count:
                break

        current_page_number += 1

    return article_urls


def extract_kurir(article_count):
    """
    Extracts content from the kurir website using BeautifulSoup. Creates a .txt file for each article.
    Each .txt file contains the URL of the article in the first line, and all lines after it contain the article's text.

    :param article_count: Maximum number of articles used to extract content.
    :return: None

    """

    website = "kurir"
    website_base_url = "https://www.kurir.rs"
    website_main_page_url = "https://www.kurir.rs/najnovije-vesti"

    os.makedirs(website, exist_ok=True)

    print("Extracting articles from {}...".format(website))
    article_url_list = get_article_urls_kurir(website_main_page_url, website_base_url, article_count)
    success_cnt = 0
    for cnt, url in enumerate(article_url_list):
        article_text = extract_content_from_single_article_kurir(url)
        file_path = "{}/{}.txt".format(website, cnt)
        save_content_to_file(file_path, url, article_text)
        success_cnt += 1
    print("Successfully extracted {}/{} articles from {}.".format(success_cnt, article_count, website))


if __name__ == "__main__":
    extract_kurir(10)