from src import commands
import time
from datetime import datetime


# core method used by ALL other methods in this module
def g_print(text, line_wait=0):
    # TODO print the text letter by letter in proportion to the seconds passed
    # interval = seconds / line.__len__()
    text_list = text.split("\n")
    for line in text_list:
        print(line)
        time.sleep(line.__len__() * line_wait)

# methods defined outside of a class are by default static! They are a single instance of a function.
def print_datetime():
    g_print("I looked at my wrist watch. The date and time were: {}"
            .format(datetime.now().strftime("%H:%M %B %d,%Y")))


def print_where(room):
    g_print("At the time, I was in the " + room.name + ".")
    print_where_dir(room, commands.C_NORTH)
    print_where_dir(room, commands.C_SOUTH)
    print_where_dir(room, commands.C_EAST)
    print_where_dir(room, commands.C_WEST)


def print_where_dir(room, direction):
    the_room = None
    if direction == commands.C_NORTH:
        the_room = room.north
    elif direction == commands.C_SOUTH:
        the_room = room.south
    elif direction == commands.C_EAST:
        the_room = room.east
    elif direction == commands.C_WEST:
        the_room = room.west
    else:
        g_print("invalid direction")

    if the_room is None:
        g_print("To the " + direction + ", there was a nice solid wall for me to bang my head against.")
    elif the_room.explored:
        g_print("To the " + direction + ", I could see the " + the_room.name + ".")
    else:
        g_print("To the " + direction + ", there was unknown territory waiting to be explored!")


def print_room(room, line_wait):
    if room.explored:
        g_print("I went back to the " + room.name + ".")
    else:
        room.set_explored()
        g_print(room.description, line_wait)


def print_music_off():
    g_print("I was getting tired of the music, so I took my earphones off.")


def print_music_on():
    g_print("I decided to put on my earphones and listen to my favorite song.")

