class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = dict()
        self.contents = set()


