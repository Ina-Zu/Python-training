from records.feed_class import News, PrivateAd, MotivationalQuote
from utils.file_reader import FileRecordProvider
from utils.analytics import generate_word_count, generate_letter_count

# === CONFIGURATION ===
NEWS_FEED_FILE = "news_feed.txt"
CSV_OUTPUT_FOLDER = "csv_output"
SOURCE_FILE = "source_file.txt"


def menu():
    print("\nSelect input method:")
    print("1 - Manual input")
    print("2 - Import from source_file.txt")
    return input("Enter choice (1/2): ").strip()


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


def import_from_file():
    provider = FileRecordProvider(SOURCE_FILE)
    for rec in provider.read_records():
        rec.save(NEWS_FEED_FILE)


def run_analytics():
    generate_word_count(NEWS_FEED_FILE, CSV_OUTPUT_FOLDER)
    generate_letter_count(NEWS_FEED_FILE, CSV_OUTPUT_FOLDER)
    print("✅ CSV analytics regenerated!")


def run():
    choice = menu()
    if choice == "1":
        manual_input()
    elif choice == "2":
        import_from_file()
    else:
        print("Invalid choice.")
    run_analytics()


if __name__ == "__main__":
    run()
