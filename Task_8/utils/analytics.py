import csv
import string
import os


def generate_word_count(output_file, csv_folder):
    words = {}

    with open(output_file, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.strip().lower().split():
                word = word.strip(string.punctuation)
                if word:
                    words[word] = words.get(word, 0) + 1

    os.makedirs(csv_folder, exist_ok=True)

    with open(os.path.join(csv_folder, "word_count.csv"), "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])
        for word, count in sorted(words.items()):
            writer.writerow([word, count])


def generate_letter_count(output_file, csv_folder):
    letters = {}
    total_chars = 0
    uppercase = 0

    with open(output_file, "r", encoding="utf-8") as f:
        for line in f:
            for ch in line:
                if ch.isalpha():
                    total_chars += 1
                    letters[ch.lower()] = letters.get(ch.lower(), 0) + 1
                    if ch.isupper():
                        uppercase += 1

    os.makedirs(csv_folder, exist_ok=True)

    with open(os.path.join(csv_folder, "letter_count.csv"), "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])

        for letter, count in sorted(letters.items()):
            percent = round((count / total_chars) * 100, 2)
            writer.writerow([letter, count, uppercase, percent])
