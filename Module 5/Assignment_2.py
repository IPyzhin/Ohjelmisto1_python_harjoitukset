numbers = []
while True:
    num = input("Enter a number: ")
    if num == "":
        break
    numbers.append(float(num))
numbers.sort(reverse=True)
print("The greatest numbers in descending order: ")
for n in numbers[:5]:
    print(n)
