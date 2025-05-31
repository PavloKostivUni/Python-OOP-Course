from datetime import datetime
from random import choice, seed

class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()
    
class Logger:
    current_time = TimeUTC()


print(Logger.current_time)
l = Logger()
print(l.current_time)


class Choice:
    def __init__(self, *choices):
        self.choices = choices
    
    def __get__(self, instance, owner_class):
        return choice(self.choices)

class Deck:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'23456789JQKA', '10')

class Dice():
    die_1 = Choice(1,2,3,4,5,6)
    die_2 = Choice(1,2,3,4,5,6)
    die_3 = Choice(1,2,3,4,5,6)
    
d = Deck()
seed(0)
for i in range(10):
    print(d.card, d.suit)

dice = Dice()
for i in range(10):
    print(dice.die_1, dice.die_2, dice.die_3)