#!/usr/bin/env python

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look(self):
        print self.name
        print self.description

current_room = Room(
    name="This room is this room",
    description="This room is a room, like other rooms but a little \
different."
)
while True:
    text = raw_input("Your command? ")

    if text == 'quit':
        break

    elif text == "look":
        current_room.look()

    else:
        print "What was that?"
