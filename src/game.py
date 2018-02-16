from src import printer, music, commands, messages
from levels.level_one import level_one
import sys


class Game:

    # note that level_one value is the one at time of importation! If we modify
    # level_one later on in the code, the changes are NOT reflected here.
    # So, it would be better to initialize level_one as an object here.
    _current_room = level_one.get_first_room()  # current room that user is in.
    _chosen_room = None  # next room that user wants to head to.
    _is_same_room = False  # user did not move to next room
    _wrong_count = 0  # counts how many times in a row user inputted wrong command
    _music_player = None

    def start(self):
        self._music_player = music.Music()
        printer.g_print(messages.intro_msg)

    def confused(self):
        printer.g_print(messages.wrong_msg)
        self._wrong_count += 1

    def toggle_music(self):
        self._music_player.toggle_music()

    def new_turn(self):
        self.check_needs_help()
        if not self._is_same_room:
            printer.g_print(messages.new_turn_msg)

    def check_hit_wall(self):
        if self._chosen_room is None:
            printer.g_print(messages.wall_msg, 0)
            self._is_same_room = True
        else:
            self._current_room = self._chosen_room
            printer.print_room(self._current_room)
            self._is_same_room = False

    def check_needs_help(self):
        if self._wrong_count >= 3:
            self._wrong_count = 0  # reset the counter and print the HELP hint
            printer.g_print(messages.help_hint_msg)

    def go_west(self):
        self._chosen_room = self._current_room.west
        self.check_hit_wall()

    def go_east(self):
        self._chosen_room = self._current_room.east
        self.check_hit_wall()

    def go_north(self):
        self._chosen_room = self._current_room.north
        self.check_hit_wall()

    def go_south(self):
        self._chosen_room = self._current_room.south
        self.check_hit_wall()

    def talk(self):
        printer.g_print(messages.none_talk_msg)

    def use(self):
        printer.g_print(messages.nothing_use_msg)

    def examine(self):
        printer.g_print(self._current_room.description)

    def examine_here(self):
        printer.g_print(self._current_room.description)

    def examine_where(self):
        printer.print_where(self._current_room)

    def datetime(self):
        printer.print_datetime()

    @staticmethod
    def help():
        printer.g_print(messages.help_tips_msg, 0)

    @staticmethod
    def quit():
        printer.g_print(messages.quit_msg, 0)
        sys.exit()

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

    def interpret(self, instruction):
        try:
            self.command_set[instruction](self)
        except KeyError:  # bad user command
            self.confused()

