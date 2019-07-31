from queue import Queue
from requests import get
import logging
from threading import Thread
"""
Ideas of using queue to implement multi-threaded pattern is to generate an accessible queue of tasks that could be 
processed by each thread and mark the task as done after finished.
--------------------------------- tasks
 ^      ^       ^       ^       ^ 
 |      |       |       |       |
 t1     t2      t3      t4      t5

 number of tasks > number of threads in this case 
"""

UNIVERSAL_QUEUE = Queue()
MAXIMUM_THREAD = 20

def worker(queue, result, func=get):
    """
    passing a reference of the queue and the reference of the result container to be updated 
    """
    while not queue.empty():
        # queue element is in the form of (index, task)
        work = queue.get()
        try:
            data = func(work[1])
            logging.info("Processing task {}".format(work[0]))
            # update the result container
            result[work[0]] = data
        except:
            logging.error("Error task {}".format(work[0]))
            result[work[0]] = {}
        # Used by Queue consumer threads.  For each get() used to fetch a task, 
        # a subsequent call to task_done() tells the queue that the processing on the task is complete.
        queue.task_done()

def threads_queue_main(tasks):
    """
    limit the number of tasks as a batch to be processed at a time
    """
    task_num = len(tasks)
    # initialize the universal queue
    for i in range(task_num):
        UNIVERSAL_QUEUE.put((i, tasks[i]))
    result = [{} for _ in tasks]
    num_thread = min(MAXIMUM_THREAD, task_num)
    for i in range(num_thread):
        logging.info("Start thread {}".format(i))
        thread = Thread(target=worker, args=[UNIVERSAL_QUEUE, result])
        # allow main thread to exit regardless of exception
        thread.setDaemon(True)
        thread.start()
    # for each element to join under the hood
    UNIVERSAL_QUEUE.join()
    logging.info("All tasks completed!")
    return result

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    urls = ["https://news.ycombinator.com/"] * 100
    result = threads_queue_main(urls)
    logging.info(result)