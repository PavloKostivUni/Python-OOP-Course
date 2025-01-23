from types import MethodType

class Person:
  """Person class"""

  _gender = "Male"

  def __init__(self, value, name):
    self.salary = value
    self.name = name
  
  @property
  def name(self):
    """Person`s name property"""
    print("Name getter")
    return self._name
  
  @name.setter
  def name(self, value):
    print("Name setter")
    if isinstance(value, str) and len(value.strip()) > 0:
      self._name = value
    else:
      raise ValueError("Name must be a non-empty string")
  
  @name.deleter
  def name(self):
    print("Name deleter")
    del self._name
  
  gender = property(doc="Person`s gender property(set only)")

  @gender.setter
  def gender(self, gender):
    print("Gender setter")
    self._gender = gender


p = Person(1000, "dimon")

print(p.name)
p.name = "pavlo"
print(p.name)

p.gender = "Female"

print(p.__dict__)

print(help(Person))