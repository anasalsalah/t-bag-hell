'''  Player moves from one room to the next. Each
room is connected to other rooms in the four different directions.
Each room hosts a set of different characters and objects
that the player can interact with.'''


class Room:
    '''
    __north_room = None
    __south_room = None
    __east_room = None
    __west_room = None

    __characters = None
    __objects = None

    __description = ""
'''

    '''__firstTime = True
    __firstTimeDesc = ""
    
    def get_first_time(self):
        return self.__firstTime

    def toggle_first_time(self):
        if self.__firstTime:
            self.__firstTime = False
        else:
            self.__firstTime = True
    '''
    def __init__(self, name, desc, is_explored=False, characters=None, objects=None, north_room=None, south_room=None, east_room=None, west_room=None):
        self.__name = name
        self.__description = desc
        self.__characters = characters
        self.__objects = objects
        self.__north_room = north_room
        self.__south_room = south_room
        self.__east_room = east_room
        self.__west_room = west_room
        self.__explored = is_explored

    def __repr__(self):
        return self.description

    def __str__(self):
        return self.description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def north(self):
        return self.__north_room

    @property
    def south(self):
        return self.__south_room

    @property
    def east(self):
        return self.__east_room

    @property
    def west(self):
        return self.__west_room

    @property
    def explored(self):
        return self.__explored

    def set_north(self, room, both_directions=True):
        self.__north_room = room
        if both_directions:
            room.set_south(self, False)

    def set_south(self, room, both_directions=True):
        self.__south_room = room
        if both_directions:
            room.set_north(self, False)

    def set_east(self, room, both_directions=True):
        self.__east_room = room
        if both_directions:
            room.set_west(self, False)

    def set_west(self, room, both_directions=True):
        self.__west_room = room
        if both_directions:
            room.set_east(self, False)

    def set_explored(self, exp=True):
        self.__explored = exp
