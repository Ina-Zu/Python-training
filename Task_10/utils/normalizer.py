# utils/normalizer.py
import re

def normalize_text(text: str) -> str:
    """
    Normalize input text:
      - replace standalone 'iz' (any case) with 'is'
      - collapse multiple spaces/newlines into single spaces
      - trim leading/trailing whitespace
      - capitalize sentences (simple split by period)
    Returns normalized string.
    """
    if text is None:
        return ""

    # Replace standalone "iz" with "is" (word boundaries, case-insensitive)
    text = re.sub(r'\biz\b', 'is', text, flags=re.IGNORECASE)

    # Collapse whitespace (spaces, tabs, newlines) into single spaces
    text = " ".join(text.split())

    # Split by sentence terminators
    sentences = re.split(r'(?<=[.!?])\s+', text)

    normalized_sentences = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue

        # Lowercase whole sentence, then capitalize only the first letter
        s = s.lower()
        s = s[0].upper() + s[1:] if len(s) > 0 else s

        normalized_sentences.append(s)

    if not normalized_sentences:
        return text.capitalize()

    # Join with spaces
    return " ".join(normalized_sentences)
