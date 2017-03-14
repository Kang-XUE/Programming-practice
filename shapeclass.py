class Shape(object):
    def area(self):
        raise NotImplementedError

class Rect (Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        if self.width > 0 and self.height > 0:
            area = self.width * self.height
            return area
        else:
            Shape.area(self)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius > 0:
            area = 3.14 * self.radius ** 2
            return area
        else:
            Shape.area(self)




