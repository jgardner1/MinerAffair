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


rooms = dict()
for i in xrange(10):
    for j in xrange(10):
        rooms[(i,j)] = Room(
            "Wilderness at {},{}".format(i,j),
            "This is the wilderness. You feel alone.")

for i in xrange(10):
    for j in xrange(10):
        if j < 9:
            rooms[(i,j)].exits['north'] = rooms[(i, j+1)]
        if j > 0:
            rooms[(i,j)].exits['south'] = rooms[(i, j-1)]

        if i < 9:
            rooms[(i,j)].exits['east'] = rooms[(i+1, j)]
        if i > 0:
            rooms[(i,j)].exits['west'] = rooms[(i-1, j)]

current_room = rooms[(0,0)]

while True:
    text = raw_input("Your command? ")

    if text == 'quit':
        break

    elif text == "look":
        current_room.look()

    elif text in current_room.exits:
        print "You go {}.".format(text)
        current_room = current_room.exits[text]
        current_room.look()

    else:
        print "What was that?"
