import os
import xml.etree.ElementTree as ET
from records.feed_class import News, PrivateAd, MotivationalQuote


class XMLRecordProvider:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_records(self):
        if not os.path.exists(self.filepath):
            print(f"❌ {self.filepath} not found!")
            return []

        tree = ET.parse(self.filepath)
        root = tree.getroot()
        records = []

        for item in root.findall("record"):
            op = item.find("operation_type").text.lower()

            if op == "news":
                records.append(News(item.find("text").text, item.find("city").text))
            elif op == "private advertisement":
                records.append(PrivateAd(item.find("text").text, item.find("expiration_date").text))
            elif op == "motivational quote":
                records.append(MotivationalQuote(item.find("quote").text, item.find("author").text))

        os.remove(self.filepath)
        print(f"✅ {self.filepath} processed and removed!")
        return records
