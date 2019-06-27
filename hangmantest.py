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

pic = 0
while True:
    pic = pic + 1
    if pic >= 5:
        break
    print(HANGMANPICS[pic])
