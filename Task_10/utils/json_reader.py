import json
from records.feed_class import News, PrivateAd, MotivationalQuote


class JSONRecordProvider:
    def __init__(self, filename):
        self.filename = filename

    def read_records(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            op = item["operation_type"].lower()

            if op == "news":
                yield News(item["text"], item["city"])

            elif op == "private advertisement":
                yield PrivateAd(item["text"], item["expiration_date"])

            elif op == "motivational quote":
                yield MotivationalQuote(item["quote"], item["author"])
