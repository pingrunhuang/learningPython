'''
this script can process a large file with multiple thread
however, we are going to compare processing with one thread and multiple thread
'''
from datetime import datetime
import time
from threading import Thread

def single_thread_process(file_path):
    with open(file=file_path) as f:
        start = datetime.now()
        for _ in f:
            # process
            pass
        print('Time elapsed using single thread:', datetime.now()-start)


class ProcessLine(Thread):
    def __init__(self, line):
        self.line = line
        super(ProcessLine, self).__init__()
    def run(self):
        # print(self.line)
        pass

def multiple_thread_process(file_path):
    threads = []
    with open(file=file_path) as f:
        start = datetime.now()
        for line in f:
            t = ProcessLine(line)
            t.daemon = True
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()
        print('Time elapsed using multiple thread:', datetime.now() - start)

single_thread_process('data/2014.csv')
multiple_thread_process('data/2014.csv')
