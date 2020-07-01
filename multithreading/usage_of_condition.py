from threading import Condition, Lock
import time

lock = Lock()
con = Condition(lock)
container = []

def has_element():
    if container:
        return True
    return False

def consumer():
    con.wait_for(has_element)
    ele = container.pop()
    print(ele)

def producer():
    with con.acquire():
        container.append("hello")
    time.sleep(2)

