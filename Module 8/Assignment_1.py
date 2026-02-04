import mysql.connector


def airport_name_query(icao):
    query = (f"SELECT ident, name, municipality FROM airport WHERE ident = '{icao.upper()}'")
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Airport name: {rivi[1]}\nLocation: {rivi[2]}")
    else:
        print("No airport found with ICAO code [ICAO-koodi]")
    return


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='boris',
    password='Bubalar60',
    autocommit=True
)

code = input("Enter the ICAO code of an airport: ")
airport_name_query(code)