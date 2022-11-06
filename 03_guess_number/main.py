import sys
import random as rand

if len(sys.argv) != 3:
    print("Invalid args")
    exit()

args = sys.argv[1:]
guess_from = args[0]
guess_to = args[1]

if not guess_from.isdecimal():
    print("Invalid from number")
    exit()

if not guess_to.isdecimal():
    print("Invalid to number")
    exit()

guess_from = int(guess_from)
guess_to = int(guess_to)

if guess_from > guess_to:
    print("Invalid from/to number")
    exit()

guess = rand.randint(guess_from, guess_to)

while True:
    your_guess = input(f"What is your guess? {guess_from} - {guess_to}: ")

    if not your_guess.isdecimal():
        continue

    your_guess = int(your_guess)
    if (guess == your_guess):
        print("Congraturations, Your Guess is right")
        break
