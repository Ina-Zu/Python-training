import os
from feed_class.news import News
from feed_class.private_ad import PrivateAd
from feed_class.motivational_quote import MotivationalQuote

SOURCE_FILE = "source_file.txt"


class SourceParser:

    def parse_source_file(self):
        if not os.path.exists(SOURCE_FILE):
            print("❌ source_file.txt not found.")
            return []

        result = []
        block = {}

        with open(SOURCE_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "/":
                    record = self._convert_block(block)
                    if record:
                        result.append(record)
                    block = {}
                    continue

                if ":" in line:
                    key, value = line.split(":", 1)
                    block[key.strip()] = value.strip().rstrip(";")

        os.remove(SOURCE_FILE)
        print("✅ Source file processed and removed.")
        return result

    def _convert_block(self, block):
        op = block.get("operation_type", "").lower()

        if op == "news":
            return News(block["text"], block["city"])

        elif op == "private advertisement":
            return PrivateAd(block["text"], block["expiration_date"])

        elif op == "motivational quote":
            return MotivationalQuote(block["quote"], block["author"])

        print(f"⚠ Unknown operation type: {op}")
        return None
