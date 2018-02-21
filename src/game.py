from src import printer, music, commands, messages
from levels.level_one import level_one
import sys


class Game:

    # note that level_one value is the one at time of importation! If we modify
    # level_one later on in the code, the changes are NOT reflected here.
    # So, it would be better to initialize level_one as an object here.
    __current_room = level_one.get_first_room()  # current room that user is in.
    __chosen_room = None  # next room that user wants to head to.
    __wrong_count = 0  # counts how many times in a row user inputted wrong command
    __music_player = None
    __line_wait = 0
    __last_output = ''

    @property
    def current_room(self):
        return self.__current_room

    @property
    def last_output(self):
        return self.__last_output

    def __init__(self, music_on=True, line_wait=0.05):
        self.__music_player = music.Music(music_on)
        self.__line_wait = line_wait
        self.__last_output = printer.g_print(messages.intro_msg, self.__line_wait)

    def wrong_command(self):
        self.__last_output = printer.g_print(messages.wrong_msg, 0)
        self.__wrong_count += 1

    def toggle_music(self):
        if self.__music_player.is_paused():
            self.__last_output = printer.print_music_on()
        else:
            self.__last_output = printer.print_music_off()
        self.__music_player.toggle_music()

    def new_turn(self):
        self.check_needs_help()
        self.__last_output = printer.g_print(messages.new_turn_msg, self.__line_wait)

    def player_moved(self):
        if self.__chosen_room is None:
            self.__last_output = printer.g_print(messages.hit_wall_msg)
        else:
            self.__current_room = self.__chosen_room

            if self.__current_room.explored:
                self.__last_output = printer.print_explored_room(self.__current_room)
            else:
                self.__current_room.set_explored()
                self.__last_output = printer.print_new_room(self.__current_room, self.__line_wait)

    def check_needs_help(self):
        if self.__wrong_count >= 3:
            self.__wrong_count = 0  # reset the counter and print the HELP hint
            self.__last_output = printer.g_print(messages.help_hint_msg)

    def go_west(self):
        self.__chosen_room = self.__current_room.west
        self.player_moved()

    def go_east(self):
        self.__chosen_room = self.__current_room.east
        self.player_moved()

    def go_north(self):
        self.__chosen_room = self.__current_room.north
        self.player_moved()

    def go_south(self):
        self.__chosen_room = self.__current_room.south
        self.player_moved()

    def talk(self):
        self.__last_output = printer.g_print(messages.none_talk_msg, self.__line_wait)

    def use(self):
        self.__last_output = printer.g_print(messages.nothing_use_msg, self.__line_wait)

    def examine(self):
        self.__last_output = printer.g_print(self.__current_room.description, self.__line_wait)

    def examine_here(self):
        self.__last_output = printer.g_print(self.__current_room.description)

    def examine_where(self):
        self.__last_output = printer.print_where(self.__current_room)

    def datetime(self):
        self.__last_output = printer.print_datetime()

    def help(self):
        self.__last_output = printer.g_print(messages.help_tips_msg)

    def quit(self):
        self.__last_output = printer.g_print(messages.quit_msg)
        sys.exit()

    def interpret(self, instruction):
        try:
            self.command_set[instruction](self)
        except KeyError:  # bad user command
            self.wrong_command()

    command_set = {commands.C_WEST: go_west,
                   commands.C_EAST: go_east,
                   commands.C_NORTH: go_north,
                   commands.C_SOUTH: go_south,
                   commands.C_TALK: talk,
                   commands.C_USE: use,
                   commands.C_EXAMINE: examine,
                   commands.C_HERE: examine_here,
                   commands.C_WHERE: examine_where,
                   commands.C_HELP: help,
                   commands.C_MUSIC: toggle_music,
                   commands.C_DATE: datetime,
                   commands.C_WHEN: datetime,
                   commands.C_QUIT: quit
                   }



