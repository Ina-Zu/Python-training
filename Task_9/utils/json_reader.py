import json
import os
from records.feed_class import News, PrivateAd, MotivationalQuote


class JSONRecordProvider:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_records(self):
        if not os.path.exists(self.filepath):
            print(f"❌ JSON file {self.filepath} not found!")
            return []

        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Поддержка: одного объекта или списка
        records = data if isinstance(data, list) else [data]
        result = []

        for item in records:
            op = item.get("operation_type", "").lower()
            if op == "news":
                result.append(News(item["text"], item["city"]))
            elif op == "private advertisement":
                result.append(PrivateAd(item["text"], item["expiration_date"]))
            elif op == "motivational quote":
                result.append(MotivationalQuote(item["quote"], item["author"]))
            else:
                print(f"⚠ Unknown operation type: {op}")

        os.remove(self.filepath)
        print(f"✅ {self.filepath} processed and removed!")
        return result