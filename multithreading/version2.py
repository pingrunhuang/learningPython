import time
import random
from threading import Thread, Condition

queue = []
condition = Condition()
class ProducerThread(Thread):
    def run(self):
        global queue
        nums = range(5)
        while True:
            condition.acquire()
            num = random.choice(nums)
            queue.append(num)
            print('Produced:',num)
            condition.notify()
            condition.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print('Nothing in the queue, consumer is waiting...')
                condition.wait()
                print('Producer added somehing to the queue and notified the consumer')
            num = queue.pop(0)
            print('Consume:', num)
            condition.release()
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()
