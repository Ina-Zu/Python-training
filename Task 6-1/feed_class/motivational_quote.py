import random
from utils.normalize import normalize_text


class MotivationalQuote:

    def __init__(self, quote, author):
        self.quote = normalize_text(quote)
        self.author = author
        self.motivation_score = random.randint(1, 10)

    def format_record(self):
        return (f"--- Motivational Quote ---\n"
                f"\"{self.quote}\"\n"
                f"Author: {self.author}\n"
                f"Motivation score: {self.motivation_score}/10\n"
                f"--------------------\n")
