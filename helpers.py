def get_word_separator(language: str):
    """Some languages doesn't have spaces between words."""
    separators = {"ja_jp": "", "zh_tw": ""}
    if language in separators:
        return separators[language]
    else:
        return " "
