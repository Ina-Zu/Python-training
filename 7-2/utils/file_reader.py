import os
import datetime
from records.feed_class import News, PrivateAd, MotivationalQuote


class FileRecordProvider:
    def __init__(self, filepath="source_file.txt"):
        self.filepath = filepath

    def parse_line(self, line):
        parts = line.strip().split("|")
        if not parts:
            return None

        rtype = parts[0].upper()

        if rtype == "NEWS":
            return News(parts[1], parts[2])

        elif rtype == "AD":
            return PrivateAd(parts[1], parts[2])

        elif rtype == "QUOTE":
            return MotivationalQuote(parts[1], parts[2])

        return None

    def read_records(self):
        if not os.path.exists(self.filepath):
            print("❌ No source_file.txt found.")
            return []

        records = []
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                if record := self.parse_line(line):
                    records.append(record)

        os.remove(self.filepath)
        print("✅ source_file.txt processed and removed!")
        return records
