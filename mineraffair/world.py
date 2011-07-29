
import random
from mineraffair.room import Room
from mineraffair.terrain import terrains

class World(object):

    def __init__(self, width=10, height=10):
        # Holds all the rooms by their x,y position
        self.rooms = dict()

        # Create all the rooms first
        for i in xrange(width):
            for j in xrange(height):
                self.rooms[(i,j)] = Room(terrain=random.choice(terrains))

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
