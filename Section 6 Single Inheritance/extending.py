class Person:
    def routine(self):
        result = self.eat()
        if hasattr(self, 'study'):
            result += self.study()
        result += self.sleep()
        return result

    def eat(self):
        return "Person eats;"
    
    def sleep(self):
        return "Person sleeps;"

class Student(Person):
    def study(self):
        return 'study...' * 3


p1 = Person()
s1 = Student()

print(p1.routine())
print(s1.routine())



class Account:
    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Generic Account"
    
    def calc_interest(self):
        return f"Calculate interest on {self.account_type} with APR = {self.__class__.apr}"

class Savings(Account):
    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Savings Account"


a1 = Account(500, 1000)
s2 = Savings(501, 750)

s2.apr = 1000
print(a1.calc_interest())
print(s2.calc_interest())