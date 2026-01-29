names = set()

def set_of_names(gname):
    if gname in names:
        return print("Existing name")
    else:
        names.add(gname)
        return print("New name")

while True:
    name = input("Enter name: ")
    if name == "":
        break
    print(set_of_names(name))

print("Entered names: ")
for name in names:
    print(name)