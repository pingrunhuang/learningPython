import threading
import time

def wait_and_print(msg):
    time.sleep(1)
    print(msg)

def async_wait_and_print(msg):
    timer = threading.Timer(1, lambda: print(msg))
    timer.start()

start = time.time()
# wait_and_print(1)
# wait_and_print(2)
# wait_and_print(3)
# print('async:')
async_wait_and_print(1)
async_wait_and_print(2)
async_wait_and_print(3)
print("Duration: {}".format(time.time()-start))