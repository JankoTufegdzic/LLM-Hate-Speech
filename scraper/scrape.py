import sys
from informer import extract_informer
from telegraf import extract_telegraf
from kurir import extract_kurir
from danas import extract_danas
from alo import extract_alo

argc = len(sys.argv)
if not 2 <= argc <= 3:
    print("Invalid argument count. \nUsage: python scrape.py <newspaper_name> <article_count>. \nNewspaper name is required and can be one of the following: informer, telegraf, kurir, danas, alo, all. \nArticle count is optional (defaults to 10). \n")
else:
    valid_newspapers = ["informer", "telegraf", "kurir", "danas", "alo", "all"]
    newspaper_name = sys.argv[1]
    article_count = 10

    if argc == 3:
        article_count = int(sys.argv[2])

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