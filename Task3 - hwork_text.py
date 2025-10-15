import re

text = """
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

text = re.sub(r'\biZ\b', 'is', text)
text = text.lower().capitalize()

sentences = re.split(r'(?<=[.!?])\s+', text.strip())
last_words = [re.findall(r'\b\w+\b(?=[.!?])', s)[-1] for s in sentences if re.findall(r'\b\w+\b(?=[.!?])', s)]
summary_sentence = ' '.join(last_words).capitalize() + '.'
text = ' '.join(sentences) + ' ' + summary_sentence

whitespace_count = len(re.findall(r'\s', text))

print(text)
print("Number of whitespace characters:", whitespace_count)
