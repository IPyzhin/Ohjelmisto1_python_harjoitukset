import random

maxroll = int(input("Enter maksimisilmäluku:"))

def roll_dice(num):
    return random.randint(1,num)

roll = 0
while roll != maxroll:
    roll = roll_dice(maxroll)
    print(roll)