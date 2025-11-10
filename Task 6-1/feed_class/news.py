import datetime
from utils.normalize import normalize_text
from feed_class.news_feed_parent import NewsFeed


class News:

    def __init__(self, text, city):
        self.text = normalize_text(text)
        self.city = city
        self.date = datetime.date.today()

    def format_record(self):
        return (f"--- News ---\n"
                f"Text: {self.text}\n"
                f"City: {self.city}\n"
                f"Date: {self.date}\n"
                f"--------------------\n")
