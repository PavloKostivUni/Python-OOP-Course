class Location:
    __slots__ = 'name', '_longtitude', '_latitude'

    def __init__(self, name, *, longtitude, latitude):
        self.name = name
        self._longtitude = longtitude
        self._latitude = latitude
    
    @property
    def longtitude(self):
        return self._longtitude
    
    @property
    def latitude(self):
        return self._latitude


l1 = Location("Home", longtitude="45.45.45", latitude="23.23.23")
l1.name = "School"

print(l1.name)



class Person:
    __slots__ = 'name'

    def __init__(self, name):
        self.name = name


class Student(Person):
    __slots__ = 'age', 'student_id'

    def __init__(self, name, age, student_id):
        super().__init__(name)
        self.age = age
        self.student_id = student_id


p1 = Person("John")
s1 = Student("Chuck", 52, "1123124")
print(s1.student_id)


class Human:
    __slots__ = 'name', '__dict__'

    def __init__(self, name, age):
        self.name = name
        self.age = age


h1 = Human("Mike", 19)
print(h1.__dict__)