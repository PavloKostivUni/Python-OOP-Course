from numbers import Real
from math import sqrt
from functools import total_ordering


class VectorDimensionMismatch(TypeError):
    pass

class Vector:
    def __init__(self, components):
        if len(components) < 1:
            raise ValueError("You can't create an empty vector")
        
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f"Vector components must be real numbers. {component} is invalid")

        self._components = tuple(components)
    
    def __len__(self):
        return len(self.components)
    
    def __repr__(self):
        return f"Vector {self.components}"
    
    @property
    def components(self):
        return self._components
    
    def validate_type_and_dimension(self, other):
        return isinstance(other, Vector) and len(self) == len(other)

    def __add__(self, other):
        if not self.validate_type_and_dimension(other):
            raise VectorDimensionMismatch("Vectors must be of same dimension")
        components = tuple(x+y for x, y in zip(self.components, other.components))
        return Vector(components)
    
    def __sub__(self, other):
        if not self.validate_type_and_dimension(other):
            raise VectorDimensionMismatch("Vectors must be of same dimension")
        components = tuple(x-y for x, y in zip(self.components, other.components))
        return Vector(components)
    
    def __mul__(self, other):
        print("__mul__ is called")
        if isinstance(other, Real):
            components = tuple(x * other for x in self.components)
            return Vector(components)
        if self.validate_type_and_dimension(other):
            components = tuple(x * y for x, y in zip(self.components, other.components))
            return sum(components)
        return NotImplemented
    
    def __rmul__(self, other):
        print("__rmul__ is called")
        return self * other
    
    def __matmul__(self, other):
        print("__matmul__ is called")

    def __iadd__(self, other):
        print("__iadd__ is called")
        if self.validate_type_and_dimension(other):
            components = (x + y for x,y in zip(self.components, other.components))
            self._components = tuple(components)
            return self
        return NotImplemented

    def __neg__(self):
        components = (-x for x in self.components)
        components = tuple(components)
        return Vector(components)
    
    def __abs__(self):
        return sqrt(sum(x ** 2 for x in self.components))



v1 = Vector((10, 12))
v2 = Vector((5, 10))
v3 = Vector((5,12,3))

print(len(v1))
print(v1)
print(v2)
print(v3)

print(f"v1+v2: {v1+v2}")
print(f"v1-v2: {v1-v2}")

try:
    v1+v3
except TypeError as ex:
    print(ex)

print(f"v1*v2: {v1*v2}")
print(f"v1*5: {v1*5}")

print(f"v2*v1: {v2*v1}")
print(f"5*v1: {5*v1}")

print(f"v1@v2: {v1 @ v2}")

print(f"v1 id: {id(v1)}")
v1 += v2
print(f"v1+=v2: {v1}")
print(f"v1 id: {id(v1)}")

neg_v = -v1
print(f"v1: {v1}")
print(f"neg_v: {neg_v}")

abs_v = Vector((1,1,1,1))
print(f"abs(v): {abs(abs_v)}")



class Person():
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Person: {self.name}"

class Family():
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.kids = []
    
    def __iadd__(self, kid):
        if isinstance(kid, Person):
            self.kids.append(kid)
            return self
        raise ValueError("Kid must be a Person object")
    
    def __repr__(self):
        return f"Family:\nFather: {self.father}; mother: {self.mother}; \nKids: {list(kid.name for kid in self.kids)}"


f1 = Family('Ivan', 'Galyna')
kid1 = Person('Yurii')
kid2 = Person('Olga')

f1 += kid1
f1 += kid2

print(f1)


print("\n")
############################
######Rich Comparisons######
############################

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector(x={self.x};y={self.y})"
    
    def __eq__(self, other):
        if isinstance(other, tuple):
            new_vector = Vector(*other)
            return self.x == new_vector.x and self.y == new_vector.y 
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __abs__(self):
         return sqrt(self.x **2 + self.y **2)
    
    def __lt__(self, other):
        if isinstance(other, tuple):
            new_vector = Vector(*other)
            return abs(self) < abs(new_vector)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, tuple):
            new_vector = Vector(*other)
            return abs(self) > abs(new_vector)
        return NotImplemented
    
    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(2, 3)

print("__eq__:")
print(v1==v2)
print(v2==v3)
print(v1==(1,1))
print((1,1)==v1)
print(v1==(1,4))
print((1,1)!=v1)
print(v1!=(1,4))

print("__lt__:")
print(v1 < (1,2))
print(v1 < v3)
print(v3 < (1,2))
print(v3 < v1)
print(v2 < v1)
print(v3 > v1)
print(v3 > (1,2))

print("__le__:")
print(v1 <= (1,1))
print(v1 <= (1,0))
print(v1 <= (1,2))
print(v1 >= v2)
print(v1 >= (1,2))


@total_ordering
class Number():
    def __init__(self, num):
        self.num = num
    
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.num == other.num
        if isinstance(other, Real):
            return self.num == other
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Number):
            return self.num < other.num
        if isinstance(other, Real):
            return self.num < other
        return NotImplemented

a = Number(1)
b = Number(3)
c = Number(1)

print("total_ordering:")
print(a==b)
print(a==c)
print(a>b)
print(a>c)
print(a<b)
print(a<c)
print(a<=b)
print(a>=c)