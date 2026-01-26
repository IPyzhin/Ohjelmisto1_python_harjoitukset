seasons = {"1": "winter", "2": "winter", "3": "spring", "4": "spring", "5": "spring",
           "6": "summer", "7": "summer", "8": "summer", "9": "autumn", "10": "autumn",
           "11": "autumn", "12": "winter"}


def get_season(num):
    if num in seasons:
        return seasons[num]


kuukausi = input("Enter the number of a month (1-12): ")
if 1 <= int(kuukausi) <= 12:
    print(f"You entered: {kuukausi}")
    print(f"The season is {get_season(kuukausi)}.")
else:
    print(f"You entered: {kuukausi}")
    print("Please enter a number between 1 and 12.")