gender = input("Enter biological gender (male/female): ")
hvalue = float(input("Enter hemoglobin value (g/l): "))
if gender.lower() == "male":
    if 134 <= hvalue <= 167:
        print("Your hemoglobin is normal.")
    elif hvalue < 134:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
elif gender.lower() == "female":
    if 117 <= hvalue <= 155:
        print("Your hemoglobin is normal.")
    elif hvalue < 117:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")