tunnus = input("Enter username: ")
salasana = input("Enter password: ")
count = 1
while True:
    if tunnus == "python" and salasana == "rules":
        print("Welcome")
        break
    elif count >= 5:
        print("Access denied")
        break
    elif tunnus != "python" or salasana != "rules":
        print("Incorrect username or password. Please try again.")
        tunnus = input("Enter username: ")
        salasana = input("Enter password: ")
        count += 1