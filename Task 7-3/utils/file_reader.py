import datetime
import os
from records.feed_class import News, PrivateAd, MotivationalQuote


class FileRecordProvider:
    def __init__(self, filepath):
        self.filepath = filepath

    def parse_block(self, block):
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        data = {}
        for line in lines:
            key, value = line.split(":")
            data[key.strip()] = value.strip()

        op = data["operation_type"].lower()

        if op == "news":
            return News(data["text"], data["city"])
        elif op == "private advertisement":
            return PrivateAd(data["text"], data["expiration_date"])
        elif op == "motivational quote":
            return MotivationalQuote(data["quote"], data["author"])

    def read_records(self):
        if not os.path.exists(self.filepath):
            print("❌ source_file.txt not found!")
            return []

        with open(self.filepath, "r", encoding="utf-8") as f:
            blocks = f.read().split("/")

        records = []
        for block in blocks:
            block = block.strip()
            if block:
                records.append(self.parse_block(block))

        os.remove(self.filepath)
        print("✅ source_file.txt processed and removed!")
        return records
