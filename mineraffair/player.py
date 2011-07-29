from mineraffair.directions import (
    directions,
    direction_abbreviations,
    opposite_directions,
    direction_vectors)
#from mineraffair.item import Item

from terrain import underground_terrain
from room import Room

import random

from itertools import groupby

class Player(object):

    def __init__(self, world, name):
        self.world = world
        self.name = name
        self.current_room = world.starting_room

    def do(self, command):
        command, pred = (command.split(None, 1)+[None, None])[:2]
        
        if command in ("look", "l"):
            self.look()

        elif command in ("mine", "m"):
            self.mine()

        elif command in ("prospect", "p"):
            self.prospect()

        elif command in ("dig",):
            self.dig(pred)

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

    def dig(self, direction):
        room = self.current_room
        direction = direction_abbreviations.get(direction, direction)

        if direction in room.exits:
            print "There is already an exit in that direction"
            return

        cur_pos = room.pos
        vector = direction_vectors[direction]
        new_pos = cur_pos+vector
        print "Digging %s" % (direction,)

        # Find the room in that direction, if any
        new_room = self.world.rooms.get(new_pos, None)

        if new_room is None:
            new_room = Room(underground_terrain, new_pos)
            self.world.rooms[new_pos] = room

        # Link the two rooms together.
        room.exits[direction] = new_room
        new_room.exits[opposite_directions[direction]] = room
        print "You dig into a new room."
        self.current_room = new_room
        
