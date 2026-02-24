from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from llm.llm_purifier import LLM_Pufirier
from llm.llm_highlighter import LLM_Highlighter
from scraper.scrape import perform_scrape
from scraper.extract import filter_general_text

app = Flask(__name__)

model_name="mistral"
llm_purifier = LLM_Pufirier(model_name=model_name)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/change', methods=['GET', 'POST'])
def change():
    input_text = ''
    output_text = ''
    if request.method == 'POST':
        input_text = request.form.get('user_input', '')

        output_text, similarity, neutral_statement = llm_purifier.purify(input_text)
        if neutral_statement:
            output_text = "[Neutralna poruka] " + output_text
        else:
            output_text = f"[{similarity:.2f}] " + output_text

    return render_template('change.html', input_text=input_text, output_text=output_text)

def mark_entire_sentence(text):
    # Find all sentences using a simple sentence end pattern
    sentence_pattern = r'[^.!?]*<mark>.*?</mark>[^.!?]*[.!?]'
    matches = re.findall(sentence_pattern, text)

    for sentence in matches:
        clean_sentence = re.sub(r'</?mark>', '', sentence)  # remove existing <mark> tags
        full_marked = f"<mark>{clean_sentence.strip()}</mark>"
        text = text.replace(sentence, full_marked)

    return text

@app.route('/highlight', methods=['GET', 'POST'])
def highlight():
    highlighted_text = ''
    url = ''
    if request.method == 'POST':
        url = request.form.get('url_input', '')
        try:
            highlighted_text = call_highlight_api(url)
            print(highlighted_text)
        except Exception as e:
            highlighted_text = f'<span class="text-danger">Error: {str(e)}</span>'
    return render_template('highlight.html', highlighted_text=highlighted_text, url=url)


def call_highlight_api(url):
    llm_highlighter=LLM_Highlighter(model_name=model_name)

    min_char_count = 20
    min_word_count = 5
    perform_scrape(url)
    text_list = filter_general_text(min_char_count, min_word_count)
    words = " ".join(text_list)

    highlighted_text=llm_highlighter.highlight(words)
    marked_parts = re.findall(r"<mark>(.*?)</mark>", highlighted_text)

    for mark in marked_parts:
        words = re.sub(mark[1:-1], f"<mark>{mark[1:-1]}</mark>", words)

    highlighted_text = mark_entire_sentence(words)
    return highlighted_text


def count_marked_sentences(text):
    """Count how many sentences are marked in the text"""
    if not text or not isinstance(text, str):
        return 0
    return len(re.findall(r'<mark>[^<]*</mark>', text))


def highlight_results(input_csv, output_csv):    
    df = pd.read_csv(input_csv)

    results = []
    for index, row in df.iterrows():
        url = row['URL']
        original_marked = row['MARKED']        
        # print(f"Processing {index + 1}/{len(df)}: {url}")

        api_marked = call_highlight_api(url)

        original_count = count_marked_sentences(original_marked)
        api_count = count_marked_sentences(api_marked)
        
        results.append({
            'URL': url,
            'ORIGINAL_MARKED': original_marked,
            'API_MARKED': api_marked,
            'ORIGINAL_COUNT': original_count,
            'API_COUNT': api_count,
            'COUNT_DIFF': api_count - original_count
        })

        # print("-" * 50)
        # print(api_marked)

    # Save results to new CSV
    results_df = pd.DataFrame(results)
    results_df.to_excel(output_csv, index=False)
    print(f"Results saved to {output_csv}")
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print(f"Total URLs processed: {len(results_df)}")
    print(f"Average original marked sentences: {results_df['ORIGINAL_COUNT'].mean():.2f}")
    print(f"Average API marked sentences: {results_df['API_COUNT'].mean():.2f}")
    print(f"Average difference: {results_df['COUNT_DIFF'].mean():.2f}")

def purify_results(input_csv, output_csv):
    llm_purifier_for_results = LLM_Pufirier(model_name=model_name)
    data = []  # Use a regular list for appending

    with open(input_csv) as f:
        lines = f.readlines()
        for line in lines:
            if len(line.strip()) == 0:  # Better empty line check
                continue
            changed, similarity, isNeutral = llm_purifier_for_results.purify(line)
            
            data.append({
                "Original": line,
                "Changed": changed,
                "IsNeutral": isNeutral,
                "Cosine Similarity": similarity
            })

        # Convert to DataFrame at the end
    dataset = pd.DataFrame(data)
    dataset.to_excel(output_csv,index=False)


if __name__ == '__main__':
    #purify_results(input_csv="dataset/hate_speech_cleaned.txt", output_csv=f"results_purify/result_{model_name}.xlsx")
    #highlight_results(input_csv="dataset/highlight_data.csv", output_csv=f"results_highlight/highlight_result_{model_name}.xlsx")

    app.run(host="0.0.0.0", port=5000, debug=True)