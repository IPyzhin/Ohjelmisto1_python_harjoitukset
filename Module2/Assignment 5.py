talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
total_grams = (13.3 * lots) + (13.3 * 32 * pounds) + (13.3 * 32 * 20 * talents)
kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000
print(f"The weight in modern units: \n{kilograms} kilograms and {remaining_grams:.2f} grams.")