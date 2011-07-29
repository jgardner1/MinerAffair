class Vector(tuple):

    def __add__(self, other):
        if len(other) != len(self):
            raise ValueError("Cannot add vectors of different length")
        return Vector(map(lambda x,y: x+y, self, other))

    def __sub__(self, other):
        if len(other) != len(self):
            raise ValueError("Cannot subtract vectors of different length")
        return Vector(map(lambda x,y: x-y, self, other))

    def __neg__(self):
        return Vector(map(lambda x: -x, self))

    def dot(self, other):
        return sum(map(lambda x,y: x*y, self, other))

    def __repr__(self):
        return "Vector(%s)" % (tuple.__repr__(self),)
