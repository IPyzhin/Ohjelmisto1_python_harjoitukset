import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='boris',
    password='Bubalar60',
    autocommit=True
)


def get_airport_coordinates(code):
    cursor = yhteys.cursor()
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (code.upper(),))
    coords = cursor.fetchone()
    return coords


def run_airport_distance():
    code1 = input("Enter the ICAO code of the first airport: ").upper()
    code2 = input("Enter the ICAO code of the second airport: ").upper()
    coords1 = get_airport_coordinates(code1)
    coords2 = get_airport_coordinates(code2)

    if coords1 is None:
        print(f"Airport with ICAO code {code1} not found in the database.")
        return
    if coords2 is None:
        print(f"Airport with ICAO code {code2} not found in the database.")
        return

    distance = geodesic(coords1, coords2).kilometers
    print(f"\n\nDistance between {code1} and {code2}: {distance:.2f} kilometers")


run_airport_distance()