import random

randomNumbers = random.randint(1,100)
userChoice = 0

while userChoice != randomNumbers:
    userChoice = int(input("Guess the number in my mind: "))
    if userChoice < randomNumbers:
        print("Your choice is too low!")

    elif userChoice > randomNumbers:
        print("Your choice is too high!")

print("You've quessed correcty!")
