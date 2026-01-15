vuosi = int(input("Enter a year: "))
if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if not vuosi % 400 == 0:
            print(f"{vuosi} is not a leap year.")
        else:
             print(f"{vuosi} is a leap year.")
    else:
        print(f"{vuosi} is a leap year.")
elif (vuosi % 100) == 0 and (vuosi % 400) == 0:
        print(f"{vuosi} is a leap year.")
else:
    print(f"{vuosi} is not a leap year.")