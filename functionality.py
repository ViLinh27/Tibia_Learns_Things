def read_markdown_file(markdown_file_path):
    with open(markdown_file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content