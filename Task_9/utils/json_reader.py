import json
import os
from records.feed_class import News, PrivateAd, MotivationalQuote


class JSONRecordProvider:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_records(self):
        if not os.path.exists(self.filepath):
            print(f"❌ {self.filepath} not found!")
            return []

        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        records = []
        for item in data["records"]:
            op = item["operation_type"].lower()
            if op == "news":
                records.append(News(item["text"], item["city"]))
            elif op == "private advertisement":
                records.append(PrivateAd(item["text"], item["expiration_date"]))
            elif op == "motivational quote":
                records.append(MotivationalQuote(item["quote"], item["author"]))

        os.remove(self.filepath)
        print(f"✅ {self.filepath} processed and removed!")
        return records
