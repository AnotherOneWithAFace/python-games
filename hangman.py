# Copyright 2019 Matthew Sweeney
#
# Licensed under the EUPL, Version 1.2 or – as soon they
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/software/page/eupl5
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the LICENSE.txt for the specific language governing
# permissions and limitations under the Licence.

import random

HANGMANPICS = ['''
    +-------+
    |       |
    |       |
            |
            |
            |
            |
            |
            |
            |
            |
===============''', '''

    +-------+
    |       |
    |       |
    o       |
            |
            |
            |
            |
            |
            |
            |
===============''', '''

    +-------+
    |       |
    |       |
    o       |
    |       |
    |       |
    |       |
            |
            |
            |
            |
===============''', '''

    +-------+
    |       |
    |       |
    o       |
   /|\      |
  / | \     |
    |       |
            |
            |
            |
            |
===============''', '''

    +-------+
    |       |
    |       |
    o       |
   /|\      |
  / | \     |
    |       |
   / \      |
  /   \     |
            |
            |
===============''']


words = "ant baboon badger bat bear beaver beetle bird camel cat clam cobra cougar coyote crab crane crow deer dog donkey duck eagle ferret fish fox frog goat goose hawk iguana jackal koala leech lemur lion lizard llama mite mole monkey moose moth mouse mule newt otter owl oyster panda parrot pigeon python quail rabbit ram rat raven rhino salmon seal shark sheep skunk sloth slug snail snake spider squid stork swan tick tiger toad trout turkey turtle wasp weasel whale wolf wombat worm zebra"

def getRandomWord(wordList):
    # this function returns a random string from the passed list of strings
    words = wordList.split()
    wordIndex = random.randint(0, (len(wordList) -1))
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print("Missed Letters:")
    for letter in missedLetters:
        print(str(letter))
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        # show the secret word with spaces in between each letter
        print(letter)
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, not something else
    while True:
        print("guesss a letter")
        guess = input().lower()
        if len(guess) > 1:
            print("please enter a single letter")
        elif guess in alreadyGuessed:
            print("you have already guessed that letter. Try again")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("please enter an ENGLISH LETTER")
        else:
            return guess

def playAgain():
    # this function returns True if the player wants to play again, otherwise it returns False
    print("do you want to play again? [(y)es or (n)o]")
    return input().lower().startswith('y')

print("H A N G M A N")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # let the player type in a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print("Yes! The secret word is '" + secretWord + "'! You've won!")
                gameIsDone = True
            else:
                missedLetters = missedLetters + guess

                # check if the player has guessed too many times and lost
                if len(missedLetters) == len(HANGMANPICS) - 1:
                    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                    print("You have run out of guesses!\nAfter " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses, the word was '" + secretWord + "'")
                    gameIsDone = True

            # ask the player if they want to play again (but only if the game is done)
            if gameIsDone:
                if playAgain():
                    gameIsDone = False
                    missedLetters = ''
                    correctLetters = ''
                    secretWord = getRandomWord(words)
                else:
                    gameIsDone = True

            if gameIsDone == True:
                print("goodbye!")
                exit()
