from mineraffair.directions import directions, direction_abbreviations

class Player(object):

    def __init__(self, world, name):
        self.name = name
        self.current_room = world.starting_room


    def do(self, command):
        if command == "look":
            self.look()

        elif command in directions:
            self.go(command)

        else:
            print "What was that?"

    def go(self, direction):

        # Replace direction with the long name, if this is an abbreviation.
        direction = direction_abbreviations.get(direction, direction)

        # If the room has an exit with the name, then go that direction.
        if direction in self.current_room.exits:
            print "You go {}.".format(direction)

            # Replace current_room with the exit destination
            self.current_room = self.current_room.exits[direction]

            # Show what the room looks like after you've moved
            self.look()

        else:
            print "BANG! You hit your head on the invisible constraints of \
this system."

    def look(self):
        room = self.current_room
        print room.name
        print room.description
        print "Exits are: "+(", ".join(room.exits))
