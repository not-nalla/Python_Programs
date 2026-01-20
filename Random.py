import random

secret_number = random.randint(1, 10)

guess = input("Guess a number between 1 and 10: ")

if guess.isdigit():
    guess = int(guess)

    if guess == secret_number:
        print("Correct! You guessed the number.")
    else:
        print("Wrong guess.")
        print("The correct number was:", secret_number)
else:
    print("Please enter a valid number.")
