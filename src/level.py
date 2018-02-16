""" A Level is a set of connected rooms. It can be represented by a map.
The player can enter a level through its first room. """

# import abc


# class Level(metaclass=abc.ABCMeta):
class Level:

    def __init__(self, room):
        self.__first_room = room

    def set_first_room(self, room):
        self.__first_room = room

    def get_first_room(self):
        return self.__first_room

    ''' create a level from a list of rooms in a train structure '''
    # TODO test this method!
    @classmethod
    def create_train(cls, rooms):
        i = 0
        while i < (rooms.__len__-1):
            rooms[i].set_east(rooms[i+1])
            i += 1
        return cls(rooms[0])

    # experimenting with abstract methods. Guide:
    # https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods
    # https://pymotw.com/3/abc/
    # @abc.abstractmethod
    def get_type(self):
        raise NotImplementedError  # this is not needed if using @abc.abstractmethod


# experimenting with abstract methods
# print("Howdy!")
# lev = Level(None)
# print("If we implement ABC, we should not see this line!")
# print(lev.get_type())
