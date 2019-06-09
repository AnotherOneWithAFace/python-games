#Copyright 2019 Matthew Sweeney
#
# Licensed under the EUPL, Version 1.2 or – as soon they
#will be approved by the European Commission - subsequent
#versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
#Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/software/page/eupl5
#
# Unless required by applicable law or agreed to in
#writing, software distributed under the Licence is
#distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
#express or implied.
# See the LICENSE.txt for the specific language governing
#permissions and limitations under the Licence.


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
