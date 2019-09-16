"""
the __new__() method is called before the __init__() method
it return a new object which could be the instance of the current class or an instance of other class

__init__ is going to set all the params and return nothing
"""

class Foo(object):
    def __init__(self):
        print("__init__() get invoked")
    def __new__(self, *args, **kwargs):
        # This method get invoked first
        print("__new__() get invoked")
        # only if an instance of Foo is returned will the __init__ method get invoked
        # instance = super(Foo, self).__new__(self, *args, **kwargs)
        instance = "asdf"
        return instance

if __name__ == "__main__":
    foo = Foo()