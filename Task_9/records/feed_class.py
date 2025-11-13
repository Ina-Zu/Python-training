import datetime
import random
from utils.normalizer import normalize_text


class Record:
    def format_record(self):
        raise NotImplementedError()

    def save(self, output_file):
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(self.format_record())


class News(Record):
    def __init__(self, text, city):
        self.text = normalize_text(text)
        self.city = city
        self.date = datetime.date.today()

    def format_record(self):
        return f"--- News ---\n{self.text}\n{self.city}, {self.date}\n--------------------\n"


class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        self.text = normalize_text(text)
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        self.days_left = (self.expiration_date - datetime.date.today()).days

    def format_record(self):
        return f"--- Private Ad ---\n{self.text}\nExpires: {self.expiration_date}, {self.days_left} days left\n--------------------\n"


class MotivationalQuote(Record):
    def __init__(self, quote, author):
        self.quote = normalize_text(quote)
        self.author = author
        self.motivation_score = random.randint(1, 10)

    def format_record(self):
        return f"--- Motivational Quote ---\n\"{self.quote}\"\nAuthor: {self.author}\nMotivation score: {self.motivation_score}/10\n--------------------\n"
