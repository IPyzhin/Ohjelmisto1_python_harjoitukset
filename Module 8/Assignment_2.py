import mysql.connector

connect = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='boris',
    password='Bubalar60',
    autocommit=True
)

def get_airports_by_country(country_code):
    query = ("SELECT type FROM airport WHERE iso_country = %s")
    cursor = connect.cursor()
    cursor.execute(query, (country_code.upper(),))
    result = cursor.fetchall()
    cursor.close()
    return result


def run_country_program(country_code):
    result = get_airports_by_country(country_code)
    output = {"small_airport": 0, "medium_airport": 0, "heliport": 0,
              "large_airport": 0, "seaplane_base": 0}

    if result:
        for rivi in result:
            type = rivi[0]
            if type in output:
                output[type] += 1

        print(f"\n\nAirports in {country_code.upper()}:")
        for typ, count in output.items():
            if count > 0:
                print(f"{count} {typ} airports")
        return output
    else:
        print(f"No airports found for country code '{country_code.upper()}'.")
        return output

code = input("Enter the country code (e.g., FI for Finland): ").upper()
run_country_program(code)