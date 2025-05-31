'''
class IntegerValue:
    def __init__(self, name):
        self.storage_name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

class Point1D:
    x = IntegerValue('x')

p1, p2, = Point1D(), Point1D()

p1.x = 52
p2.x = 10.2

print(p1.x, p2.x)

class Point2D:
    x = IntegerValue('x')
    y = IntegerValue('y')

p2d1 = Point2D()
p2d1.x = 10.5
p2d1.y = 15.2

p2d2 = Point2D()
p2d2.x = 103.5
p2d2.y = 135.2

print(p2d1.x, p2d1.y)
print(p2d2.x, p2d2.y)
print(p2d1.__dict__)
'''

class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.values.get(instance, None)

class Point2D:
    x = IntegerValue()
    y = IntegerValue()


p1 = Point2D()
p2 = Point2D()

p1.x = 10.1
p1.y = 20.2
print(p1.x, p1.y)

import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

id_p1 = id(p1)
print(ref_count(id_p1))