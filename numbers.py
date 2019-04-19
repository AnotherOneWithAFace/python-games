# this is a guess the number game
import random

guessesTaken = 0

print("Hello! What's your name?")
playerName = input()

number = random.randint(1, 20)
print("well, " + playerName + " I'm thinking of a number between 1 and 20, and you have 6 guesses to get it right!")

while guessesTaken < 6:
    print("Take a guess!")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low")

    if guess > number:
        print("Your guess is too high")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good Job " + playerName + "! You guessed the number in " + guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number)
