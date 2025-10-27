import datetime
import random

OUTPUT_FILE = "news_feed.txt"


class Record:
    def format_record(self):
        raise NotImplementedError("Subclasses must implement this method")


class News(Record):
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = datetime.date.today()

    def format_record(self):
        return (f"--- News ---\n"
                f"Text: {self.text}\n"
                f"City: {self.city}\n"
                f"Date: {self.date}\n"
                f"--------------------\n")


class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        self.text = text
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
        self.quote = quote
        self.author = author
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


def main():
    print("Select record type:\n1 - News\n2 - Private Ad\n3 - Motivational Quote")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        text = input("Enter news text: ")
        city = input("Enter city: ")
        record = News(text, city)

    elif choice == "2":
        text = input("Enter ad text: ")
        expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
        record = PrivateAd(text, expiration_date)

    elif choice == "3":
        quote = input("Enter your quote: ")
        author = input("Enter author name: ")
        record = MotivationalQuote(quote, author)

    else:
        print("Invalid choice.")
        return

    save_record(record)
    print("✅ Record added successfully!")


if __name__ == "__main__":
    main()
