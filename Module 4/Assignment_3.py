num = input("Enter a number (or press Enter to quit): ")
large = int(num)
small = int(num)
while num != "":
    if int(num) > large:
        large = int(num)
    if int(num) < small:
        small = int(num)
    else:
        num = input("Enter a number (or press Enter to quit): ")
print(f"Smallest number: {small:.1f}\nLargest number: {large:.1f}")