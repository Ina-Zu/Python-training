import sqlite3
import os


class Database:
    def __init__(self):
        os.makedirs("db", exist_ok=True)
        self.db_path = "db/news.db"
        self._create_tables()

    def _create_tables(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT UNIQUE,
                city TEXT,
                date TEXT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS ads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT UNIQUE,
                expiration_date TEXT,
                days_left INTEGER
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote TEXT UNIQUE,
                author TEXT,
                motivation_score INTEGER
            )
        """)

        conn.commit()
        conn.close()

    # Save methods with duplicate protection

    def save_news(self, text, city, date):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO news (text, city, date) VALUES (?, ?, ?)",
                    (text, city, date))
        conn.commit()
        conn.close()

    def save_ad(self, text, expiration_date, days_left):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO ads (text, expiration_date, days_left) VALUES (?, ?, ?)",
                    (text, expiration_date, days_left))
        conn.commit()
        conn.close()

    def save_quote(self, quote, author, motivation_score):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO quotes (quote, author, motivation_score) VALUES (?, ?, ?)",
                    (quote, author, motivation_score))
        conn.commit()
        conn.close()

    # Universal dispatcher
    def save_record(self, record):
        if record.__class__.__name__ == "News":
            self.save_news(record.text, record.city, str(record.date))

        elif record.__class__.__name__ == "PrivateAd":
            self.save_ad(record.text, str(record.expiration_date), record.days_left)

        elif record.__class__.__name__ == "MotivationalQuote":
            self.save_quote(record.quote, record.author, record.motivation_score)

        else:
            raise ValueError("Unknown record type")
