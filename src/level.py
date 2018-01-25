''' A Level is a set of connected rooms. It can be represented by a map.
The player can enter a level through its first room. '''


class Level:
    __firstRoom = None

    def __init__(self, first_room):
        self.__firstRoom = first_room

    def set_first_room(self, room):
        self.__firstRoom = room

    def get_first_room(self):
        return self.__firstRoom

