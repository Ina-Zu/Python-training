import re

def normalize_text(text: str) -> str:
    text = re.sub(r'\biz\b', 'is', text, flags=re.IGNORECASE)
    return ". ".join([s.strip().capitalize() for s in text.split(".")])
