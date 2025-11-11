import csv
import os
from collections import Counter

FEED = "news_feed.txt"
CSV_DIR = "csv_output"


def generate_word_count():
    if not os.path.exists(CSV_DIR):
        os.mkdir(CSV_DIR)

    with open(FEED, "r", encoding="utf-8") as f:
        words = f.read().lower().split()

    counts = Counter(words)

    with open(f"{CSV_DIR}/word_count.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, cnt in counts.items():
            writer.writerow([word, cnt])


def generate_letter_count():
    with open(FEED, "r", encoding="utf-8") as f:
        text = f.read()

    letters = [c for c in text if c.isalpha()]

    counts = Counter(letters)
    total = sum(counts.values())

    uppercase = sum(1 for c in letters if c.isupper())

    with open(f"{CSV_DIR}/letter_count.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])

        for letter, cnt_all in sorted(counts.items()):
            cnt_upper = sum(1 for c in text if c == letter.upper())
            pct = round((cnt_all / total) * 100, 2)
            writer.writerow([letter, cnt_all, cnt_upper, pct])
