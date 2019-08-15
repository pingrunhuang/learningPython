# /usr/bin/python

"""
used for decorating with multiple decorators
@ is equal to func=decorator(func) which is essentially creating a new function
"""

from functools import wraps

########################################## Basic usage ##########################################

# without wraps
def my_decorator(some_func):
    def wrapper_func(*args, **kwargs):
        print("the {} function has been decorated".format(some_func.__name__))
        return some_func
    return wrapper_func

@my_decorator
def helloworld():
    return
helloworld()

########################################## With or without wraps ##########################################

# with wraps: all informations like function name, docstring, arguments list, etc inside the some_func are copied
def my_logger_with_wraps(some_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(some_func.__name__), level=logging.INFO)
    @wraps(some_func)
    def wrapper_func(*args, **kwargs):
        logging.info(msg='ran with args: {} and key word args: {}'.format(args, kwargs))
        return some_func(*args, **kwargs)
    return wrapper_func

def my_logger_without_wraps(some_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(some_func.__name__), level=logging.INFO)
    def wrapper_func(*args, **kwargs):
        logging.info(msg='ran with args: {} and key word args: {}'.format(args, kwargs))
        return some_func(*args, **kwargs)
    return wrapper_func


@my_logger_with_wraps
def display_info1(name, info, phone=""):
    """
    my display docstring 1
    """
    print('display_info 1 ran with arguments:({},{},{})'.format(name,info,phone))

@my_logger_without_wraps
def display_info2(name, info, phone=""):
    """
    my display docstring 2
    """
    print('display_info 2 ran with arguments:({},{},{})'.format(name,info,phone))

def compare_with_wraps_and_without_wraps():
    display_info1("john",23,phone="4321")
    display_info2("marry",24)
    print(display_info1.__doc__)
    # note that this will return None which means the docstring is not copied
    print(display_info2.__doc__)


############################### which one get executed first if 2 decorators ###############################
""" Conclusions:
If both don't use the @wraps decorator, it is stacked
The strange thing is if both use @wraps, the executed sequence are the same
Don't know why
"""

def my_timer(some_func):
    import time
    @wraps(some_func)
    def wrapper_func(*args, **kwargs):
        t1=time.time()
        result = some_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} Ran in {} sec.".format(some_func.__name__, t2))
        return result
    return wrapper_func

@my_timer
@my_logger_with_wraps
def gen_list1(count):
    my_list = []
    for x in range(count):
        my_list.append(x)
    return my_list

@my_logger_with_wraps
@my_timer
def gen_list2(count):
    my_list = []
    for x in range(count):
        my_list.append(x)
    return my_list


########################################## Decorator for dp programming ##########################################
import functools
def memoize(func):
    memo = dict()
    @functools.wraps(func)
    def inner(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return inner

@memoize
def nsum(n):
    assert n>=0
    return 0 if n == 0 else nsum(n-1) + n 

@memoize
def fibonacci(n):
    assert n>=0
    return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)


############################# How to manipulate extra actions on an existing class  ###############################
class TestClass:
    def __init__(self):
        print("{} instanciated!".format(TestClass.__name__))

def addToClass(cls):
    def decorator(some_func):
        setattr(cls, some_func.__name__, some_func)
        return some_func
    return decorator

def test_class_decorator():
    # self refers to the instance of TestClass
    @addToClass(TestClass)
    def hello(self):
        print("hello world")

    t = TestClass()
    t.hello()

if __name__ == "__main__":
    from timeit import Timer
    measure = [
        {'exec': 'fibonacci(100)','import':'fibonacci', 'func':fibonacci},
        {'exec': 'nsum(200)', 'import':'nsum', 'func':nsum}
    ]
    for m in measure:
        t = Timer(stmt=m["exec"], setup="from __main__ import {}".format(m["import"]))
        print("name: {}, doc: {}, executing: {}, time: {}".format(m["func"].__name__, m["func"].__doc__, m["exec"], t.timeit()))

    # compare_with_wraps_and_without_wraps()

    gen_list1(100)
    gen_list2(100)

    test_class_decorator()