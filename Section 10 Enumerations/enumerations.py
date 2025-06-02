import enum

class Color(enum.Enum):
    red = 1
    green = 2
    blue = 3

class Status(enum.Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'

class UnitVectir(enum.Enum):
    V1D = (1, )
    V2D = (1, 1)
    V3D = (1, 1, 1)

print(Status.PENDING)
print(Status.PENDING.name, Status.PENDING.value)

class Constants(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3

print(Constants.ONE.value < Constants.TWO.value)
print(Status('pending'))
print(Status['PENDING'])

for member in Status:
    print(repr(member))

print(list(Status))


class Person():
    __hash__ = None

class Family(enum.Enum):
    person_1 = Person()
    person_2 = Person()

print(Family.person_1)


class EnumBase(enum.Enum):
    pass

class EnumExt(EnumBase):
    TWO = 2


def is_member(en, name):
    return getattr(en, name, None) is not None

print(is_member(Status, 'PENDING'))
print(is_member(Status, 'OK'))

print(Status.__members__)
print('PENDING' in Status.__members__)