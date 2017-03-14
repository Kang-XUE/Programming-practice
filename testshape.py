from shapeclass import Shape,Rect,Circle

myshapes = [
    Rect(1.0, 2.0),
    Rect(2.0, 4.0),
    Circle(5.0),
]

sum_shapes = 0.0
for shape in myshapes:
    sum_shapes += shape.area()
print sum_shapes