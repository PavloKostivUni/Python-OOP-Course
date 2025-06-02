from enum import Enum
from functools import total_ordering
from http import HTTPStatus


class Color(Enum):
    red = 1
    green = 2
    blue = 3

    def purecolor(self, value):
        return {self: value}
    
    def __str__(self):
        return f'{self.name} ({self.value})'
    
print(Color.red.purecolor(100), Color.blue.purecolor(255))

print(Color.red)


@total_ordering
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

    def __eq__(self, other):
        if isinstance(other, Number):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        return False

print(Number.ONE < Number.TWO)
print(Number.ONE == 1)
print(Number.ONE >= Number.ONE)


class Phase(Enum):
    READY = 'ready'
    RUNNING = 'running'
    FINISHED = 'finished'

    def __str__(self):
        return self.value
    
    def __eq__(self, other):
        if isinstance(other, Phase):
            return self is other
        elif isinstance(other, str):
            return self.value == other
        return False
    
    def __lt__(self, other):
        ordered_items = list(Phase)
        self_ordered_index = ordered_items.index(self)

        if isinstance(other, str):
            try:
                other = Phase(other)
            except ValueError:
                return False

        if isinstance(other, Phase):
            other_order_index = ordered_items.index(other)
            return self_ordered_index < other_order_index

print(Phase.READY)
print(Phase.READY < Phase.RUNNING)
print(Phase.READY < 'running')


class State(Enum):
    READY = 1
    BUSY = 0

    def __bool__(self):
        return bool(self.value)

print(bool(State.READY), bool(State.BUSY))

state = State.BUSY
if state:
    print('system is ready')
else:
    print('system is busy')


class ColorBase(Enum):
    def hello(self):
        return f'{str(self)} says hello!'

class Color1(ColorBase):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

print(Color1.BLUE.hello())


@total_ordering
class OderedEnum(Enum):
    """Create an ordering based on the member values.
    So member values have to support rich comparisons."""

    def __lt__(self, other):
        if isinstance(other, OderedEnum):
            return self.value < other.value
        return NotImplemented

class Number(OderedEnum):
    ONE = 1
    TWO = 2
    THREE = 3

class Dimension(OderedEnum):
    D1 = 1,
    D2 = 1, 1
    D3 = 1, 1, 1

print(Number.ONE < Number.TWO)
print(Dimension.D1 >= Dimension.D2)


print(list(HTTPStatus)[0:10])
print(HTTPStatus.NOT_FOUND.value, HTTPStatus.NOT_FOUND.name, HTTPStatus.NOT_FOUND.phrase)

class AppStatus(Enum):
    OK = (0, 'No problem!')
    FAILED = (1, 'Crap!')

    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)

        member._value_ = member_value
        member.phrase = member_phrase

        return member

print(AppStatus.OK.value, AppStatus.OK.name, AppStatus.OK.phrase)

print(AppStatus(1))


class TwoValueEnum(Enum):
    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)

        member._value_ = member_value
        member.phrase = member_phrase

        return member