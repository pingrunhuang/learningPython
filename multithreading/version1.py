import random
import time
from threading import Thread, Lock

queue = []
lock = Lock()


class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            lock.acquire()
            queue.append(num)
            print("Produced:", num)
            lock.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            lock.acquire()
            if not queue:
                print('Queue is empty now, but consumer will try to consume')
            num = queue.pop(0)
            print('Consumed:', num)
            lock.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()