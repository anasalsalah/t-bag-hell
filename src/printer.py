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

    return text


# methods defined outside of a class are by default static! They are a single instance of a function.
def get_datetime():
    return "I looked at my wrist watch. The date and time were: {}".format(datetime.now().strftime("%H:%M %B %d,%Y"))


def get_where(room):
    where_text = "At the time, I was in the " + room.name + ".\n"
    where_text += __where_direction(room, commands.C_NORTH) + "\n"
    where_text += __where_direction(room, commands.C_SOUTH) + "\n"
    where_text += __where_direction(room, commands.C_EAST) + "\n"
    where_text += __where_direction(room, commands.C_WEST)
    return where_text


def __where_direction(room, direction):
    if direction == commands.C_NORTH:
        the_room = room.north
    elif direction == commands.C_SOUTH:
        the_room = room.south
    elif direction == commands.C_EAST:
        the_room = room.east
    elif direction == commands.C_WEST:
        the_room = room.west
    else:
        raise ValueError("Invalid direction %s" % direction)

    if the_room is None:
        return "To the " + direction + ", there was a nice solid wall for me to bang my head against."
    elif the_room.explored:
        return "To the " + direction + ", there was the " + the_room.name + "."
    else:
        return "To the " + direction + ", a I couldn't tell what was out there."


def get_explored_room(room):
    return "I went to the " + room.name + "."


def get_new_room(room):
    return room.description


