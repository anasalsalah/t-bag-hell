import os
from src import game, messages


class GameLibrary(object):

    __game = None

    def __init__(self):
        os.chdir('C:/Users/Anas/PycharmProjects/t-bag-hell/')

    def __init_game(self, music_on, line_wait):
        self.__game = game.Game(music_on, line_wait)

    def start_game(self, music_on=False, line_wait=0.0):
        self.__init_game(music_on, line_wait)

    def result_should_be(self, title, expected):
        if self.__game.last_output.strip() != expected.strip():
            raise AssertionError("%s: actual result does not match expected." % title)

    def input_command(self, command):
        self.__game.interpret(command)

    def move(self,direction):
        self.__game.interpret(direction)

    def validate_room(self,room_name):
        if self.__game.current_room.name != room_name:
            raise AssertionError("Player is NOT in room titled: %s" % room_name)

    def get_room_desc(self):
        return self.__game.current_room.description

    def get_room_name(self):
        return self.__game.current_room.name

    @staticmethod
    def get_intro_msg():
        return messages.intro_msg

    @staticmethod
    def get_wrong_msg():
        return messages.wrong_msg
