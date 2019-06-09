#Copyright 2019 Matthew Sweeney
#
# Licensed under the EUPL, Version 1.1 or – as soon they
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


# this program takes the player down into a world of dragons. a very small world

import random
import time

# define the into function
def displayIntro():
    print("you are on a planet full of dragons. In front of you, ")
    print("you see 2 caves. In one cave, the dragon is friendly")
    print("and will share his treasure with you. The other dragon")
    print("is greedy and hungry, and will eat you on sight.")
    print()

# define the chooseCave function, for choosing a cave
def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? [1 or 2]")
        cave = input()

    return cave

# define the checkCave function, to display the text inbetween choosing a cave and seeing the results of it. for suspense
def checkCave(chosenCave):
    print("you aproach the cave...")
    time.sleep(2)
    print("it's dark and spooky...")
    time.sleep(2)
    print("a large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print("gives you his treasure!")
    else:
        print("gobbles you down in one bite!")

# defines a repeater loop
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print("do you want to play again? [(y)es or (n)o]")
    playAgain = input()
else:
    print("goodbye!")
