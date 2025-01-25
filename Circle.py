import math

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            raise ValueError("Radius should be a positive and non-zero integer")
        self._area = None
    
    @property
    def area(self):
        if self._area == None:
            print("Area is being calculated...")
            self._area = math.pi * self.radius * self.radius
        return self._area

c = Circle(5)

print(c.radius)
print(c.area)
print(c.area)

c.radius = 6
print(c.radius)
print(c.area)
print(c.area)