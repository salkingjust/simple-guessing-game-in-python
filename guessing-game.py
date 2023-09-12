import random

randomNumbers = random.randint(1,100)
userChoice = 0
chances = 5
print("Welcome to the Number Guessing Game!")
print(f"You have {chances} chances to guess the number between 1 and 100.")

while userChoice != randomNumbers and chances > 0:
    userChoice = int(input(f"Guess the number in my mind({chances} chances left): "))
    if userChoice < randomNumbers:
        print("Your choice is too low!")

    elif userChoice > randomNumbers:
        print("Your choice is too high!")
    chances -= 1
print("You've quessed correcty!")
