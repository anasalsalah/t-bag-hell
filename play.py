from levels.level_one import level_one
import sys
from src import printer, music, commands, messages


music_player = music.Music()
current_room = level_one.get_first_room()  # current room that user is in.
chosen_room = None  # next room that user wants to head to.
try_again = False  # user did not move to next room
wrong_count = 0  # counts how many times in a row user inputted wrong command

# start the game by showing the introduction
printer.g_print(messages.intro_msg)

while True:

    if try_again:  # user still in the same room, so no need to print the room they're in
        try_again = False  # reset flag
    else:  # show the current room the user is in
        printer.print_room(current_room)
        printer.g_print(messages.new_turn_msg)

    if wrong_count >= 3:
        wrong_count = 0  # reset the counter and print the HELP hint
        printer.g_print(messages.help_hint_msg)


    # read the user command
    instruction = sys.stdin.readline().strip().lower()

    # if the command is a direction, set the chosen room
    if instruction == commands.C_WEST:
        chosen_room = current_room.west
    elif instruction == commands.C_EAST:
        chosen_room = current_room.east
    elif instruction == commands.C_NORTH:
        chosen_room = current_room.north
    elif instruction == commands.C_SOUTH:
        chosen_room = current_room.south
    else: # the command is not navigational, user stays in same room
        if instruction == commands.C_TALK:
            printer.g_print(messages.none_talk_msg)
        elif instruction == commands.C_USE:
            printer.g_print(messages.nothing_use_msg)
        elif instruction == commands.C_EXAMINE:
            printer.g_print(current_room.description)
        elif instruction == commands.C_HERE:
            printer.g_print(current_room.description)
        elif instruction == commands.C_HELP:
            printer.g_print(messages.help_tips_msg, 0)
        elif instruction == commands.C_WHERE:
            printer.print_where(current_room)
        elif instruction == commands.C_MUSIC:
            music_player.toggle_music()
        elif instruction == commands.C_DATE or instruction == commands.C_WHEN:
            printer.print_datetime()
        elif instruction == commands.C_QUIT: # quit the game, exit the main loop
            printer.g_print(messages.quit_msg, 0)
            break
        else: # bad user command
            printer.g_print(messages.wrong_msg)
            wrong_count += 1
        try_again = True # indicate that user is still in same room
        continue  # go back to main loop

    if chosen_room is None:  # user navigated to a wall
        try_again = True # indicate that user is still in same room
        printer.g_print(messages.wall_msg, 0)
    else:  # user navigated to an adjacent room
        current_room = chosen_room
