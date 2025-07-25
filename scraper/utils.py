def save_content_to_file(path, title, extracted_text):
    with open(path, "w", encoding="utf-8") as file:
        if title is not None: file.write(title + "\n")
        for line in extracted_text:
            file.write(line + "\n")