import datetime
import random
import os
import re

OUTPUT_FILE = "../news_feed.txt"
DEFAULT_INPUT_FOLDER = "input_files"


# ================= NORMALIZATION (HW3/HW4) =================

def normalize_text(text):
    """
    Normalize case and replace incorrect 'iz' with 'is'.
    """
    text = re.sub(r'\biz\b', 'is', text, flags=re.IGNORECASE)
    return text.lower().capitalize()


# ================= BASE RECORD CLASS =================

class Record:
    """
    Base record class providing unified formatting behavior.
    """

    def format_body(self):
        """
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclass must implement this method.")

    def format_record(self):
        """
        Generates fully formatted text block for file output.
        """
        return f"--- {self.__class__.__name__} ---\n{self.format_body()}--------------------\n"


# ================= CONCRETE RECORD TYPES =================

class News(Record):
    """
    News record containing text, city, and publication date.
    """

    def __init__(self, text, city):
        self.text = normalize_text(text)
        self.city = city
        self.date = datetime.date.today()

    def format_body(self):
        return f"Text: {self.text}\nCity: {self.city}\nDate: {self.date}\n"


class PrivateAd(Record):
    """
    Private ad record with expiration date and remaining days.
    """

    def __init__(self, text, expiration_date):
        self.text = normalize_text(text)
        self.expiration_date = expiration_date
        self.days_left = (self.expiration_date - datetime.date.today()).days

    def format_body(self):
        return (
            f"Text: {self.text}\n"
            f"Expiration date: {self.expiration_date}\n"
            f"Days left: {self.days_left}\n"
        )


class MotivationalQuote(Record):
    """
    Motivational quote record containing score.
    """

    def __init__(self, quote, author):
        self.quote = normalize_text(quote)
        self.author = author
        self.motivation_score = random.randint(1, 10)

    def format_body(self):
        return (
            f"\"{self.quote}\"\n"
            f"Author: {self.author}\n"
            f"Motivation score: {self.motivation_score}/10\n"
        )


# ================= FILE PROVIDER =================

class FileRecordProvider:
    """
    Reads record lines from a text file and converts them to objects.
    Format examples per line:

    NEWS|text|city
    AD|text|YYYY-MM-DD
    QUOTE|quote|author
    """

    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = os.path.join(DEFAULT_INPUT_FOLDER, "input.txt")

    def parse_line(self, line):
        parts = line.strip().split("|")
        record_type = parts[0].upper()

        if record_type == "NEWS":
            return News(parts[1], parts[2])

        elif record_type == "AD":
            expiration = datetime.datetime.strptime(parts[2], "%Y-%m-%d").date()
            return PrivateAd(parts[1], expiration)

        elif record_type == "QUOTE":
            return MotivationalQuote(parts[1], parts[2])

        return None

    def read_records(self):
        if not os.path.exists(self.filepath):
            print("❌ File not found.")
            return []

        records = []
        with open(self.filepath, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    record = self.parse_line(line)
                    if record:
                        records.append(record)

        os.remove(self.filepath)
        print(f"✅ File processed and removed: {self.filepath}")

        return records


# ================= SAVE FEED =================

def save_record(record):
    """
    Append formatted record to main news feed file.
    """
    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write(record.format_record())


# ================= RUNNER =================

class Runner:
    """
    Handles program workflow and user interaction.
    """

    def get_valid_expiration_date(self):
        """
        Forces input of a date >= today.
        """
        while True:
            date_str = input("Enter expiration date (YYYY-MM-DD): ")
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if date >= datetime.date.today():
                    return date
                print("❌ Date must not be in the past.")
            except ValueError:
                print("❌ Invalid format.")

    def menu(self):
        print("\nSelect input method:")
        print("1 - Manual input")
        print("2 - Load from file")
        return input("Enter choice (1/2): ").strip()

    def manual(self):
        print("\nSelect record type:")
        print("1 - News")
        print("2 - Private Ad")
        print("3 - Motivational Quote")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            text = input("Enter news text: ")
            city = input("Enter city: ")
            save_record(News(text, city))

        elif choice == "2":
            text = input("Enter ad text: ")
            expiration = self.get_valid_expiration_date()
            save_record(PrivateAd(text, expiration))

        elif choice == "3":
            quote = input("Enter quote: ")
            author = input("Enter author: ")
            save_record(MotivationalQuote(quote, author))

        else:
            print("Invalid choice.")

    def from_file(self):
        path = input("Enter file path (or press Enter for default): ").strip()
        provider = FileRecordProvider(path if path else None)

        for rec in provider.read_records():
            save_record(rec)

    def run(self):
        choice = self.menu()

        if choice == "1":
            self.manual()
        elif choice == "2":
            self.from_file()
        else:
            print("Invalid choice.")


# ================= ENTRY POINT =================

if __name__ == "__main__":
    Runner().run()
