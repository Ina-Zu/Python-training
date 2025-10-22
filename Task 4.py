import random
import string
import re

# ==============================
# TASK 2 — реализация с функциями
# ==============================

def generate_random_dicts(min_dicts=2, max_dicts=10, min_keys=2, max_keys=5):
    num_dicts = random.randint(min_dicts, max_dicts)
    return [
        {k: random.randint(0, 100) for k in random.sample(string.ascii_lowercase, random.randint(min_keys, max_keys))}
        for _ in range(num_dicts)
    ]

def merge_dicts(dicts):
    merged = {}
    for i, d in enumerate(dicts):
        for key, value in d.items():
            if key not in merged or value > merged[key][0]:
                merged[key] = (value, i + 1)
    return merged

def rename_keys(merged, dicts):
    result = {}
    for key, (value, idx) in merged.items():
        key_name = f"{key}_{idx}" if sum(key in d for d in dicts) > 1 else key
        result[key_name] = value
    return result

def main_module2():
    dicts = generate_random_dicts()
    print("=== TASK 2: Generated list of dicts ===")
    print(dicts)

    merged = merge_dicts(dicts)
    result = rename_keys(merged, dicts)

    print("\n=== TASK 2: Final merged dict ===")
    print(result)


# ==============================
# TASK 3 — реализация с функциями
# ==============================

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

    print("\n=== TASK 3: Final normalized text ===")
    print(final_text)
    print("\nNumber of whitespace characters:", whitespace_count)


# ==============================
# MAIN EXECUTION
# ==============================

if __name__ == "__main__":
    main_module2()
    main_module3()
