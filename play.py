#!/usr/bin/env python

while True:
    text = raw_input("Your command? ")

    if text == 'quit':
        break

    elif text == "look":
        print "There is nothing to see here because you really don't exist."

    else:
        print "What was that?"
