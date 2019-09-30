"""
Programs that are designed to read or modify itself is metaprogramming

Go through some usage of type

Use case
1. Domain restriction of values
2. Implicit conversion of values to custom classes (you might want to hide all of these complexities from users writing the class)
3. Enforcing different naming conventions and style guidelines (like “every method should have a docstring”)
4. Adding new attributes to a class
"""

# 2 ways of creating a new class 
class RandomClass:
    pass
clazz = type("RandomClass", (), {})
print(type(clazz) == type(RandomClass))


class ParentClass:
    pass
class ChildClass(ParentClass):
    some_var = 1
    def say_hi(self):
        print("Hello!")

def say_hi():
    print("Hello!")
p_class = type("ParentClass", (), {})
c_class = type("ChildClass", (p_class,), {"some_var":1, "say_hi": say_hi})
print(type(c_class) == type(ChildClass))


############################### change to snake style with metaclass in python ###########################################
def camel_to_snake(name):
    import re
    s1 = re.sub("(.)([A-Z][a-z]+)", r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class SnakeCaseMetaclass(type):
    def __new__(cls, name, parents, attrs):
        snake_case_attrs = {}
        for name, val in attrs.items():
            snake_case_attrs[camel_to_snake(name)] = val
        return type(name, parents, snake_case_attrs)

class SomeClass(metaclass=SnakeCaseMetaclass):
    someAttr = 5

someCls = SomeClass()
# print(someCls.some_attr)


################################################ Singleton with metaclass ################################################

import threading

class Singleton(type):
    """Singleton is a metaclass which combine Singleton Mode with Abstract Base Class"""

    def __init__(cls, name, bases, attrs):
        super(Singleton, cls).__init__(name, bases, attrs)
        cls._instance = None
        cls._lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Manager3(metaclass=Singleton):
    """python3"""
    pass

class Manager2(object):
    """python2"""
    __metaclass__ = Singleton




from abc import ABCMeta, abstractclassmethod
# a base wrapper for decorator class 
class BaseWrapper(metaclass=ABCMeta):
    @abstractclassmethod
    def __call__(self, func):
        pass


############################################# Registration of classes #######################################################

handlers = {}
class CustomMetaClass(type):
    # when a class get defined, this method will get called just like an object get initialized, the __new__() method get called
    def __new__(matacls, name, parents, attrs):
        custom_cls = type.__new__(matacls, name, parents, attrs)
        for ext in attrs['formats']:
            handlers[ext] = custom_cls
        return custom_cls

class Handler(metaclass=CustomMetaClass):
    formats = set()

class ImageHandler(Handler):
    formats = "jpeg", "png"

class AudioHandler(Handler):
    formats = "mp3", "wav"

print(handlers)