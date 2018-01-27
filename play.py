from levels.levelOne import levelOne
from datetime import datetime
import sys
import time
from pygame import mixer

C_NORTH = "north"
C_SOUTH = "south"
C_EAST = "east"
C_WEST = "west"
C_HELP = "help"
C_WHERE = "where"
C_DATE = "date"
C_WHEN = "when"
C_QUIT = "quit"
C_EXAMINE = "examine"
C_HERE = "here"
C_MUSIC = "music"

help_msg = '''I thought to myself, what could I do? I could:
- explore in one of the directions: NORTH, SOUTH, EAST, or WEST.
- toggle the MUSIC on or off.
- Look around to find out WHERE in the Hell I was.
- Look at my watch to know WHEN I was.
- EXAMINE the place I'm in or any of the objects or characters I find here.
- check my INVENTORY for objects I'm carrying with me.
- TALK to any of the characters around me.
- USE any of the objects, optionally WITH another object or character.'''

quit_msg = "You must be busy. I'll finish the story for you later. Bye for now!"

wrong_msg = '''At that moment, my mind felt like an incensed ape banging a keyboard with his fists.
Random words and jumbled letters appeared before my eyes.
But I collected myself and focused...'''

wall_msg = "I smashed my face into a wall. I screamed in pain. But I didn't give up."


def datetime_msg():
    return "I looked at my wrist watch. The date and time were: {}\n".format(datetime.now().strftime("%H:%M %B %d,%Y"))


def g_print(line, seconds=0):
    print(line, "\n")
    time.sleep(seconds)


def print_where_dir(room, direction):
    the_room = None
    if direction == C_NORTH:
        the_room = room.north
    elif direction == C_SOUTH:
        the_room = room.south
    elif direction == C_EAST:
        the_room = room.east
    elif direction == C_WEST:
        the_room = room.west
    else:
        print("invalid direction")

    if the_room is None:
        print("To the " + direction + ", there was a nice solid wall for me to bang my head against.")
    elif the_room.explored:
        print("To the " + direction + ", I could see the " + the_room.name + ".")
    else:
        print("To the " + direction + ", there was unknown territory waiting to be explored!")


def print_where(room):
    print("At the time, I was in the " + room.name + ".")
    print_where_dir(room, C_NORTH)
    print_where_dir(room, C_SOUTH)
    print_where_dir(room, C_EAST)
    print_where_dir(room, C_WEST)
    print("")


def go_to_room(room):
    if room.explored:
        g_print("I went back to the " + room.name + ".", 0)
    else:
        room.set_explored()
        g_print(room)


def toggle_music(the_song, toggle):
    if toggle:
        g_print("I decided to put on my earphones and listen to my favorite song.", 0)
        the_song.play()
    else:
        g_print("I was getting tired of the music, so I took my earphones off.", 0)
        the_song.stop()


mixer.init()
song = mixer.music
song.load("media/silly-pig-song.ogg")
music_on = False

current_room = levelOne.get_first_room()
chosen_room = None
try_again = False

g_print('''
~~~~~~~~~~~~~~~~~~~~THIS IS HELL!~~~~~~~~~~~~~~~~~~~~~
~~ a Kafka-esque comedy of Dante-esque proportions ~~~''')
g_print('''I've been to Hell and back. Literally.
Hell. With a capital H.''')
g_print("Did I ever tell you that story?")

g_print('''Of course, I didn't realize I was in THE Hell.
That day, I woke up in my room with a hangover.
I felt like shit, but it was nothing out of the ordinary.''')

while True:

    if try_again:
        try_again = False
    else:
        go_to_room(current_room)

    print("I deliberated what to do...")
    instruction = sys.stdin.readline().strip()

    if instruction == C_WEST:
        chosen_room = current_room.west
    elif instruction == C_EAST:
        chosen_room = current_room.east
    elif instruction == C_NORTH:
        chosen_room = current_room.north
    elif instruction == C_SOUTH:
        chosen_room = current_room.south
    else:
        if instruction == C_EXAMINE:
            g_print(current_room, 0)
        elif instruction == C_HERE:
            g_print(current_room, 0)
        elif instruction == C_HELP:
            g_print(help_msg, 0)
        elif instruction == C_WHERE:
            print_where(current_room)
        elif instruction == C_MUSIC:
            music_on = not music_on
            toggle_music(song, music_on)
        elif instruction == C_DATE or instruction == C_WHEN:
            print(datetime_msg())
        elif instruction == C_QUIT:
            print(quit_msg)
            break
        else:
            g_print(wrong_msg, 1)
        try_again = True
        continue

    if chosen_room is None:
        try_again = True
        g_print(wall_msg, 0)
    else:
        current_room = chosen_room
