from utils import save_content_to_file
from bs4 import BeautifulSoup
import requests
import os


def extract_content_from_single_article_alo(website_url):
    """
    Extract content (text) from a single article from the alo website using BeautifulSoup.

    :param website_url: URL of the article that needs to have its content extracted.
    :return: A list of strings corresponding to the paragraphs in the article.
    """

    html_code = requests.get(website_url).text
    parsed_html = BeautifulSoup(html_code, "lxml")
    extracted_text = []

    # Separate element contains the introductory text in the article, so it's the first to be extracted.
    header_container = parsed_html.find("div", class_="single-news-lead-text")
    if header_container: extracted_text.append(header_container.p.get_text(separator=" ", strip=True))

    news_content = parsed_html.find("div", class_="single-news-content")

    # Some articles have their paragraphs in a separate subsection, so if its found, the main div is changed accordingly.
    subsection = news_content.find("div", class_="single-news-inner")
    if subsection: news_content = subsection

    # Parameter recursive=False eliminates paragraphs from nested tags, such as related news, etc.
    ignore_classes = []
    paragraphs = news_content.find_all(["p"], recursive=False)

    # For each of the extracted paragraphs, the code extracts the text without formatting tags (strong, a, ...).
    for paragraph in paragraphs:
        if paragraph.find(["p", "div"], class_=ignore_classes):
            continue
        text = paragraph.get_text(separator=" ", strip=True)

        # Converts &nbsp; into a single blank space.
        text = text.replace('\xa0', ' ')
        if text:
            extracted_text.append(text)

    # Removes the last line which is the newspapers' signature.
    if len(extracted_text) > 1: extracted_text.pop()

    return extracted_text


def get_article_urls_alo(main_page_url, base_url, max_article_count=10):
    """
    Generates a list of article URLs from the alo website's newest articles page.

    :param main_page_url: URL of the page, which contains the list of the newest articles.
    :param base_url: Website's base URL used for appending relative hyperlinks.
    :param max_article_count: Maximum number of articles to extract.
    :return: List of strings corresponding to the article URLs.
    """

    # Website specific (the last page on the website is page 40). Each page contains 25 article cards.
    max_page_limit = 40

    current_page_number = 1
    current_article_count = 0
    article_urls = []

    # Iterates through the pages of the article list and extracts article URLs.
    while current_page_number <= max_page_limit and current_article_count < max_article_count:
        current_page_url = "{}?page={}".format(main_page_url, current_page_number)

        html_code = requests.get(current_page_url).text
        parsed_html = BeautifulSoup(html_code, "lxml")
        article_list = parsed_html.find("div", class_="news-list")

        for article in article_list.find_all("a", class_="news-item-image"):
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


def extract_alo(article_count):
    """
    Extracts content from the alo website using BeautifulSoup. Creates a .txt file for each article.
    Each .txt file contains the URL of the article in the first line, and all lines after it contain the article's text.

    :param article_count: Maximum number of articles used to extract content.
    :return: None

    """

    website = "alo"
    website_base_url = "https://alo.rs"
    website_main_page_url = "https://www.alo.rs/live"

    os.makedirs(f"data/{website}", exist_ok=True)

    print("Extracting articles from {}...".format(website))
    article_url_list = get_article_urls_alo(website_main_page_url, website_base_url, article_count)
    success_cnt = 0
    for cnt, url in enumerate(article_url_list):
        article_text = extract_content_from_single_article_alo(url)
        file_path = "data/{}/{}.txt".format(website, cnt)
        save_content_to_file(file_path, url, article_text)
        success_cnt += 1
    print("Successfully extracted {}/{} articles from {}.".format(success_cnt, article_count, website))

    # url = "https://www.alo.rs/vesti/svet/1091473/zvanicno-je-naredeno-povlaci-se-vojska/vest"
    # abc = [print(a) for a in extract_content_from_single_article_alo(url)]


if __name__ == "__main__":
    extract_alo(10)