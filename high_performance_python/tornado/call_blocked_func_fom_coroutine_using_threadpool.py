from concurrent.futures import ThreadPoolExecutor
from tornado import gen
from tornado.ioloop import IOLoop

# instantiate a pool with 2 threads
thread_pool = ThreadPoolExecutor(2)

def block_func(count):
    import time
    for _ in range(count):
        time.sleep(1)

@gen.coroutine
def call_blocking():
        print("Start")
        # submit method to call blocking method
        yield thread_pool.submit(block_func, 10)
        print("End")

if __name__ == "__main__":
        IOLoop.current().run_sync(lambda:call_blocking())