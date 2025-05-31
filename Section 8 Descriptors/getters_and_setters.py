from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'__get__ called in {self}')
            return datetime.utcnow().isoformat()

class Logger1:
    current_time = TimeUTC()

class Logger2:
    current_time = TimeUTC()

print(Logger1.current_time)
print(Logger2.current_time)

l1 = Logger1()
print(hex(id(l1)))
print(l1.current_time)
l2 = Logger1()
print(hex(id(l2)))
print(l2.current_time)


class Countdown:
    def __init__(self, start):
        self.start = start + 1
    
    def __get__(self, instance, owner):
        if isinstance is None:
            return self
        self.start -=1
        return self.start

class Rocket:
    countdown = Countdown(10)

rocket1 = Rocket()
rocket2 = Rocket()

print(rocket1.countdown)
print(rocket2.countdown)


class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')
    
    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
        else:
            print(f'__get__ called, instance={instance}, owner_class={owner_class}')

class Point2D:
    x = IntegerValue()
    y = IntegerValue()

print(Point2D.x)

p = Point2D()
print(p.x)

p.x=100