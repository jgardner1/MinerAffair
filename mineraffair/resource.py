"""
ResourceItems are special items that live in a room.

MineralResourceItems are mineral resources. These are buried in the ground,
waiting for some lucky miner to find the minerals. As they are mined out of
the ground, the ground becomes depleted of the minerals. Minerals do not
return once depleted.

SmallAnimalResourceItems are small animals, such as rabbits or beavers, that
are generally trapped or occasionally hunted. They have varying difficulties
of trapping and hunting.  There is an average animal size.
Different breeds of animals have different reproduction rates and prey on
different animals and plants. This means that they regularly harvest from
those resources, or if there is not enough, their population diminishes.

LargeAnimalResourceItems are large animals that must be hunted. They vary in
the difficulty of hunting

FishResources are fish in the water body. They are limited by the amount of
water in the area, and if they prey on other species, the amount of the other
species.

PlantResources are small herbs or bushes that can be easily harvested. They
vary when they are ripe. There is a certain amount of dormant seeds just in
case they get totally wiped out. Some plants are perennial and take a while to
reach maturity.

TreeResourceItems are trees in the area. These can be felled. They take a long
time to grow back, but are generally more caluable. Like plant resources,
these have seeds in the area just in case they get wiped out.

The living resources cross-pollinate to some degree to neighboring rooms.

Resources are for Terrains. They list what kind of resources a particular
terrain might have, what the limits of that resource are, etc...
"""
import random
import math

from mineraffair.item import Item


class Resource(object):
    """Terrains have resources. The resources will generate resource items for
    the rooms."""

    def __init__(self, name, amount_fn, grow_fn=None):
        self.name = name
        self.amount_fn = amount_fn
        self.grow_fn = grow_fn

    def generate(self):
        weight = self.amount_fn()
        if weight <= 0:
            return None

        else:
            return self.kind(
                resource=self,
                weight=weight)

class MineralResource(Resource):
    kind = MineralResourceItem

class AnimalResource(Resource):
    kind = AnimalResourceItem

    # eats: A list of resources that the animal preys on. This can be plants
    # or other animals. 
    def __init__(self, eats);

class ResourceItem(Item):
    """Resource items can be mined / planetd / harvested / hunted. They are
    special items in a room."""
    is_resource = True
    
    def __init__(self, resource, weight):
        Item.__init__(self, resource.name, weight=weight)
        self.resource = resource

class MineralResourceItem(ResourceItem):
    """A MineralResourceItem is a special item in a room that can be mined.
    The minerals do not regenerated. The amount of minerals discovered depends
    on the overall amount. More minerals means you take away a larger haul and
    have a higher chance of finding it."""
    is_mineral_resource = True

    def mine(self):
        weight_mined = min(self.weight,
            random.gauss(1.0, 1.0)*math.log(self.weight))

        if weight_mined <= 0:
            return None

        self.weight -= weight_mined

        return Item(name=self.name, weight=weight_mined)

class AnimalResourceItem(ResourceItem):
    """AnimalResourceItems can be hunted or stocked. They also naturally grow
    over time to a sustainable level depending on the vegetable or other
    animal resources."""
    is_animal_resource = True

    def hunt(self):
        weight_mined = min(self.weight,
            random.gauss(1.0, 1.0)*math.log(self.weight))

        if weight_mined <= 0:
            return None

        self.weight -= weight_mined

        return Item(name=self.name, weight=weight_mined)
