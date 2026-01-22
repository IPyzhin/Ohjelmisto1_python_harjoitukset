def gallons_to_liters(volume):
    return volume * 3.785


while True:
    ammount = float(input("Enter a volume in American gallons (negative value to quit): "))
    if ammount >= 0:
        print(f"{ammount:.1f} American gallons is {gallons_to_liters(ammount):.2f} liters.")
    else:
        break
print("Program finished.")