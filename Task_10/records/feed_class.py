import datetime
import random


class Record:
    def format(self):
        raise NotImplementedError("Subclass must implement format()")


class News(Record):
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = datetime.date.today()

    def format(self):
        return f"--- News ---\n{self.text}\n{self.city}, {self.date}\n\n"

    def save(self, filename):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.format())


class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        self.days_left = (self.expiration_date - datetime.date.today()).days

    def format(self):
        return f"--- Private Ad ---\n{self.text}\nExpires: {self.expiration_date}, {self.days_left} days left\n\n"

    def save(self, filename):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.format())


class MotivationalQuote(Record):
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author
        self.motivation_score = random.randint(1, 10)

    def format(self):
        return f"--- Quote ---\n\"{self.quote}\"\n— {self.author} ({self.motivation_score}/10)\n\n"

    def save(self, filename):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.format())
