import csv
import string
import os


def generate_word_count(output_file, csv_folder):
    words = {}

    with open(output_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().lower()
            for word in line.split():
                word = word.strip(string.punctuation)
                if word:
                    words[word] = words.get(word, 0) + 1

    os.makedirs(csv_folder, exist_ok=True)

    with open(f"{csv_folder}/word_count.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])
        for word, count in sorted(words.items()):
            writer.writerow([word, count])


def generate_letter_count(output_file, csv_folder):
    letters = {}
    uppercase = 0
    total_chars = 0

    with open(output_file, "r", encoding="utf-8") as f:
        for line in f:
            for ch in line:
                if ch.isalpha():
                    total_chars += 1
                    letters[ch.lower()] = letters.get(ch.lower(), 0) + 1
                    if ch.isupper():
                        uppercase += 1

    os.makedirs(csv_folder, exist_ok=True)

    with open(f"{csv_folder}/letter_count.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])

        for letter, cnt in sorted(letters.items()):
            percent = round((cnt / total_chars) * 100, 2)
            writer.writerow([letter, cnt, uppercase, percent])


