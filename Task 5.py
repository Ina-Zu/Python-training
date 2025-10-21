import re

def normalize_text(text):
    text = re.sub(r'\biz\b', 'is', text, flags=re.IGNORECASE)
    return text.lower().capitalize()

def extract_last_words(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    last_words = [re.findall(r'\b\w+\b(?=[.!?])', s)[-1] for s in sentences if re.findall(r'\b\w+\b(?=[.!?])', s)]
    return ' '.join(last_words).capitalize() + '.'

def count_whitespaces(text):
    return len(re.findall(r'\s', text))

def add_summary_sentence(text):
    normalized = normalize_text(text)
    sentences = re.split(r'(?<=[.!?])\s+', normalized.strip())
    last_sentence = extract_last_words(normalized)
    # добавляем новое предложение в тот параграф, где оно должно быть (после второго)
    paragraphs = normalized.split('\n\n')
    if len(paragraphs) > 1:
        paragraphs[1] += " " + last_sentence
    return '\n\n'.join(paragraphs)

def main_module3():
    text = """
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
    final_text = add_summary_sentence(text)
    whitespace_count = count_whitespaces(final_text)

    print(final_text)
    print("\nNumber of whitespace characters:", whitespace_count)

if __name__ == "__main__":
    main_module3()
