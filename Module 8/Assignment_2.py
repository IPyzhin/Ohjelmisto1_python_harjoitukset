import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='boris',
    password='Bubalar60',
    autocommit=True
)


def get_airports_by_country(country_code):
    query = (f"SELECT id, type FROM airport WHERE iso_country = '{country_code.upper()}'")
    return query

def run_country_program(country_code):
    small = medium = heliport = large = 0
    kursori = yhteys.cursor()
    kursori.execute(get_airports_by_country(country_code))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            if rivi[1] == "small_airport":
                small += 1
            elif rivi[1] == "medium_airport":
                medium += 1
            elif rivi[1] == "large_airport":
                large += 1
            elif rivi[1] == "heliport":
                heliport += 1
        return small, medium, heliport, large
    else:
        print("No airport found with ICAO code [ICAO-koodi]")
        return 0, 0, 0, 0

code = input("Enter the country code (e.g., FI for Finland): ")
small, medium, heliport, large = run_country_program(code)
print(f"Airports in {code}: \n")
print(f"{small} small_airport airports")
print(f"{medium} medium_airport airports")
print(f"{heliport} heliport airports")
print(f"{large}  large_airports")