import re


def normalize_text(text):
    text = re.sub(r'\biz\b', 'is', text, flags=re.IGNORECASE)
    return text.lower().capitalize()
