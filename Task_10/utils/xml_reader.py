import xml.etree.ElementTree as ET
from records.feed_class import News, PrivateAd, MotivationalQuote


class XMLRecordProvider:
    def __init__(self, filename):
        self.filename = filename

    def read_records(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()

        for item in root:
            op = item.find("operation_type").text.lower()

            if op == "news":
                yield News(item.find("text").text, item.find("city").text)

            elif op == "private advertisement":
                yield PrivateAd(item.find("text").text, item.find("expiration_date").text)

            elif op == "motivational quote":
                yield MotivationalQuote(item.find("quote").text, item.find("author").text)
