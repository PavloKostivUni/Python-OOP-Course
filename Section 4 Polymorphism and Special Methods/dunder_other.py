from functools import partial
from collections import defaultdict
from time import perf_counter
from functools import wraps
from time import sleep
from datetime import datetime, date


############################
########### Hash ###########
############################
print("Hash:")

class Person():
    def __init__(self, name):
        self._name = name
    
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __repr__(self):
        return f"Person: {self.name}"
    
    @property
    def name(self):
        return self._name


p1 = Person("Michael")
p2 = Person("Michael")
p3 = Person("Pavlo")

print(hash(p1))
print(hash(p2))
print(hash(p3))

p_dict = {p1: p1.name}
print(p_dict)

############################
########### Bool ###########
############################
print("Bool:")

class MyList():
    def __init__(self, length):
        self._length = length
    
    @property
    def length(self):
        return self._length
    
    def __len__(self):
        return self._length
    
    def __bool__(self):
        return self._length > 0
    

ml1 = MyList(0)
ml2 = MyList(5)

print(bool(ml1))
print(bool(ml2))

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __bool__(self):
        return self.x !=0 or self.y != 0

p1 = Point(1,1)
p2 = Point(0,0)

print(bool(p1))
print(bool(p2))

############################
########### Call ###########
############################
print("\nCall:")

class Person():
    def __init__(self, name):
        self.name = name
    
    def __call__(self, *args):
        return self.name, *args

p1 = Person("Ivan")
print(p1(5, "Work"))

def abc_func(a, b, c):
    return a+b+c

partial_func = partial(abc_func, 15, 5)

print(partial_func(32))

class MyPartial():
    def __init__(self, func, *args):
        self._func = func
        self._args = args
    
    def __call__(self, *args):
        return self._func(*self._args, *args)


my_partial_func = MyPartial(abc_func, 52, 36)
print(my_partial_func(14))


class DefaultValue():
    def __init__(self, default_value):
        self._default_value = default_value
        self.counter = 0
    
    def __call__(self):
        self.counter += 1
        return self._default_value

def1 = DefaultValue("no")
def2 = DefaultValue(None)

d1 = defaultdict(def1)
d2 = defaultdict(def2)
d1['a'] = 100
print(d1["a"])
print(d1["b"])
print(f"Counter: {def1.counter}")
print(d2["a"])
print(d2["b"])
print(f"Counter: {def2.counter}")


def profiler(fn):
    _counter = 0
    _total_elapsed = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal _counter
        nonlocal _total_elapsed
        _counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        _total_elapsed += (end-start)
        return result
    
    def counter():
        return _counter
    
    def total_elapsed():
        return _total_elapsed
    
    def avg_time():
        return _total_elapsed / _counter
    
    inner.counter = counter
    inner.total_elapsed = total_elapsed
    
    return inner

@profiler
def time_fn():
    #sleep(0.5)
    pass

@profiler
def time_fn():
    #sleep(1)
    pass

time_fn()
print(time_fn.counter())


class Profiler:
    def __init__(self, fn):
        self._counter = 0
        self._total_elapsed = 0
        self._fn = fn
    
    def __call__(self, *args, **kwargs):
        self._counter += 1
        start = perf_counter()
        result = self._fn(*args, **kwargs)
        end = perf_counter()
        self._total_elapsed += (end-start)
        return result
    
    @property
    def avg_time(self):
        return self._total_elapsed / self._counter


@Profiler
def fn_1(a):
    #sleep(1)
    return a

fn_1(5)
print(fn_1("Hello"))

print(f"Counter: {fn_1._counter}")
print(f"Total time: {fn_1._total_elapsed}")
print(f"Average time: {fn_1.avg_time}")

############################
########## format ##########
############################
print("\nFormat".upper())

a = 0.1
print(format(a, ".20f"))

now = datetime.today()
print(format(now, "%Y-%m-%d %H:%M:%S"))

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return f"Person(name = {self.name}, dob = {self.dob.isoformat()})"
    
    def __str__(self):
        return f"Person({self.name})"
    
    def __format__(self, format_spec):
        print("__format__ called...")
        dob = format(self.dob, format_spec)
        return f"Person(name = {self.name}, dob = {dob})"

p = Person("Bob", date(2005, 3, 25))
print(repr(p))
print(format(p, "%B %d, %Y"))
    

############################
########### del  ###########
############################
print(str.upper("\nDelete"))

import ctypes
import sys

def ref_count(adress):
    return ctypes.c_long.from_address(adress).value

class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Person's name: {self.name}"

    def __del__(self):
        raise ValueError(f"__del__ called for {self}")
        #print(f"__del__ called for {self}")
    
    def gen_ex(self):
        raise ValueError("Some error")


p = Person("Mike")
p_id = id(p)

try:
    p.gen_ex()
except ValueError as ex:
    error = ex

print(error)

print(ref_count(p_id))
del p
print(ref_count(p_id))
del error
print(ref_count(p_id))

class ErrToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stdderr = sys.stderr
    
    def __enter__(self):
        self._file = open(self._fname, "w")
        sys.stderr = self._file
    
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stderr = self._current_stdderr
        if self._file:
            self._file.close()
        return False


p2 = Person("Ivan")

with ErrToFile("err.txt"):
    del p2

print("Program end")