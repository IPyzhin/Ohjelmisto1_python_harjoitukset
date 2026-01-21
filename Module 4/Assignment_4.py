import random
rnum = random.randint(1,10)
while True:
    guess_str = input("Guess a number (1-10): ")
    guess = int(guess_str)
    if guess == rnum:
        print("Correct")
        break
    elif guess > rnum:
        print("Too high")
    else:
        guess < rnum
        print("Too low")

