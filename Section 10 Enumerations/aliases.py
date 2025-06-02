import enum

class NumSides(enum.Enum):
    Triangle = 3
    Rectangle = 4
    Square = 4
    Rhombus = 4

print(NumSides.Rectangle is NumSides.Square)
print(NumSides.Rhombus is NumSides.Square)

print(list(NumSides))
print(NumSides.Square in NumSides)

print(NumSides(4))
print(NumSides['Square'])
print(NumSides.__members__)


class Status(enum.Enum):
    ready = 'ready'

    running = 'running'
    busy = 'running'
    processing = 'running'

    ok = 'ok'
    finished_no_error = 'ok'
    ran_ok = 'ok'
    
    errors = 'errors'
    finished_with_errors = 'errors'
    errored = 'errors'

print(Status['busy'])


@enum.unique
class StatusUnique(enum.Enum):
    ready = 1
    done_ok = 2
    errors = 3