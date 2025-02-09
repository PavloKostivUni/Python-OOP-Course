class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        print("__repr__ is called")
        return f"Person(name: {self.name}; age: {self.age})"
    
    def __str__(self):
        print("__str__ is called")
        return self.name

p = Person("Ivan", 30)

print(p)
print(str(p))
print(repr(p))


class Point():
    pass

class Line():
    pass

point = Point()
line = Line()

print(repr(point))
print(repr(line))