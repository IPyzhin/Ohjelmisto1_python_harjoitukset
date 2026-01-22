dev = []
num = int(input("Enter an integer: "))
for n in range (1, int(num)+1):
    if int(num) % n == 0:
        dev.append(n)
if len(dev) == 2:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")