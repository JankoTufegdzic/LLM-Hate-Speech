# LLM-Hate-Speech

This repository is created for research published at the International Electrotechnical and Computer Science Conference (ERK 2025), later included in IEEE Xplore.

DOI references:
```
DOI1
DOI1
```

This repository is for research on LLM-powered hate speech detection, purification, and highlighting in text data. It provides tools for scraping, processing, and evaluating hate speech using large language models.


## Repo Structure

```bash
LLM-Hate-Speech/
├─ app.py                  # Main Flask application
├─ dataset/                # Hate speech datasets and highlight data
│   ├─ hate_speech.txt
│   ├─ hate_speech_cleaned.txt
│   └─ highlight_data.csv
├─ llm/                    # LLM wrappers and helpers
│   ├─ helper.py
│   ├─ llm_highlighter.py
│   └─ llm_purifier.py
├─ scraper/                # News scraper modules
│   ├─ alo.py, kurir.py, telegraf.py, ...
│   └─ utils.py
├─ results_highlight/      # Highlighting results (Excel, summary)
├─ results_purify/         # Purification results (Excel)
├─ templates/              # HTML templates for Flask app
├─ requirements.txt        # Default dependencies
└─ README.md
```

## Quickstart

### Environment

Create a virtual environment and install dependencies:
```bash
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```

### Run the Application
```bash
python app.py
```

### Configuration
You can set model or other options via environment variables or a `.env` file at the repo root. Example:
```
MODEL=mistral
```

## Citation
If you use this codebase or ideas from the accompanying write-up, please cite appropriately:
```
<Add citation details here>
```

## License
This project is licensed under the GNU General Public License v3.0.
