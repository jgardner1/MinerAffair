from mineraffair.directions import directions, direction_abbreviations
from mineraffair.item import Item

import random

from itertools import groupby

class Player(object):

    def __init__(self, world, name):
        self.name = name
        self.current_room = world.starting_room

    def do(self, command):
        if command == "look":
            self.look()

        elif command == "mine":
            self.mine()

        elif command == "prospect":
            self.prospect()

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
            print

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
        print "Contents:"
        for name, g in groupby(sorted((_.name for _ in room.contents
                if not _.is_resource))):
            number = len(list(g))
            if number > 1:
                print "{} {}s".format(number, name)
            else:
                print name
        print "Exits are: "+(", ".join(room.exits))

    def prospect(self):
        room = self.current_room

        resources = [_ for _ in room.contents if _.is_resource]

        if not resources:
            print "There are no resources left."
        else:
            print "You are able to see the following resources:"
            for resource in resources:
                print "  * {} ({}kg)".format(resource.name, resource.weight)

    def mine(self):
        print "You chop away at the earth, looking for treasure."

        result = self.current_room.mine()

        if not result:
            print "You can't seem to find anything interesting to mine."
        else:
            print "You find {}kg of {}!".format(result.weight, result.name)
