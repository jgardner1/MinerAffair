from mineraffair.directions import (
    directions,
    direction_abbreviations,
    direction_vectors)
#from mineraffair.item import Item

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

        elif command in ("dig", "d"):
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
            print "You go {direction}.".format(direction=direction)

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
        for name, g in groupby(sorted((_.name for _ in room.contents))):
            number = len(list(g))
            if number > 1:
                print "{} {}s".format(number, name)
            else:
                print name
        print "Exits are: "+(", ".join(room.exits))

    def mine(self):
        print "You chop away at the earth, looking for treasure."

        possibilities = [
            (1.0, dict(name='rocks')),
            (1.0, dict(name='copper')),
            (1.0, dict(name='iron')),
            (0.1, dict(name='silver')),
        ]

        poss_iter = iter(possibilities)
        choice = poss_iter.next()
        total = choice[0]
        for poss in poss_iter:
            total += poss[0]
            if random.random() < poss[0]/total:
                choice = poss

        result = Item(**choice[1])

        room = self.current_room
        room.contents.add(result)
        print "You find {}!".format(result.name)

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
        room = self.world.rooms.get(new_pos, None)

        if room is None:
            print "need to make a new room"
            # room = Room(..., new_pos)
            # world.rooms[new_pos] = room

        # Link the two rooms together.

