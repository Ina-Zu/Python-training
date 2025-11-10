from feed_class.news_feed_parent import NewsFeed
from feed_class.news import News
from feed_class.private_ad import PrivateAd
from feed_class.motivational_quote import MotivationalQuote
from utils.text_parser import SourceParser


class AppRunner:

    def console_runner(self):
        while True:
            print("\nSelect the way you want add data:")
            print("1. Console mode")
            print("2. Load from txt")
            print("3. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.console_mode()

            elif choice == "2":
                records = SourceParser().parse_source_file()
                for r in records:
                    NewsFeed().save_record(r)

            elif choice == "3":
                print("Bye!")
                break

            else:
                print("Invalid option!")

    def console_mode(self):
        print("\nSelect type of record to add:")
        print("1. News")
        print("2. Private Advertisement")
        print("3. Motivational Quote")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            text = input("Enter text: ")
            city = input("Enter city: ")
            NewsFeed().save_record(News(text, city))

        elif choice == "2":
            text = input("Enter text: ")
            expiration = input("Enter expiration date (YYYY-MM-DD): ")
            NewsFeed().save_record(PrivateAd(text, expiration))

        elif choice == "3":
            quote = input("Enter quote: ")
            author = input("Enter author name: ")
            NewsFeed().save_record(MotivationalQuote(quote, author))

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    AppRunner().console_runner()
