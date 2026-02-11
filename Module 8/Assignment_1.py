import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='boris',
    password='Bubalar60',
    autocommit=True
)

def airport_name_query(icao):
    query = (f"SELECT name, municipality FROM airport WHERE ident = %s")
    kursori = yhteys.cursor()
    kursori.execute(query, (icao.upper(),))
    tulos = kursori.fetchone()
    if kursori.rowcount:
            print(f"Airport name: {tulos[0]}\nLocation: {tulos[1]}")
    else:
        print(f"No airport found with ICAO code {code}")
    return




code = input("Enter the ICAO code of an airport: ")
airport_name_query(code)