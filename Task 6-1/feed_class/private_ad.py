import datetime
from utils.normalize import normalize_text


class PrivateAd:

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
