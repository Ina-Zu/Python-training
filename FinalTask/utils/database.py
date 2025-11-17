import sqlite3
import os


class CityDatabase:
    def __init__(self):
        os.makedirs("db", exist_ok=True)
        self.db_path = "db/cities.db"
        self._create_table()

    def _create_table(self):
        """Create database table for storing city coordinates."""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS cities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                latitude REAL,
                longitude REAL
            )
        """)

        conn.commit()
        conn.close()

    def get_city(self, name):
        """Return coordinates for a city or None if not found."""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("SELECT latitude, longitude FROM cities WHERE name = ?", (name.lower(),))
        result = cur.fetchone()

        conn.close()
        return result

    def save_city(self, name, lat, lon):
        """Save city coordinates to the database."""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute(
            "INSERT OR IGNORE INTO cities (name, latitude, longitude) VALUES (?, ?, ?)",
            (name.lower(), lat, lon),
        )

        conn.commit()
        conn.close()
