import os
from records.feed_class import News, PrivateAd, MotivationalQuote
from utils.file_reader import FileRecordProvider
from utils.json_reader import JSONRecordProvider
from utils.xml_reader import XMLRecordProvider
from utils.analytics import generate_word_count, generate_letter_count
from utils.database import Database


NEWS_FEED_FILE = "news_feed.txt"
CSV_OUTPUT_FOLDER = "csv_output"
SOURCE_TXT_FILE = "source_file.txt"
SOURCE_JSON_FILE = "source_file.json"
SOURCE_XML_FILE = "source_file.xml"


def menu():
    print("\nSelect input method:")
    print("1 - Manual input")
    print("2 - Import from TXT")
    print("3 - Import from JSON")
    print("4 - Import from XML")
    print("5 - Exit")
    return input("Enter choice (1-5): ").strip()


def manual_input(db):
    print("\nSelect record type:")
    print("1 - News")
    print("2 - Private Ad")
    print("3 - Motivational Quote")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        record = News(input("Enter news text: "), input("Enter city: "))
    elif choice == "2":
        record = PrivateAd(input("Enter ad text: "), input("Expiration date YYYY-MM-DD: "))
    elif choice == "3":
        record = MotivationalQuote(input("Quote: "), input("Author: "))
    else:
        print("Invalid choice.")
        return

    record.save(NEWS_FEED_FILE)
    db.save_record(record)
    print("✔ Saved to file and database.")


def import_from_provider(provider, db):
    for rec in provider.read_records():
        rec.save(NEWS_FEED_FILE)
        db.save_record(rec)


def run_analytics():
    generate_word_count(NEWS_FEED_FILE, CSV_OUTPUT_FOLDER)
    generate_letter_count(NEWS_FEED_FILE, CSV_OUTPUT_FOLDER)


def run():
    os.makedirs(CSV_OUTPUT_FOLDER, exist_ok=True)
    db = Database()

    while True:
        choice = menu()

        if choice == "1":
            manual_input(db)

        elif choice == "2":
            import_from_provider(FileRecordProvider(SOURCE_TXT_FILE), db)
            print("✔ TXT import completed.")

        elif choice == "3":
            import_from_provider(JSONRecordProvider(SOURCE_JSON_FILE), db)
            print("✔ JSON import completed.")

        elif choice == "4":
            import_from_provider(XMLRecordProvider(SOURCE_XML_FILE), db)
            print("✔ XML import completed.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
            continue

        run_analytics()


if __name__ == "__main__":
    run()
