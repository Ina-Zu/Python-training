import os
import csv
import string


def generate_word_count(input_file, output_folder):
    """Generate word frequency statistics and save as CSV."""
    os.makedirs(output_folder, exist_ok=True)

    word_count = {}

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            # Remove punctuation
            cleaned = "".join(char.lower() if char.isalnum() else " " for char in line)
            words = cleaned.split()

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    output_path = os.path.join(output_folder, "word_count.csv")

    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["word", "count"])

        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([word, count])


def generate_letter_count(input_file, output_folder):
    """Generate letter frequency statistics and save as CSV."""
    os.makedirs(output_folder, exist_ok=True)

    total_letters = 0
    letter_stats = {letter: {"count": 0, "uppercase": 0} for letter in string.ascii_lowercase}

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            for char in line:
                if char.lower() in letter_stats:
                    total_letters += 1
                    letter_stats[char.lower()]["count"] += 1

                    if char.isupper():
                        letter_stats[char.lower()]["uppercase"] += 1

    output_path = os.path.join(output_folder, "letter_count.csv")

    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])

        for letter, data in letter_stats.items():
            count = data["count"]
            upper = data["uppercase"]
            percent = round((count / total_letters) * 100, 2) if total_letters > 0 else 0

            writer.writerow([letter, count, upper, percent])
