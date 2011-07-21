#!/usr/bin/env python

current_room = dict(
    name="This room is this room",
    description="This room is a room, like other rooms but a little \
different."
)
while True:
    text = raw_input("Your command? ")

    if text == 'quit':
        break

    elif text == "look":
        print current_room['name']
        print current_room['description']

    else:
        print "What was that?"
