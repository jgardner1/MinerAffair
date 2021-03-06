from vector import Vector
import random
from mineraffair.room import Room
from mineraffair.terrain import terrains
from mineraffair.directions import direction_vectors

class World(object):

    def __init__(self, width=10, height=10):
        # Holds all the rooms by their x,y position
        self.rooms = dict()

        # Create all the rooms first
        for i in xrange(width):
            for j in xrange(height):
                pos = Vector((i, j, 0))
                self.rooms[pos] = Room(
                    terrain=random.choice(terrains),
                    pos=pos)

        # One of the rooms is an abandoned cabin.
        self.cabin = self.rooms[Vector((random.randrange(width), random.randrange(height),0 ))]
        self.cabin.name = 'Abandoned Cabin'
        self.cabin.description = 'This is an abandoned cabin, long forgotten.'

        def link_dir(room, dir):
            vec = direction_vectors[dir]
            try:
                room.exits[dir] = self.rooms[room.pos+vec]
            except KeyError:
                return

        # Now populate the exits of each room.
        for i in xrange(10):
            for j in xrange(10):
                room = self.rooms[Vector((i,j,0))]

                link_dir(room, 'north')
                link_dir(room, 'south')
                link_dir(room, 'east')
                link_dir(room, 'west')

        # Set the starting room somewhere in the middle.
        self.starting_room = self.rooms[Vector((width//2, height//2,0))]

    def add_room(self, room):
        self.rooms
