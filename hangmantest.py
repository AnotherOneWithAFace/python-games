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
print(HANGMANPICS[pic])
while True:
    pic = ++pic
    if pic == 5:
        exit()
    print(HANGMANPICS[pic])
