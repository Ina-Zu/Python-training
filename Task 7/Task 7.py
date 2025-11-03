import datetime
import random
import json
import os

OUTPUT_FILE = "../news_feed.txt"


class Record:
    def format_record(self):
        raise NotImplementedError("Subclasses must implement this method")


class News(Record):
    def __init__(self, text, city):
        self.text = normalize_text(text)
        self.city = normalize_text(city)
        self.date = datetime.date.today()

    def format_record(self):
        return (f"--- News ---\n"
                f"Text: {self.text}\n"
                f"City: {self.city}\n"
                f"Date: {self.date}\n"
                f"--------------------\n")


class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        self.text = normalize_text(text)
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        self.days_left = (self.expiration_date - datetime.date.today()).days

    def format_record(self):
        return (f"--- Private Ad ---\n"
                f"Text: {self.text}\n"
                f"Expiration date: {self.expiration_date}\n"
                f"Days left: {self.days_left}\n"
                f"--------------------\n")


class MotivationalQuote(Record):
    def __init__(self, quote, author):
        self.quote = normalize_text(quote)
        self.author = normalize_text(author)
        self.motivation_score = random.randint(1, 10)

    def format_record(self):
        return (f"--- Motivational Quote ---\n"
                f"\"{self.quote}\"\n"
                f"Author: {self.author}\n"
                f"Motivation score: {self.motivation_score}/10\n"
                f"--------------------\n")


def save_record(record):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write(record.format_record())


def normalize_text(text: str) -> str:
    """Sentence case + remove extra spaces."""
    text = " ".join(text.split())
    return text.capitalize()


def process_txt_file(fname):
    with open(fname, encoding="utf-8") as f:
        for line in f:
            parts = [p.strip() for p in line.split("|")]
            if not parts or len(parts) < 2:
                continue

            rtype = parts[0].lower()

            if rtype == "news":
                save_record(News(parts[1], parts[2]))
            elif rtype == "ad":
                save_record(PrivateAd(parts[1], parts[2]))
            elif rtype == "quote":
                save_record(MotivationalQuote(parts[1], parts[2]))
    open(fname, "w").close()


def process_json_file(fname):
    with open(fname, encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        rtype = item["type"].lower()
        if rtype == "news":
            save_record(News(item["text"], item["city"]))
        elif rtype == "ad":
            save_record(PrivateAd(item["text"], item["expiration"]))
        elif rtype == "quote":
            save_record(MotivationalQuote(item["quote"], item["author"]))

    open(fname, "w").close()


def main():
    print("Select input source:\n1 - Keyboard\n2 - TXT file\n3 - JSON file")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        print("Select record type:\n1 - News\n2 - Private Ad\n3 - Motivational Quote")
        c = input("Enter choice (1/2/3): ").strip()

        if c == "1":
            text = input("Enter news text: ")
            city = input("Enter city: ")
            save_record(News(text, city))

        elif c == "2":
            text = input("Enter ad text: ")
            exp = input("Enter expiration (YYYY-MM-DD): ")
            save_record(PrivateAd(text, exp))

        elif c == "3":
            quote = input("Enter quote: ")
            author = input("Enter author: ")
            save_record(MotivationalQuote(quote, author))

    elif choice == "2":
        fname = input("Enter TXT filename: ")
        process_txt_file(fname)

    elif choice == "3":
        fname = input("Enter JSON filename: ")
        process_json_file(fname)

    print("✅ Records added successfully!")


if __name__ == "__main__":
    main()
