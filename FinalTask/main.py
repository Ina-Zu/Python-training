from utils.database import CityDatabase
from utils.distance import haversine


def ask_coordinates(city):
    """Ask user for coordinates input."""
    print(f"\nCoordinates for '{city}' not found. Please enter them.")

    while True:
        try:
            lat = float(input("Enter latitude: "))
            lon = float(input("Enter longitude: "))
            return lat, lon
        except ValueError:
            print("Invalid number. Try again.")


def main():
    db = CityDatabase()

    print("=== City Distance Calculator ===")

    while True:
        city1 = input("\nEnter first city name (or 'exit'): ").strip()
        if city1.lower() == "exit":
            break

        city2 = input("Enter second city name: ").strip()

        # --- load or ask for city1 ---
        coords1 = db.get_city(city1)
        if coords1 is None:
            lat, lon = ask_coordinates(city1)
            db.save_city(city1, lat, lon)
            coords1 = (lat, lon)

        # --- load or ask for city2 ---
        coords2 = db.get_city(city2)
        if coords2 is None:
            lat, lon = ask_coordinates(city2)
            db.save_city(city2, lat, lon)
            coords2 = (lat, lon)

        # --- calculate distance ---
        dist = haversine(coords1[0], coords1[1], coords2[0], coords2[1])
        print(f"\nDistance between {city1} and {city2}: {dist:.2f} km")


if __name__ == "__main__":
    main()
