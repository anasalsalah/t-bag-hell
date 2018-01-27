from src.room import Room
from src.level import Level

'''constructing  first room'''

bedRoom = Room('bedroom', '''My bedroom was a MESS (it probably still is).
My mom is probably turning in her grave.''')

kitchen = Room('kitchen', '''My kitchen was composed of pizza scraps, dirty cutlery,
and swarms of bugs circling black garbage bags.
I could see nothing else in this heinous fly trap.''')

living = Room('living room', '''The living room still looked like a dump.
Things seldom change around here. Including my hygenic proclivities.''')

hallway = Room('hallway', '''I stepped out of my house, and... what's this???
Instead of my front yard, I walk into a hallway that seems to extend into infinity!
Each side of the hallway is lined with room doors just like mine!
My hangover suddenly gave way to a sick stomach and wobbly knees.
... What's going on here???

To the west, I spotted an elevator that looks too old to function. 
But it seemed to be the only thing that would get me out of this nightmare.''')

elevator = Room('elevator', '''This elevator is operated with a steel lever. Quite old school.''')

spa = Room('spa', '''I pulled the lever and headed down. The counter kept counting, counting, counting down.
In God-knows-how-long, I exit the elevator, and I'm greeted by a friendly Velociraptor in a suit.
Welcome, Sirmadam!''')

bedRoom.set_east(kitchen)
bedRoom.set_south(living)
bedRoom.set_north(hallway)
hallway.set_west(elevator)
elevator.set_south(spa)

levelOne = Level(bedRoom)
