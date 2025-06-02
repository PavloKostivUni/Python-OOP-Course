import enum
import random

random.seed(0)

class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            new_value = random.randint(1, 100)
            if new_value not in last_values:
                return new_value

    a = enum.auto()
    b = enum.auto()
    c = enum.auto()
    d = enum.auto()

for member in State:
    print(member.name, member.value)

class StateStr(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()

    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()

for member in StateStr:
    print(member.name, member.value)


class NameAsString(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

class Enum1(NameAsString):
    A = enum.auto()
    B = enum.auto()

print(list(Enum1))


class StateObj(enum.Enum):
    """User won't be able to use values"""
    Waiting = object()
    Running = object()
    Finished = object()

class Aliased(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(f'count={count}')
        if count % 2 == 1:
            #make this member an alias of the previous one
            return last_values[-1]
        else:
            return last_values[-1] + 1
    
    GREEN = 1
    GREEN_ALIAS = 1
    RED = 10
    CRIMSON = enum.auto()
    BLUE = enum.auto()
    AQUA = enum.auto()

print(list(Aliased))


class AliasedBase(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return last_values[-1]

class Color(AliasedBase):
    RED = object()
    CRIMSON = enum.auto()
    CARMINE = enum.auto()

    BLUE = object()
    AQUAMARINE = enum.auto()
    AZURE = enum.auto()

print(list(Color))