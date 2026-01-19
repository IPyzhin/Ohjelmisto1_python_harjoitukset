koef = 2.54
value = float(input("Enter length in inches (negative value to quit): "))
while value >= 0:
    inchtosent = koef * value
    print(f"{value} inches is {inchtosent:.2f} centimeters")
    value = float(input("Enter length in inches (negative value to quit): "))
print("Program ended.")