import ctypes
import weakref


def ref_count(address):
    return ctypes.c_long.from_address(address).value

class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'Person(name={self.name})'


p1 = Person("Guido")
p1_id = id(p1)
p2 = p1

del(p2)
print(ref_count(p1_id))

weak1 = weakref.ref(p1)
print(ref_count(p1_id))
print(weak1)

del(p1)
print(weak1)

p2 = Person('Valera')
d1 = weakref.WeakKeyDictionary()
d1[p2] = 'Valera'

d2 = weakref.WeakKeyDictionary()
d2[p2] = 'Valera'

print(ref_count(id(p2)))
print(weakref.getweakrefcount(p2))
print(p2.__weakref__)

print(d1.keyrefs())
del(p2)
print(d1.keyrefs())