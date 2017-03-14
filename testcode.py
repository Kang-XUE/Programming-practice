from Vectorclass import Vector

a = Vector(1, 2, 3)
print a.v0
print a.length()
a.scale(3)
print a.v0
v = Vector(2, 8, 7)
print a.dot_product(v)
print a.cross_product(v).v0