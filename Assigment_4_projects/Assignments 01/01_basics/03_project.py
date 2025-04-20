#Number Guessing Game

import random

def play_game():
    number = random.randint(1, 99)
    print("I'm thinking of a number between 1 and 99...")

    guess = int(input("Your guess: "))

    while guess != number:
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
        
        guess = int(input("Try again: "))

    print("🎉 Congratulations! You guessed it right! The number was:", number)

# Run the game
play_game()

