OUTPUT_FILE = "output/news_feed.txt"


class NewsFeed:

    def save_record(self, record):
        with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
            file.write(record.format_record())
        print("✅ Record added!")
