from records.feed_class import News, PrivateAd, MotivationalQuote


class FileRecordProvider:
    def __init__(self, filename):
        self.filename = filename

    def read_records(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            blocks = f.read().split("/")

        for block in blocks:
            block = block.strip()
            if not block:
                continue

            lines = block.split("\n")
            data = {}

            for line in lines:
                if ":" in line:
                    key, value = line.split(":", 1)
                    data[key.strip()] = value.strip()

            op = data.get("operation_type", "").lower()

            if op == "news":
                yield News(data["text"], data["city"])

            elif op == "private advertisement":
                yield PrivateAd(data["text"], data["expiration_date"])

            elif op == "motivational quote":
                yield MotivationalQuote(data["quote"], data["author"])

