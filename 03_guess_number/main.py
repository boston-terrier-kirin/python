import sys
import random as rand

args = sys.argv[1:]

if len(args) != 2:
    print("Invalid args")

guess_from = sys.argv[1]
guess_to = sys.argv[2]

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
