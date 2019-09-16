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


######################################## USAGE ########################################
class Manager3(metaclass=Singleton):
    """python3"""
    pass

class Manager2(object):
    """python2"""
    __metaclass__ = Singleton
