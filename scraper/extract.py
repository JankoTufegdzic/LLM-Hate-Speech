import os
import sys
from utils import save_content_to_file

allowed = ["informer", "telegraf", "kurir", "alo", "danas"]

def extract_paragraphs(sources=None, min_char_count=20, min_word_count=5):
    """
    A function that extracts paragraphs from .txt file containing scraped content from newspaper websites.
    The function only retains paragraphs which have a minimum of min_char_count characters and min_word_count words.
    It saves the extracted content into a file.

    :param sources: List of newspaper names used to extract content.
    :param min_char_count: Minimum number of characters for a paragraph.
    :param min_word_count: Minimum number of words for a paragraph.
    :return: List of strings, which are extracted paragraphs.
    """

    if sources is None or len(sources) == 0: sources = allowed

    # For each newspaper source, the appropriate directory is searched for scraped content. Each .txt file is filtered
    # and the paragraphs are added to the final list.
    all_paragraphs = []
    for source in sources:
        for filename in os.listdir(source):
            if filename.endswith(".txt"):
                file_path = os.path.join(source, filename)
                with open(file_path, encoding="utf-8") as f:
                    content = f.readlines()
                    for line_no, line in enumerate(content):
                        # Skips the first line of the file, which is a link to the article.
                        if line_no == 0:
                            continue
                        line = line.strip()
                        char_count = len(line)
                        word_count = len(line.split())
                        if char_count >= min_char_count and word_count >= min_word_count:
                            all_paragraphs.append(line)

    return all_paragraphs


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 3:
        print(
            "Invalid argument count. \nUsage: python extract.py <min character count> <min word count> <list of newspapers names separated by a blank space>. \nMinimum character and word count can be 0, which defaults them to 20 and 5, respectively.\nNewspaper name is required and can be one of the following: informer, telegraf, kurir, danas, alo. \nIf no newspapers are provided, the extraction is performed for all newspapers. \n")
    else:
        min_ch_count = int(sys.argv[1])
        if min_ch_count <= 0: min_ch_count = 20

        min_wrd_count = int(sys.argv[2])
        if min_wrd_count <= 0: min_wrd_count = 5

        newspapers = []
        for i in range(3, argc):
            arg = sys.argv[i]
            print(arg)
            if arg in allowed:
                newspapers.append(arg)
            else:
                print("Invalid newspaper name: {}. Aborting.".format(arg))
                newspapers = None
                break

        if newspapers is not None:
            extracted_paragraphs = extract_paragraphs(newspapers, min_ch_count, min_wrd_count)
            save_content_to_file("extracted_text.txt", None, extracted_paragraphs)
            print("Successfully extracted paragraphs with a minimum of {} characters and {} words. Exiting.".format(min_ch_count, min_wrd_count))