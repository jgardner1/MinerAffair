#!/usr/bin/env python

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = dict()

    def look(self):
        print self.name
        print self.description

room1 = Room(
    name="This room is this room",
    description="This room is a room, like other rooms but a little \
different."
)

room2 = Room(
    name="This is another room",
    description="This room is slightly different from the previous room."
)

room1.exits['north'] = room2
room2.exits['south'] = room1

current_room = room1

while True:
    text = raw_input("Your command? ")

    if text == 'quit':
        break

    elif text == "look":
        current_room.look()

    elif text in current_room.exits:
        print "You go {}.".format(text)
        current_room = current_room.exits[text]

    else:
        print "What was that?"
