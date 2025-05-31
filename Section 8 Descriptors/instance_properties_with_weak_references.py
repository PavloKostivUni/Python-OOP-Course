import weakref
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.values.get(id(instance))
            return value_tuple[1]
    
    def _remove_object(self, weak_ref):
        for key, value in self.values.items():
            if value[0] == weak_ref:
                del self.values[key]
                break

class Point:
    x = IntegerValue()

    def __init__(self, x):
        self.x = x
    
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x


p1 = Point(10.1)
p1_id = id(p1)
p2 = Point(23.123)

print(p1.x)
p1.x = 23.43
print(p1.x)

print(ref_count(p1_id))
print(Point.x.values)
del(p1)
print(ref_count(p1_id))
print(Point.x.values)


class ValidString:
    def __init__(self, min_length=0, max_length=255):
        self.data = {}
        self._min_length = min_length
        self._max_length = max_length
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        if len(value) < self._min_length:
            raise ValueError(f"Value must be at least {self._min_length} characters")
        if len(value) > self._max_length:
            raise ValueError(f"Value must not exceed {self._max_length} characters")
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), value)
    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.data.get(id(instance))
            return value_tuple[1]
    
    def _finalize_instance(self, weakref):
        for key, value in self.data.items():
            if value[0] == weakref:
                del self.data[key]
                break

class Person:
    __slots__ = '__weakref__'

    first_name = ValidString(1, 100)
    last_name = ValidString(1, 100)

    def __eq__(self, other):
        return (
            isinstance(other, Person) and
            self.first_name == other.first_name and
            self.last_name == other.last_name
        )

class BankAccount:
    __slots__ = '__weakref__'

    account_number = ValidString(5, 255)

    def __eq__(self, other):
        return (
            isinstance(other, BankAccount) and
            self.account_number == other.account_number
        )

p1 = Person()
p1_id = id(p1)
p1.first_name = 'Valera'
print(p1.first_name)

b1 = BankAccount()
b1.account_number = 'ABC123'
print(b1.account_number)

print(ref_count(p1_id))
print(Person.first_name.data)
del p1
print(ref_count(p1_id))
print(Person.first_name.data)