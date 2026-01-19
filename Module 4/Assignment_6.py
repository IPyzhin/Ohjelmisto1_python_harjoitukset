import random
N = int(input("Enter number of dots N: "))
k = 1
n = 0
while k != N:
    k += 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    pyht = (x ** 2) + (y ** 2)
    if pyht < 1:
       n += 1
pi = (4 * n) / N
print(f"Approximation of pi: {pi:0.4f}")