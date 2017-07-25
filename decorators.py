# /usr/bin/python

# used for decorating with multiple decorators
from functools import wraps

def my_decorator(some_func):
    def wrapper_func(*args, **kwargs):
        print("the {} function has been decorated".format(some_func.__name__))
        return some_func
    return wrapper_func

def my_logger(some_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(some_func.__name__), level=logging.INFO)
    @wraps(some_func)
    def wrapper_func(*args, **kwargs):
        logging.info(msg='ran with args: {} and key word args: {}'.format(args, kwargs))
        return some_func(*args, **kwargs)
    return wrapper_func

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



# @my_decorator
# def helloworld():
#     return
#
# helloworld()

#
# @my_logger
# def display_info(name, info, phone=""):
#     print('display_info ran with arguments:({},{},{})'.format(name,info,phone))
#
# display_info("john",23,phone="4321")


@my_logger
@my_timer
def generator(count):
    for x in range(count):
        yield x
    # return (x for x in xrange(count))

generator(10000000)

@my_logger
@my_timer
def gen_list(count):
    my_list = []
    for x in range(count):
        my_list.append(x)
    return my_list
    # return [x for x in xrange(count)]

# actually this decorator syntac is equivilant to
# gen_list = my_timer(gen_list)


gen_list(10000000)