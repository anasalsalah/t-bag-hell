from src.room import Room
from src.level import Level

'''constructing first room'''

bedRoom = Room("Your bedroom is a mess. Your mom is probably turning in her grave.")
kitchen = Room("Your kitchen is composed of pizza scraps and dirty cutlery."
               "Nothing else could be seen in this heinous fly trap.")
living = Room("The living room still looks like a dump."
              "Things seldom change around here. Including your hygenic proclivities.")
hallway = Room("This hallway seems to extend into infinity."
               "Each side of the hallway is lined with room doors just like yours."
               "There's an elevator to the west.")
elevator = Room("This elevator is operated with a steel lever. Quite old school.")
spa = Room("As soon as you exit the elevator, you're greeted with a friendly Velociraptor in a suit. \"Welcome, Sirmadam!\"")

bedRoom.set_east(kitchen)
bedRoom.set_west(living)
bedRoom.set_north(hallway)
hallway.set_west(elevator)
elevator.set_south(spa)

levelOne = Level(bedRoom)
