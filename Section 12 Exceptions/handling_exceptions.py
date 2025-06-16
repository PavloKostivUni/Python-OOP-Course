import json


try:
    raise ValueError('custom message', 'secondary message')
except ValueError as ex:
    print(ex)

def func_1():
    raise IndexError('bad value')

try:
    func_1()
except ValueError as ex:
    print('handling an value error', repr(ex))
except IndexError as ex:
    print('handling an index error', repr(ex))

try:
    raise ValueError('error')
except ValueError as ex:
    print('handling value exception', repr(ex))
except Exception as ex:
    print('handling exception', repr(ex))

try:
    raise ValueError()
except ValueError:
    print('handled error')
finally:
    print('running finally')

try:
    raise ValueError
except ValueError:
    print('value error')
else:
    print('no exception')

try:
    pass
except ValueError:
    print('value error...')
else:
    print('no exception')


json_data = """{
    "Alex": {"age": 18},
    "Bryan": {"age": 21, "city": "London"},
    "Guido": {"age": "unknown"},
    "Guido2": {"age": 22}
}"""

data = json.loads(json_data)
print(data)

class Person:
    __slots__ = 'name', '_age'

    def __init__(self, name):
        self.name = name
        self._age = None

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Invalid age")
        
    def __repr__(self):
        return f'Person((name={self.name}, age={self.age}))'
    
persons = []

for name, attributes in data.items():
    p = Person(name)

    for attrib_name, attrib_value in attributes.items():
        skip_person = False
        try:
            setattr(p, attrib_name, attrib_value)
        except AttributeError:
            print(f"Ignoring attribute: {name}.{attrib_name}={attrib_value}")
        except ValueError as ex:
            print(f'Data for Person({name}) contains an invalid attribute value: {ex}')
            skip_person = True
            break

    if not skip_person:
        persons.append(p)

print(persons)


def convert_int(val):
    if not isinstance(val, int):
        raise TypeError()
    if val not in {0, 1}:
        raise ValueError('Integer values 0 or 1 only')
    return bool(val)

def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()
    
    val = val.casefold()
    if val in {'0', 'f', 'false'}:
        return False
    if val in {'1', 't', 'true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False, 0, 1')

class ConversionError(Exception):
    pass

def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'the type is inadmissible')
    except ValueError as ex:
        raise ConversionError(f'the value {val} cannot be converted to a bool: {ex}')
    else:
        return b
    
values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)
    
    print(value, result)


def get_item_forgive_me(seq, idx, default = None):
    try:
        return seq[idx]
    except (IndexError, TypeError, KeyError):
        return default

def get_item_ask_perm(seq, idx, default = None):
    if hasattr(seq, '__getitem__'):
        if isinstance(seq, dict):
            return seq.get(idx, default)
        elif isinstance(idx, int):
            if idx < len(seq):
                return seq[idx]
    return default

print(get_item_forgive_me([1, 2, 3], 5, 'Nope'))
print(get_item_ask_perm([1, 2, 3], 2, 'Nope'))

print(get_item_forgive_me({'a': 100}, 'a'))
print(get_item_ask_perm({'a': 100}, 'a'))


class ConstantSequence:
    def __init__(self, val):
        self.val = val
    
    def __getitem__(self, idx):
        return self.val

seq = ConstantSequence(10)

print(get_item_forgive_me(seq, 2, 'Nope'))