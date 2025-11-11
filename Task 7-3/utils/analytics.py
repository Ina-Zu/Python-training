import csv
import string

OUTPUT_FILE = "news_feed.txt"
CSV_FOLDER = "csv_output"


def generate_word_count():
    words = {}

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().lower()
            for word in line.split():
                # убрать пунктуацию
                word = word.strip(string.punctuation)
                if word:
                    words[word] = words.get(word, 0) + 1

    # создаём папку если нет
    import os
    os.makedirs(CSV_FOLDER, exist_ok=True)

    with open(f"{CSV_FOLDER}/word_count.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])
        for word, count in sorted(words.items()):
            writer.writerow([word, count])


def generate_letter_count():
    letters = {}
    uppercase = 0
    total_chars = 0

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            for ch in line:
                if ch.isalpha():
                    total_chars += 1
                    letters[ch.lower()] = letters.get(ch.lower(), 0) + 1
                    if ch.isupper():
                        uppercase += 1

    import os
    os.makedirs(CSV_FOLDER, exist_ok=True)

    with open(f"{CSV_FOLDER}/letter_count.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])

        for letter, cnt in sorted(letters.items()):
            percent = round((cnt / total_chars) * 100, 2)
            writer.writerow([letter, cnt, uppercase, percent])

