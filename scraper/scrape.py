import sys
from informer import extract_informer, extract_content_from_single_article_informer
from telegraf import extract_telegraf, extract_content_from_single_article_telegraf
from kurir import extract_kurir, extract_content_from_single_article_kurir
from danas import extract_danas, extract_content_from_single_article_danas
from alo import extract_alo, extract_content_from_single_article_alo
from general_scraper import extract_text_from_single_page
from utils import save_content_to_file


def perform_scrape(website_url):
    """
    The function calls an appropriate scrape function based on the provided URL and saves the scraped content
    to the 'extracted_unfiltered_text.txt' file.

    :param website_url: URL of the website used for content scraping.
    :return: None
    """
    print("Extracting text from '{}'...".format(website_url))

    if "informer.rs" in website_url:
        content = extract_content_from_single_article_informer(website_url)
    elif "telegraf.rs" in website_url:
        content = extract_content_from_single_article_telegraf(website_url)
    elif "kurir.rs" in website_url:
        content = extract_content_from_single_article_kurir(website_url)
    elif "danas.rs" in website_url:
        content = extract_content_from_single_article_danas(website_url)
    elif "alo.rs" in website_url:
        content = extract_content_from_single_article_alo(website_url)
    else:
        content = extract_text_from_single_page(website_url)

    save_content_to_file("extracted_unfiltered_text.txt", website_url, content)
    file_path = "extracted_unfiltered_text.txt"

    save_content_to_file(file_path, website_url, content)
    print("Successfully extracted text content from the website page and saved to 'unfiltered_text.txt'.")


if __name__ == "__main__":
    argc = len(sys.argv)
    if not 3 <= argc <= 4:
        print("Invalid argument count. \n\nUsage: \n1) python scrape.py newspaper <newspaper_name> <article_count>. \nNewspaper name is required and can be one of the following: informer, telegraf, kurir, danas, alo, all. Article count is optional (defaults to 10). \n\n2) python scrape.py url <website_url>. \nWebsite url is an arbitrary website url.")
    else:
        valid_newspapers = ["informer", "telegraf", "kurir", "danas", "alo", "all"]
        extraction_type = sys.argv[1]

        if extraction_type == "newspaper":
            newspaper_name = sys.argv[2]
            article_count = 10

            if argc == 4:
                article_count = int(sys.argv[3])

            if newspaper_name not in valid_newspapers:
                print("Invalid newspaper name. Valid options are: informer, telegraf, kurir, danas, alo, all. Aborting.")
            elif article_count <= 0:
                print("Invalid article count. Aborting.")
            else:
                if newspaper_name == "informer" or newspaper_name == "all":
                    extract_informer(article_count)
                if newspaper_name == "telegraf" or newspaper_name == "all":
                    extract_telegraf(article_count)
                if newspaper_name == "kurir" or newspaper_name == "all":
                    extract_kurir(article_count)
                if newspaper_name == "danas" or newspaper_name == "all":
                    extract_danas(article_count)
                if newspaper_name == "alo" or newspaper_name == "all":
                    extract_alo(article_count)
                print("Successfully extracted. Exiting.")
        elif extraction_type == "url":
            url = sys.argv[2]
            perform_scrape(url)
        else:
            print("Invalid extraction type. Allowed types are 'newspaper' and 'url'. Aborting.")