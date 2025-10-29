import re

def normalize_text(text):
    text = re.sub(r'(\b)iZ(\b)', r'\1is\2', text, flags=re.IGNORECASE)
    sentences = re.split(r'(?<=[.!?])', text)
    sentences = [s.strip().capitalize() for s in sentences if s.strip()]
    normalized_text = ' '.join(sentences)
    return normalized_text

def create_summary_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    last_words = []
    for s in sentences:
        words = re.findall(r'\b\w+\b(?=[.!?])', s)
        if words:
            last_words.append(words[-1])
    summary_sentence = ' '.join(last_words).capitalize() + '.'
    return summary_sentence

def count_whitespaces(text):
    return len(re.findall(r'\s', text))

def process_text(text):
    paragraphs = text.strip().split('\n\n')
    normalized_paragraphs = [normalize_text(p) for p in paragraphs]
    summary_sentence = create_summary_sentence(' '.join(normalized_paragraphs))

    if len(normalized_paragraphs) > 1:
        normalized_paragraphs[1] += ' ' + summary_sentence
    else:
        normalized_paragraphs[-1] += ' ' + summary_sentence

    final_text = '\n\n'.join(normalized_paragraphs)
    whitespace_count = count_whitespaces(final_text)

    print(final_text)
    print("\nNumber of whitespace characters:", whitespace_count)

text = """
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

process_text(text)
