from levels.levelOne import levelOne
import sys
import winsound

currentRoom = levelOne.get_first_room()
chosenRoom = None
tryAgain = False

winsound.PlaySound("SillyPigSong.wav",winsound.SND_ASYNC)
print("You wake up. You feel like shit.")

while True:

    if tryAgain:
        tryAgain = False
    else:
        print(currentRoom)

    print("\nWhere do you want to go next? (north, south, east, west)")
    direction = sys.stdin.readline()

    if direction.strip() == "west":
        chosenRoom = currentRoom.get_west()
    elif direction.strip() == "east":
        chosenRoom = currentRoom.get_east()
    elif direction.strip() == "north":
        chosenRoom = currentRoom.get_north()
    elif direction.strip() == "south":
        chosenRoom = currentRoom.get_south()
    elif direction.strip() == "quit":
        print("Goodbye!")
        break
    else:
        print("The filth on your fingers prevents you from typing properly. You decide to try again.")
        tryAgain = True
        continue

    if chosenRoom == None:
        tryAgain = True
        print("You smash your face into a wall. You scream in pain. But you don't give up.")
    else:
        currentRoom = chosenRoom
