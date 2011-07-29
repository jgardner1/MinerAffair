from mineraffair.vector import Vector
directions = set((
    'north', 'n',
    'south', 's',
    'east',  'e', 
    'west',  'w',
    'up',    'u',
    'down',  'd',
))

direction_abbreviations = {
    'n':'north',
    's':'south',
    'e':'east',
    'w':'west',
    'u':'up',
    'd':'down',
}

direction_vectors = {
    'north':Vector((0,1,0)),
    'south':Vector((0,-1,0)),
    'east': Vector((1,0,0)),
    'west': Vector((-1,0,0)),
    'up':   Vector((0,0,1)),
    'down': Vector((0,0,-1)),
}
