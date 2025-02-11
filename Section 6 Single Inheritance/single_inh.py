class Shape:
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Polygon(Shape):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Triangle(Polygon):
    pass


print(issubclass(Ellipse, Shape))
print(issubclass(Circle, Shape))
print(issubclass(Polygon, Ellipse))

s = Shape()
e = Circle()
sq = Square()
p = Polygon()

print(isinstance(s, Shape))
print(isinstance(sq, Rectangle))

print(isinstance(sq, type(p)))