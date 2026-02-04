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
    city1 = (f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{code.upper()}'")
    cursor = yhteys.cursor()
    cursor.execute(city1)
    coords = cursor.fetchone()
    return coords


def run_airport_distance(code1, code2):
    coords1 = get_airport_coordinates(code1)
    coords2 = get_airport_coordinates(code2)
    if not coords1:
        print(f"Airport with ICAO code {code1} not found in the database.")
    if not coords2:
        print(f"Airport with ICAO code {code2} not found in the database.")
    if coords1 and coords2:
        distance = geodesic(coords1, coords2).kilometers
        print(f"Distance between {code1} and {code2}: {distance:.2f}")


code1 = input("Enter the ICAO code of the first airport: ").upper()
code2 = input("Enter the ICAO code of the second airport: ").upper()
run_airport_distance(code1, code2)