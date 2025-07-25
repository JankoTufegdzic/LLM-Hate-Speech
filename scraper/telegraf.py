from scraper.utils import save_content_to_file
from bs4 import BeautifulSoup
import requests
import os


def extract_content_from_single_article_telegraf(website_url):
    """
    Extract content (text) from a single article from the telegraf website using BeautifulSoup.

    :param website_url: URL of the article that needs to have its content extracted.
    :return: A list of strings corresponding to the paragraphs in the article.
    """

    html_code = requests.get(website_url).text
    parsed_html = BeautifulSoup(html_code, "lxml")

    news_content = parsed_html.find("div", class_="article-content")

    # Parameter recursive=False eliminates paragraphs from nested tags, such as related news, etc.
    ignore_classes = []
    paragraphs = news_content.find_all(["p"], recursive=False)
    extracted_text = []

    # For each of the extracted paragraphs, the code extracts the text without formatting tags (strong, a, ...).
    for paragraph in paragraphs:
        if paragraph.find(["p", "div"], class_=ignore_classes):
            continue
        text = paragraph.get_text(separator=" ", strip=True)

        # Converts &nbsp; into a single blank space. Appends text only if it's non-empty.
        text = text.replace('\xa0', ' ')
        if text:
            extracted_text.append(text)

    # Deletes last paragraph from the list because it's irrelevant info (Telegraf signature).
    extracted_text.pop()

    return extracted_text


def get_article_urls_telegraf(main_page_url, max_article_count=10):
    """
    Generates a list of article URLs from the telegraf website's newest articles page.

    :param main_page_url: URL of the page, which contains the list of the newest articles.
    :param max_article_count: Maximum number of articles to extract.
    :return: List of strings corresponding to the article URLs.
    """

    current_article_count = 0
    article_urls = []

    # Locates the div which contains all article links.
    html_code = requests.get(main_page_url).text
    parsed_html = BeautifulSoup(html_code, "lxml")
    article_list = parsed_html.find("div", class_="filter-page-content-inner")

    # For each article item from the list, a link to the article is extracted.
    for article in article_list.find_all("div", class_="grid-image-wrapper"):
        link = article.find("a").get("href")
        article_urls.append(link)
        current_article_count += 1
        if current_article_count >= max_article_count:
            break

    return article_urls


def extract_telegraf(article_count=10):
    """
    Extracts content from the telegraf website using BeautifulSoup. Creates a .txt file for each article.
    Each .txt file contains the URL of the article in the first line, and all lines after it contain the article's text.

    :param article_count: Maximum number of articles used to extract content.
    :return: None

    """

    website = "telegraf"
    website_main_page_url = "https://www.telegraf.rs/najnovije-vesti"

    os.makedirs(website, exist_ok=True)

    print("Extracting articles from {}...".format(website))
    article_url_list = get_article_urls_telegraf(website_main_page_url, article_count)
    success_cnt = 0

    for cnt, url in enumerate(article_url_list):
        article_text = extract_content_from_single_article_telegraf(url)
        file_path = "{}/{}.txt".format(website, cnt)
        save_content_to_file(file_path, url, article_text)
        success_cnt += 1
    print("Successfully extracted {}/{} articles from {}.".format(success_cnt, article_count, website))


if __name__ == "__main__":
    extract_telegraf(10)

