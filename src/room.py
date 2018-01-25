''' Player moves from one room to the next. Each
room is connected to other rooms in the four different directions.
Each room hosts a set of different characters and objects
that the player can interact with. '''


class Room:
    __northRoom = None
    __southRoom = None
    __eastRoom = None
    __westRoom = None

    __characters = None
    __objects = None

    __description = ""

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
    def __init__(self, desc, characters=None, objects=None, nRoom=None, sRoom=None, eRoom=None, wRoom=None):
        self.__description = desc
        self.__characters = characters
        self.__objects = objects
        self.__northRoom = nRoom
        self.__southRoom = sRoom
        self.__eastRoom = eRoom
        self.__westRoom = wRoom

    def __repr__(self):
        return self.get_description()

    def get_description(self):
        return self.__description

    def set_north(self,room, both_directions=True):
        self.__northRoom = room
        if both_directions:
            room.set_south(self, False)

    def set_south(self,room, both_directions=True):
        self.__southRoom = room
        if both_directions:
            room.set_north(self, False)

    def set_east(self, room, both_directions=True):
        self.__eastRoom = room
        if both_directions:
            room.set_west(self, False)

    def set_west(self, room, both_directions=True):
        self.__westRoom = room
        if both_directions:
            room.set_east(self, False)

    def get_north(self):
        return self.__northRoom

    def get_south(self):
        return self.__southRoom

    def get_east(self):
        return self.__eastRoom

    def get_west(self):
        return self.__westRoom


