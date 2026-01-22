import math

def calculate_unit_price(diameter, price):
    radius = (diameter / 2) / 100
    square = (math.pi * (radius ** 2))
    return price / square

first_d = int(input("Enter the diameter of the first pizza (cm): "))
first_p = int(input("Enter the price of the first pizza (euros): "))
two_d = int(input("Enter the diameter of the second pizza (cm): "))
two_p = int(input("Enter the price of the second pizza (euros): "))
print (f"Unit price of the first pizza: {calculate_unit_price(first_d, first_p):0.2f} euros/m²")
print (f"Unit price of the second pizza: {calculate_unit_price(two_d, two_p):0.2f} euros/m²")
if calculate_unit_price(first_d, first_p) < calculate_unit_price(two_d, two_p):
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")