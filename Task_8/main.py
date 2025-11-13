from records.feed_class import News, PrivateAd, MotivationalQuote
from utils.file_reader import FileRecordProvider
from utils.json_reader import JSONRecordProvider
from utils.analytics import generate_word_count, generate_letter_count


# === Конфигурация путей ===
NEWS_FEED_FILE = "news_feed.txt"
CSV_OUTPUT_FOLDER = "csv_output"
SOURCE_TXT_FILE = "source_file.txt"
SOURCE_JSON_FILE = "source_file.json"


def menu():
    print("\nSelect input method:")
    print("1 - Manual input")
    print("2 - Import from source_file.txt")
    print("3 - Import from source_file.json")
    return input("Enter choice (1/2/3): ").strip()


def manual_input():
    print("\nSelect record type:")
    print("1 - News")
    print("2 - Private Ad")
    print("3 - Motivational Quote")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        News(input("Enter news text: "), input("Enter city: ")).save(NEWS_FEED_FILE)
    elif choice == "2":
        PrivateAd(input("Enter ad text: "), input("Enter expiration date YYYY-MM-DD: ")).save(NEWS_FEED_FILE)
    elif choice == "3":
        MotivationalQuote(input("Enter quote: "), input("Enter author: ")).save(NEWS_FEED_FILE)
    else:
        print("Invalid choice.")


def import_from_txt():
    provider = FileRecordProvider(SOURCE_TXT_FILE)
    for record in provider.read_records():
        record.save(NEWS_FEED_FILE)


def import_from_json():
    provider = JSONRecordProvider(SOURCE_JSON_FILE)
    for record in provider.read_records():
        record.save(NEWS_FEED_FILE)


def run_analytics():
    generate_word_count(NEWS_FEED_FILE, CSV_OUTPUT_FOLDER)
    generate_letter_count(NEWS_FEED_FILE, CSV_OUTPUT_FOLDER)
    print("✅ CSV analytics generated!")


def run():
    choice = menu()
    if choice == "1":
        manual_input()
    elif choice == "2":
        import_from_txt()
    elif choice == "3":
        import_from_json()
    else:
        print("Invalid choice.")
        return

    run_analytics()


if __name__ == "__main__":
    run()

