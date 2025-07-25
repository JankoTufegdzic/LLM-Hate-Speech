from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd
from llm.llm_purifier import LLM_Pufirier
from llm.llm_highlighter import LLM_Highlighter
from scraper.scrape import perform_scrape
from scraper.extract import filter_general_text

app = Flask(__name__)

model_name="qwen3"
llm_purifier = LLM_Pufirier(model_name=model_name)
llm_highlighter=LLM_Highlighter(model_name=model_name)


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

@app.route('/highlight', methods=['GET', 'POST'])
def highlight():
    highlighted_text = ''
    url = ''
    if request.method == 'POST':
        url = request.form.get('url_input', '')
        try:
            # Minimal character and word count for each extracted paragraph (lenient filter).
            min_char_count = 20
            min_word_count = 5
            perform_scrape(url)
            text_list = filter_general_text(min_char_count, min_word_count)
            words = " ".join(text_list)
            
            highlighted_text=llm_highlighter.highlight(words)
            print(highlighted_text)
            #highlighted_text = ' '.join(words)
        except Exception as e:
            highlighted_text = f'<span class="text-danger">Error: {str(e)}</span>'
    return render_template('highlight.html', highlighted_text=highlighted_text, url=url)

if __name__ == '__main__':
    # data = []  # Use a regular list for appending

    # with open("dataset/hate_speech_cleaned.txt") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         if len(line.strip()) == 0:  # Better empty line check
    #             continue
    #         changed, similarity, isNeutral = llm_purifier.purify(line)
            
    #         data.append({
    #             "Original": line,
    #             "Changed": changed,
    #             "IsNeutral": isNeutral,
    #             "Cosine Similarity": similarity
    #         })

    #     # Convert to DataFrame at the end
    # dataset = pd.DataFrame(data)
    # dataset.to_excel(f"result_{llm_purifier.model_name}.xlsx",index=False)
    print(llm_highlighter.highlight("Ja živim u Turskoj. Svi turci su mnogo ružni. Ali su dobar narod."))
    
    # app.run(host="0.0.0.0", port=5000, debug=True)