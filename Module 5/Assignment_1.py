import random
rolls = int(input("How many dice to roll: "))
dicesum = 0
for i in range(rolls):
    num = random.randint(1,6)
    dicesum += num
print("Sum of the dice:", str(dicesum))
