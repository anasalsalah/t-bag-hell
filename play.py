from levels.levelOne import levelOne
from playsound import playsound
import sys
import time


def gprint(line, seconds=3):
    print(line)
    time.sleep(seconds)

currentRoom = levelOne.get_first_room()
chosenRoom = None
tryAgain = False

playsound('media/silly-pig-song.mp3', False)

gprint("~~~~~~~~~~~THIS IS HELL!~~~~~~~~~~~~")
gprint("~~~a fantasy-action-comedy-drama~~~~\n\n")
gprint("I've been to Hell and back. Literally.\nHell. With a capital H.")
gprint("Have I told you that story?\n\n")

gprint('''Of course, I didn't realize I was in THE Hell.
I woke up in my room with a hangover.
I felt like shit, but it was nothing out of the ordinary.''',5)

while True:

    if tryAgain:
        tryAgain = False
    else:
        gprint(currentRoom,4)

    gprint("\nI deliberated over which direction to take... (north, south, east, west)")
    direction = sys.stdin.readline()

    if direction.strip() == "west":
        chosenRoom = currentRoom.west
    elif direction.strip() == "east":
        chosenRoom = currentRoom.east
    elif direction.strip() == "north":
        chosenRoom = currentRoom.north
    elif direction.strip() == "south":
        chosenRoom = currentRoom.south
    elif direction.strip() == "quit":
        gprint("You must be busy. I'll finish the story for you later. Bye for now!")
        break
    else:
        gprint('''At that moment, my head felt a keyboard spitting out random letters,
like some ape was trying to fist-bang his way into writing Hamlet.
But I collected myself and focused.''',5)
        tryAgain = True
        continue

    if chosenRoom == None:
        tryAgain = True
        gprint("I smashed my face into a wall. I screamed in pain. But I didn't give up.")
    else:
        currentRoom = chosenRoom
