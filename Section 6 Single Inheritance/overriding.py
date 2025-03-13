class Shape:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        return f'Shape.info called for {self.name}'

    def extended_info(self):
        return f'Shape.extended_info called for {self.name}', self.info

class Polygon(Shape):
    def __init__(self, name):
        self.name = name
    
    def info(self):
        return f'Polygon info called for {self.name}'


p = Polygon('square')

print(p.extended_info())



class Person:
    def __str__(self):
        print('Person.__str__ is called')
        return self.__repr__()
    
    def __repr__(self):
        return str(hex(id(self)))

class Student(Person):
    def __repr__(self):
        return 'Student.__repr__ is called'

s = Student()

print(s)