class Person:
    def work(self):
        return f"{self.__class__.__name__} works"
    
class Student(Person):
    def work(self):
        result = super().work()
        return f"{self.__class__.__name__} studies and {result}"

class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f"{self.__class__.__name__} codes and {result}"


p1 = Person()
s1 = Student()
py1 = PythonStudent()

print(p1.work())
print(s1.work())
print(py1.work())


from math import pi
from numbers import Real 

class Circle:
    def __init__(self, radius):
        self.set_radius(radius)
    
    @property
    def radius(self):
        return self._radius
    
    def set_radius(self, radius):
        if isinstance(radius, Real) and radius > 0:
            self._radius = radius
            self._area = None
            self._perimeter = None
        else:
            raise ValueError('Radius must be a positive real number')
    
    @radius.setter
    def radius(self, radius):
        self.set_radius(radius)
    
    @property
    def area(self):
        if self._area == None:
            self._area = pi * self.radius ** 2
        return self._area
    
    @property
    def perimeter(self):
        if self._perimeter == None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)
    
    @property
    def radius(self):
        return super().radius


c1 = Circle(1)

print(c1.radius)
print(c1.perimeter)
print(c1.area)

c1.radius = 2
print(c1.radius)
print(c1.perimeter)
print(c1.area)

uc1 = UnitCircle()
print(uc1.radius)
print(uc1.perimeter)
print(uc1.area)