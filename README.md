### Install required packages
```bash
pip install -r requirements.txt
```

### Run the application
```bash
python app.py
```

### Scraper

-   To run the scraper, use the following command, replacing `{newspapers_name}` with the name of the newspaper and `{article_number}` with the number of articles you want to scrape:

```bash
python scraper.py <newspapers_name> <article_number>
```

-   Then you need to run extract.py to extract the data from the scraped articles. You can specify the minimum character count and word count for the articles you want to extract, as well as a list of newspaper names separated by spaces:

```bash
python extract.py <min_character_count> <min_word_count> <list_of_newspaper_names_separated_by_blank_spaces>
```
-   Allowed newspaper names are: `informer`, `telegraf`, `kurir`, `danas`, `alo`, `all`
