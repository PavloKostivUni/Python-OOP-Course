class Person:
  name = "anton"

  def __init__(self, name, age):
    Person.name = name
    self.age = age

  def __str__(self):
    return "Hello I'm a Person"

  @staticmethod
  def myfunc(cls):
    print("Hello my name is" + cls.name)

p1 = Person("John", 36)
p1.myfunc(Person)
print(Person)
print(p1)