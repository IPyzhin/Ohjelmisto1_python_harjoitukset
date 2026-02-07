import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):
    conn = mysql.connector.connect(
        host='127.0.0.1', port=3306, database='flight_game',
        user='boris', password='Bubalar60', autocommit=True
    )
    cursor = conn.cursor()
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code.upper(),))
    coords = cursor.fetchone()
    cursor.close()
    conn.close()
    return coords


def run_airport_distance(code1, code2):
    coords1, coords2 = get_airport_coordinates(code1), get_airport_coordinates(code2)

    if not coords1 or None in coords1:
        print(f"Airport with ICAO code {code1} not found in the database.")
        return
    if not coords2 or None in coords2:
        print(f"Airport with ICAO code {code2} not found in the database.")
        return

    distance = geodesic(coords1, coords2).kilometers
    print(f"Distance between {code1.upper()} and {code2.upper()}: {distance:.2f} kilometers")


code1 = input("Enter the ICAO code of the first airport: ").upper()
code2 = input("Enter the ICAO code of the second airport: ").upper()
run_airport_distance(code1, code2)