import io
import os
from contextlib import redirect_stdout
from src import game, messages, commands
# from robot.api.deco import keyword


class GameLibrary(object):
    __game = None
    __result = ""

    where_to_go = None

    def __init__(self, verbose=True):
        os.chdir('C:/Users/Anas/PycharmProjects/t-bag-hell/')
        print("verbose is: %s" % verbose)

    # redirects stdout to an output IO which allows us to
    # process game's messages for testing.
    def __call_output(self, fct, *args):
        output = io.StringIO()
        with redirect_stdout(output):
            fct(*args)
        self.__result = output.getvalue()

    #@keyword('Start game')
    def start_game(self, music_on=False, line_wait=0.0):
        self.__call_output(self.__init_game, music_on, line_wait)
        # self.result_should_be("Introduction", messages.intro_msg)
        self.where_to_go = {commands.C_NORTH: self.__game.go_north,
                            commands.C_SOUTH: self.__game.go_south,
                            commands.C_WEST: self.__game.go_west,
                            commands.C_EAST: self.__game.go_east}

    def __init_game(self,music_on, line_wait):
        self.__game = game.Game(music_on, line_wait)

    def result_should_be(self, title, expected):
        if self.__result.strip() != expected.strip():
            raise AssertionError("%s: actual result does not match expected." % title)

    def is_wrong_command(self, command):
        self.__call_output(self.__game.interpret, command)
        #self.result_should_be("Wrong Command", messages.wrong_msg)

    def move(self,direction):
        self.__call_output(self.where_to_go[direction])

    def if_in_room(self,room_name):
        if self.__game.current_room.name != room_name:
            raise AssertionError("Player is NOT in room titled: %s" % room_name)

    def get_room_desc(self):
        return self.__game.current_room.description

    def get_room_name(self):
        return self.__game.current_room.name

    def examine_room(self):
        self.__call_output(self.__game.interpret, commands.C_EXAMINE)
        # self.result_should_be("Room Description", self.__game.current_room.description)

    def hit_wall(self, direction):
        # go in the same direction 10 times. bound to hit something!
        for i in range(1, 10):
            self.where_to_go[direction]()
        # go in that direction one more time
        self.__call_output(self.where_to_go[direction])
        # self.result_should_be("Hitting a Wall", messages.wall_msg)

    def get_intro_msg(self):
        return messages.intro_msg

    def get_wrong_msg(self):
        return messages.wrong_msg


# library = GameLibrary()
# library.start_game(False,0.0)
# library.is_wrong_command("use")
# library.is_hit_wall(commands.C_NORTH)
# #if library.if_in_room("bedroom"):
# library.examine_room()
# library.get_room_desc()
