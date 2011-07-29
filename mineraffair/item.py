import random

class Item(object):
    is_resource = False
    is_mineral_resource = False

    def __init__(self, name, weight=0.0, resource=None):
        self.name = name
        self.weight = float(weight)
        self.resource = resource
