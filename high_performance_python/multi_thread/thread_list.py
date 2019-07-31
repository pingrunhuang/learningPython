import threading
import time 
from queue import Queue
"""
Pattern:
1. worker function 
2. launcher 

number of tasks == number of threads in this case 
"""

def worker(worker_id,duration):
    print("Start {}".format(worker_id))
    time.sleep(duration)
    print("Finished {}".format(worker_id))

def threads_list_main(task_num):
    threads = []
    for i in range(task_num):
        thread = threading.Thread(target=worker, args=[i, 5])
        thread.start()
        threads.append(thread)
    # joining all of the started thread to ensure of the task in thread get finished
    # essentailly pause the calling of thread
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    threads_list_main(1000)