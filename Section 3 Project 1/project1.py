from datetime import datetime, timezone, timedelta
import itertools
import numbers
import unittest

class Account:

    _interest_rate = 0.05
    id_counter = itertools.count(100)
    _transaction_list = []
    _transaction_codes = {
        'deposit': 'D',
        'withdrawal': 'W',
        'interest': 'I',
        'rejected': 'X'
    }

    def __init__(self, first_name, last_name, time_offset = None, initial_balance=1000.00):
        self._account_num = next(Account.id_counter)
        self.first_name = first_name
        self.last_name = last_name
        if time_offset is not None:
            self._user_tz = timezone(timedelta(hours=time_offset))
        else:
            self._user_tz = timezone(timedelta())
        self._balance = self.validate_real_number(initial_balance, 0)
    
    @property
    def account_num(self):
        return self._account_num

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name("_first_name", value, "Last name string can't be empty")
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name("_last_name", value, "Last name string can't be empty")
    
    def validate_and_set_name(self, attr_name, value, error_msg):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f"{error_msg}")
        setattr(self, attr_name, str(value).strip())

    @property
    def user_tz(self):
        return self._user_tz
    
    @user_tz.setter
    def user_tz(self, tz_value):
        if not isinstance(tz_value, timezone):
            raise ValueError("Value must be a TimeZone object")
        else:
            self._user_tz = tz_value

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        amount = self.validate_real_number(amount, 0.01)
        
        self._balance += amount
        type = Account._transaction_codes['deposit']
        transaction = Transaction(type, self.account_num, self.current_dt_utc())
        self.add_transaction(transaction)

        return transaction.confirmation_num
    
    def withdrawal(self, amount):
        amount = self.validate_real_number(amount, 0.01)

        accepted = False
        if self.balance - amount < 0:
            type = Account._transaction_codes['rejected']
            print("Transaction falied - Insufficient funds")
        else:
            accepted = True
            type = Account._transaction_codes['withdrawal']

        transaction = Transaction(type, self.account_num, self.current_dt_utc())
        self.add_transaction(transaction)

        if accepted:
            self._balance -= amount
        
        return transaction.confirmation_num

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError("Interest rate must be a real number")
        if value < 0:
            raise ValueError("Interest rate must be positive")
        cls._interest_rate = value

    def apply_interest_rate(self):
        interest = self._balance * Account.get_interest_rate()
        type = Account._transaction_codes["interest"]
        transaction = Transaction(type, self.account_num, self.current_dt_utc())
        self.add_transaction(transaction)
        self._balance += interest

        return transaction.confirmation_num
    
    def current_dt_utc(self):
        return datetime.now(self.user_tz)
    
    @staticmethod
    def validate_real_number(value, min_number=None):
        if not isinstance(value, numbers.Real):
            raise ValueError("Withdrawal amount must be a real number")
        if value < min_number:
            raise ValueError(f"Withdrawal amount must be at least {min_number}")
        
        return value
    
    @classmethod
    def add_transaction(cls, transaction):
        cls._transaction_list.append(transaction)
    
    @classmethod
    def get_all_transactions(cls):
        return cls._transaction_list
    
    @classmethod
    def get_transaction_by_id(cls, id):
        for transaction in cls._transaction_list:
            if transaction.transaction_id == id:
                return transaction


class Transaction():
    _transaction_id_seed = 100000

    def __init__(self, type, account_num, time):
        self._type = type
        self._account_num = account_num
        self._time = time
        self._transaction_id = self.transaction_id_seed
        self._confirmation_num = self.generate_confirmation_num()

    @property
    def type(self):
        return self._type
    
    @property
    def account_num(self):
        return self._account_num

    @property
    def time(self):
        return self._time

    @property
    def transaction_id_seed(self):
        Transaction._transaction_id_seed += 1
        return self._transaction_id_seed
    
    @property 
    def transaction_id(self):
        return self._transaction_id
    
    @property 
    def confirmation_num(self):
        return self._confirmation_num
    
    def generate_confirmation_num(self):
        dt_str = self.time.strftime('%Y%m%d%H%M%S')
        return f"{self.type}-{self.account_num}-{dt_str}-{self.transaction_id}"


user1 = Account("Pavlo", "Kostiv", 2)
user2 = Account("Ivan", "Kostiv")

try:
    user1.first_name = "  "
except ValueError as ex:
    print(ex)

user2.last_name = "Abobich"

print(user1.first_name)
print(user2.last_name)

Account.set_interest_rate(0.1)
user1.apply_interest_rate()
user1.deposit(100)

user2.deposit(300.52)
user2.withdrawal(100)
user2.deposit(200)

user2.withdrawal(2000)

print(f"User1 balance: {user1.balance}")
print(f"User2 balance: {user2.balance}")

print(user1.user_tz)
print(user1.current_dt_utc())

for transaction in Account.get_all_transactions():
    print(f"Type: {transaction.type}, id: {transaction.transaction_id}, account id: {transaction.account_num}, time: {transaction.time.strftime('%Y-%m-%d, %H:%M:%S')}")

transaction = Account.get_transaction_by_id(100006)
print(f"id: {transaction.transaction_id}, account id: {transaction.account_num}, time: {transaction.time.strftime('%Y-%m-%d, %H:%M:%S')}")
print(f"confirmation number: {transaction.confirmation_num}")



#############
###testing###
#############

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account_number = 102
        self.first_name = "FIRST"
        self.last_name = "LAST"
        self.tz = 3
        self.balance = 100.00

    def create_account(self):
        return Account(self.first_name, self.last_name, self.tz, self.balance)

    def test_create_account(self):
        a = self.create_account()

        #self.assertEqual(account_number, a.account_num)
        self.assertEqual(self.first_name, a.first_name)
        self.assertEqual(self.last_name, a.last_name)
        self.assertEqual(timezone(timedelta(hours=self.tz)), a.user_tz)
        self.assertEqual(self.balance, a.balance)

    def test_create_account_blank_first_name(self):
        self.first_name = ""

        with self.assertRaises(ValueError):
            a = self.create_account()
    
    def test_create_account_blank_last_name(self):
        self.last_name = ""

        with self.assertRaises(ValueError):
            a = self.create_account()

    def test_create_account_negative_balance(self):
        self.balance = -500

        with self.assertRaises(ValueError):
            a = self.create_account()
    
    def test_account_withdrawal_ok(self):
        a = self.create_account()
        conf_num = a.withdrawal(100)

        self.assertTrue(conf_num.startswith('W-'))
        self.assertEqual(self.balance - 100, a.balance)
    
    def test_account_negative_withdrawal(self):
        a = self.create_account()

        with self.assertRaises(ValueError):
            conf_num = a.withdrawal(-100)
    
    def test_account_withdrawal_overdraw(self):
        a = self.create_account()
        conf_num = a.withdrawal(200)

        self.assertTrue(conf_num.startswith('X-'))
        self.assertEqual(self.balance, a.balance)
    
    def test_account_deposit_ok(self):
        a = self.create_account()
        conf_num = a.deposit(100)

        self.assertTrue(conf_num.startswith('D-'))
        self.assertEqual(self.balance+100, a.balance)
    
    def test_account_negative_deposit(self):
        a = self.create_account()

        with self.assertRaises(ValueError):
            conf_num = a.deposit(-100)
    
    def test_account_apply_interest_ok(self):
        a = self.create_account()
        conf_num = a.apply_interest_rate()

        self.assertTrue(conf_num.startswith('I-'))
        self.assertEqual(self.balance + self.balance * Account.get_interest_rate(), a.balance)


run_tests(TestAccount)