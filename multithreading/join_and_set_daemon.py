from threading import Thread
import time
main_thread = 10
sub_thread = 10

class MyThread(Thread):
    def __init__(self, id):
        super(MyThread, self).__init__()
        self.id = id

    def run(self):
        time.sleep(sub_thread)
        print(self.id)

def set_daemon_try():
    """
    if main_thread > sub_thread:
        id will be printed
    else:
        id won't be printed
    
    reason:
        set daemon will set the sub thread running in back, when the main thread is finished and the sub thread is not finished yet, the program will terminate the sub thread regardlessly
    """

    t = MyThread(999)
    t.setDaemon(True)
    t.start()
    time.sleep(main_thread)
    print("I am your father thread")

def join_try():
    """
    Using the join() function will wait for the finish of the sub thread 
    if join() is commented out:
        the main thread will keep on going and the whole program will get terminated after both threads are finished
    """

    t = MyThread(999)
    t.start()
    t.join()
    time.sleep(main_thread)
    print("I am your father thread")



def join_crawler_multithreading(iteration=500):
    """
    500 iterations only need 4s but some of the response is not valid which need to retry
    """
    import requests
    class SubThread(Thread):
        def __init__(self, group=None, target=None, name=None,
                    args=(), kwargs={}, Verbose=None):
            super(SubThread, self).__init__(group, target, name, args, kwargs)
            self._return = None
        def run(self):
            # print(type(self._target))
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)
        def join(self, *args):
            super(SubThread, self).join(*args)
            return self._return
    future_contract_endpoint = "https://www.okex.com/api/futures/v3/instruments"
    threads = []
    result = []
    start = time.time()
    for i in range(iteration):
        thread = SubThread(target=requests.get,name="Thread-{}".format(i), args=(future_contract_endpoint,))
        thread.start()
        threads.append(thread)

    for t in threads:
        result.append(t.join())
    duration = time.time() - start
    print("Duration 1: {}".format(duration))

def join_crawler_singlethreading(iteration=500):
    """
    500 times of iteration require 55s 
    """

    import requests
    result = []
    future_contract_endpoint = "https://www.okex.com/api/futures/v3/instruments"
    start = time.time()
    for _ in range(iteration):
        res = requests.get(future_contract_endpoint)
        result.append(res)
    duration = time.time() - start
    print("Duration 2: {}".format(duration))