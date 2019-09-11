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
