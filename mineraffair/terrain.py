from random import gauss

from mineraffair.resource import Resource, MineralResourceItem

class Terrain(object):

    def __init__(self, name, description, resources):
        self.name = name
        self.description = description
        self.resources = resources

    def gen_resources(self):
        return filter(None, 
            (resource.generate() for resource in self.resources))

terrains = []
def add_terrain(terrain): terrains.append(terrain)


add_terrain(Terrain(
    name="Plains",
    description="The flatness of this area of the world is annoying.",
    resources=[
        Resource('copper ore', MineralResourceItem, lambda: gauss(100, 5000)),
        Resource('iron ore', MineralResourceItem, lambda: gauss(100, 5000)),
    ]))
                
add_terrain(Terrain(
    name="Grassland",
    description="Thick grass creates plenty of hiding opportunities.",
    resources=[
        Resource('copper ore', MineralResourceItem, lambda: gauss(100, 5000)),
        Resource('iron ore', MineralResourceItem, lambda: gauss(100, 5000)),
    ]))

add_terrain(Terrain(
    name="Mountains",
    description="Towering mountains making passing through this area \
dangerous.",
    resources=[
        Resource('copper ore', MineralResourceItem, lambda: gauss(10000, 5000)),
        Resource('iron ore',   MineralResourceItem, lambda: gauss(10000, 5000)),
    ]))
