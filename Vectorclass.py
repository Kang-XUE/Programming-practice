class Vector (object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.v0 = [self.x, self.y, self.z]

    def length(self):
        l = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return l

    def scale(self, factor):
        self.x = self.x * factor
        self.y = self.y * factor
        self.z = self.z * factor
        self.v0 = [self.x, self.y, self.z]

    def dot_product(self, v):
        dprdt = self.x * v.x + self.y * v.y + self.z * v.z
        return dprdt

    def cross_product(self, v):
        cprdtx = self.y * v.z - self.z * v.y
        cprdty = self.z * v.x - self.x * v.z
        cprdtz = self.x * v.y - self.y * v.x
        cprdt = Vector(cprdtx,cprdty,cprdtz)
        return cprdt
