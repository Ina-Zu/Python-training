import os
from records.feed_class import News, PrivateAd, MotivationalQuote


class FileRecordProvider:
    def __init__(self, filepath):
        self.filepath = filepath

    def parse_block(self, block):
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        data = {}
        for line in lines:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().rstrip(";")

        op = data.get("operation_type", "").lower()

        if op == "news":
            return News(data["text"], data["city"])
        elif op == "private advertisement":
            return PrivateAd(data["text"], data["expiration_date"])
        elif op == "motivational quote":
            return MotivationalQuote(data["quote"], data["author"])
        else:
            print(f"⚠ Unknown operation type: {op}")

    def read_records(self):
        if not os.path.exists(self.filepath):
            print(f"❌ File {self.filepath} not found!")
            return []

        with open(self.filepath, "r", encoding="utf-8") as f:
            blocks = f.read().split("/")

        records = [self.parse_block(b) for b in blocks if b.strip()]
        os.remove(self.filepath)
        print(f"✅ {self.filepath} processed and removed!")
        return [r for r in records if r]
