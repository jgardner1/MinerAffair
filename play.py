#!/usr/bin/env python

import random

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = dict()

terrains = (
    dict(
        name="Meadow",
        description="You are surrounded by grass and flowers.",
    ),
    dict(
        name="Hills",
        description="There are rolling hills here, quite annoying.",
    ),
    dict(
        name="Mountains",
        description="Mountains make this area quite foreboding.",
    ),
    dict(
        name="Valley",
        description="Nestled between the hills and mountains, this valley is \
quiet.",
    ),
    dict(
        name="Lake",
        description="You stand at the edge of a perfectly blue lake.",
    )
)

class World(object):
    
    def __init__(self, width=10, height=10):
        # Holds all the rooms by their x,y position
        self.rooms = dict()

        # Create all the rooms first
        for i in xrange(width):
            for j in xrange(height):
                self.rooms[(i,j)] = Room(**random.choice(terrains))

        # One of the rooms is an abandoned cabin.
        self.cabin = self.rooms[(random.randrange(width), random.randrange(height))]
        self.cabin.name = 'Abandoned Cabin'
        self.cabin.description = 'This is an abandoned cabin, long forgotten.'


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

class Player(object):

    def __init__(self,  name):
        self.name = name
        self.current_room = world.starting_room

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

        


player = Player("Bob")

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
        player.look()

    elif text in directions:
        player.go(text)

    else:
        print "What was that?"
