class Room(object):
    def __init__(self, name, description, pos):
        self.name = name
        self.description = description
        self.pos = pos
        self.exits = dict()
        self.contents = set()



