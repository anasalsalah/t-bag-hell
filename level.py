from room import Room


class Level:
    __firstRoom = None

    def __init__(self, firstRoom):
        self.__firstRoom = firstRoom

    def set_first_room(self, room):
        self.__firstRoom = room

    def get_first_room(self):
        return self.__firstRoom

