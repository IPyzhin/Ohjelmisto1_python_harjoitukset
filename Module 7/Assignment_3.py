airports = {}

def add_airport(code, aname):
    if code in airports:
        return print("airport already exists")
    else:
        airports.update({code: aname})

while True:
    print("\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit")
    option = input("Please choose an option (1-3): ")
    if option == "1":
        icao = input("Enter the ICAO code: ")
        airport_name = input("Enter the airport name: ")
        add_airport(icao, airport_name)
        print (f"Airport {airport_name} with ICAO code {icao} has been added.")
    elif option == "2":
        icao = input("Enter the ICAO code: ")
        if icao in airports:
            print("The airport with ICAO code " + icao + " is " + airports[icao] + ".")
        else:
            print(f"No airport found with ICAO code {icao}.")
    elif option == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break