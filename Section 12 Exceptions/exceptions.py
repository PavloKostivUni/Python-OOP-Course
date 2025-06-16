l = [1, 2, 3]
ex = IndexError()

try:
    l[4]
except IndexError as ex:
    print(ex.__class__, ':', str(ex))

ex = ValueError('custom message')

print(str(ex), repr(ex))

def func_1():
    func_2()

def func_2():
    try:
        func_3()
    except ValueError:
        print('error occured - silencing it')

def func_3():
    ex = ValueError('some custom message')
    raise ex

func_1()


def square(seq, index):
    return seq[index] ** 2

def squares(seq, max_n):
    for i in range(max_n):
        try:
            yield square(seq, i)
        except IndexError:
            return

l = [1, 2, 3]
print(list(squares(l, 4)))