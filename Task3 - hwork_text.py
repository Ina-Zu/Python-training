import re

def normalize_text(text):
    text = re.sub(r'(\b)iZ(\b)', r'\1is\2', text, flags=re.IGNORECASE)
    text = text.lower().capitalize()
    return text

def create_summary_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    last_words = [re.findall(r'\b\w+\b(?=[.!?])', s)[-1] for s in sentences if re.findall(r'\b\w+\b(?=[.!?])', s)]
    summary_sentence = ' '.join(last_words).capitalize() + '.'
    return summary_sentence

def count_whitespaces(text):
    return len(re.findall(r'\s', text))

def process_text(text):
    normalized = normalize_text(text)
    summary_sentence = create_summary_sentence(normalized)
    final_text = normalized + " " + summary_sentence
    whitespace_count = count_whitespaces(final_text)
    print(final_text)
    print("Number of whitespace characters:", whitespace_count)

text = """
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

process_text(text)

