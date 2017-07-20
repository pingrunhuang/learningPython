import time
import random
from threading import Thread
from queue import Queue

MAX_SIZE_QUEUE = 10
queue = Queue(MAX_SIZE_QUEUE)

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('Produced:', num)
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get(0)
            queue.task_done()
            print('Consumed:', num)
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()



