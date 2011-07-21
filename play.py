#!/usr/bin/env python

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = dict()

    def look(self):
        print self.name
        print self.description
        print "Exits are: "+(", ".join(self.exits.keys()))


class World(object):
    
    def __init__(self, width=10, height=10):
        # Holds all the rooms by their x,y position
        self.rooms = dict()

        # Create all the rooms first
        for i in xrange(width):
            for j in xrange(height):
                self.rooms[(i,j)] = Room(
                    "Wilderness".format(i,j),
                    "This is the wilderness. You feel alone.")

        # Now populate the exits of each room.
        for i in xrange(10):
            for j in xrange(10):
                if j < 9:
                    self.rooms[(i,j)].exits['north'] = self.rooms[(i, j+1)]
                if j > 0:
                    self.rooms[(i,j)].exits['south'] = self.rooms[(i, j-1)]

                if i < 9:
                    self.rooms[(i,j)].exits['east'] = self.rooms[(i+1, j)]
                if i > 0:
                    self.rooms[(i,j)].exits['west'] = self.rooms[(i-1, j)]

        # Set the starting room somewhere in the middle.
        self.starting_room = self.rooms[(width//2, height//2)]

world = World()

current_room = world.starting_room

directions = set((
    'north', 'n',
    'south', 's',
    'east',  'e', 
    'west',  'w',
))

direction_abbreviations = {
    'n':'north',
    's':'south',
    'e':'east',
    'w':'west',
}
    

while True:
    text = raw_input("Your command? ")

    if text == 'quit':
        break

    elif text == "look":
        current_room.look()

    elif text in directions:

        # Replace text with the long name, if this is an abbreviation.
        text = direction_abbreviations.get(text, text)

        # If the room has an exit with the name, then go that direction.
        if text in current_room.exits:
            print "You go {}.".format(text)

            # Replace current_room with the exit destination
            current_room = current_room.exits[text]

            # Show what the room looks like after you've moved
            current_room.look()

        else:
            print "BANG! You hit your head on the invisible constraints of \
this system."

    else:
        print "What was that?"
