class IntegerValue:
    def __set__(self, instance, value):
        print('__set__ called...')
    
    def __get__(self, instance, owner_class):
        print('__get__ called...')

class Point:
    x = IntegerValue()


p = Point()
p.x = 100
p.__dict__['x'] = 'Hello'
print(p.x)
print(p.__dict__)


class TimeUTC:
    def __get__(self, instance, owner_class):
        print('__get__ called...')

class Logger:
    current_time = TimeUTC()

l = Logger()

print(l.current_time)
l.__dict__['current_time'] = 'hello'

print(l.current_time)
print(l.__dict__)


class ValidString:
    def __init__(self, min_length=None):
        self.min_length = min_length
    
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} not long enough')
        instance.__dict__[self.property_name] = value
    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        print(f'calling __get__ for {self.property_name}')
        return instance.__dict__.get(self.property_name, None)

class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)


person = Person()
person.first_name = 'Alex'

print(person.__dict__)
print(person.first_name)