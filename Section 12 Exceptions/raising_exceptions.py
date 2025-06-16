ex = BaseException('a', 'b', 'c')

print(ex.args)
print(repr(ex))

try:
    raise ValueError('some message', 100, 200)
except ValueError as ex:
    print(ex.args)

def div(a, b):
    try:
        return a // b
    except ZeroDivisionError as ex:
        print('logging exception...', repr(ex))
        raise

#div(1, 0)

class CustomError(Exception):
    """a custom exception"""

def my_func(a,b):
    try:
        return a // b
    except ZeroDivisionError as ex:
        print('logging exception...', repr(ex))
        raise CustomError(*ex.args)
    
#my_func(1, 0)

try:
    raise ValueError('level 1')
except ValueError:
    try:
        raise TypeError('level 2')
    except TypeError:
        #raise KeyError('level 3')
        pass

try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            #raise ValueError('value error occured') from ex_1
            pass


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
                raise ConversionError(f'the type is inadmissible') from None
    except ValueError as ex:
        raise ConversionError(f'the value {val} cannot be converted to a bool: {ex}') from None
    else:
        return b
    
#print(make_bool('ABC'))