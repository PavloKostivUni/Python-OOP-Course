class BaseValidator:
    def __init__(self, min_value=None, max_value=None):
        self._min_value = min_value
        self._max_value = max_value
    
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)
    
    def validate(self, value):
        pass
    
    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.property_name] = value


class IntegerField(BaseValidator):
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.property_name} must be {self.__class__.__name__}")
        if self._min_value is not None and value < self._min_value:
            raise ValueError(f"{self.property_name} must be bigger then {self._min_value}")
        if self._max_value is not None and value > self._max_value:
            raise ValueError(f"{self.property_name} must be less then {self._max_value}")
    
class CharField(BaseValidator):
    def __init__(self, min_value=0, max_value=255):
        min_value = min_value or 0
        self._min_value = max(min_value, 0)
        self._max_value = max_value
    
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.property_name} must be {self.__class__.__name__}")
        if self._min_value is not None and len(value) < self._min_value:
            raise ValueError(f"{self.property_name} must be at least {self._min_value} characters")
        if self._max_value is not None and len(value) > self._max_value:
            raise ValueError(f"{self.property_name} must be less then {self._max_value} characters")


class Person():
    name = CharField(1, 10)
    bio = CharField()
    age = IntegerField(0, 100)
    favorite_number = IntegerField()


p1 = Person()

try:
    p1.age = -4
except ValueError as ex:
    print(ex)

p1.age = 15
p1.favorite_number = 333

try:
    p1.name = ""
except ValueError as ex:
    print(ex)

p1.name = "Pavlo"
p1.bio = "Hello"

print(p1.age)

print(p1.__dict__)
