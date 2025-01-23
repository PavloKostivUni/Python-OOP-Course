from types import MethodType

class Person:
  """Person class"""

  gender = "Male"

  def __init__(self, value, name):
    self.salary = value
    self.name = name
  
  def get_name(self):
    print("Name getter")
    return self._name
  
  def set_name(self, value):
    print("Name setter")
    if isinstance(value, str) and len(value.strip()) > 0:
      self._name = value
    else:
      raise ValueError("Name must be a non-empty string")
  
  def del_name(self):
    print("Name deleter")
    del self._name
  
  name = property(fget=get_name, fset=set_name, fdel=del_name, doc="Person`s name property")

  def say_hello(self):
    print(f"Hello from {self.gender}")
  
  def register_method(self, func, name):
    setattr(self, name, MethodType(func, self))


p = Person(1000, "dimon")
print(f"salary: {p.salary}")
p.gender = "Female"


def say_hello(self):
  print(f"Hello from {self.gender} in a new function")

p.register_method(say_hello, "sa_hello")

Person.say_hello(Person)
p.sa_hello()


print(p.name)
p.name = "pavlo"
print(p.name)