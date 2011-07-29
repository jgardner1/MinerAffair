import random

class Room(object):

    def __init__(self, terrain):
        self.name = terrain.name
        self.description = terrain.description
        self.terrain = terrain
        self.exits = dict()
        self.contents = list()
        self.contents.extend(terrain.gen_resources())

    def mine(self):
        """Yield some material from mining."""
        mined_resource = None
        total_weight = 1000
        for resource in self.contents:
            if not resource.is_mineral_resource: continue

            total_weight += resource.weight
            if random.random() < resource.weight/total_weight:
                mined_resource = resource

        if not mined_resource:
            return None

        result = mined_resource.mine()
        if not result:
            return None

        self.contents.append(result)

        if mined_resource.weight <= 0:
            self.contents.remove(mined_resource)

        return result
