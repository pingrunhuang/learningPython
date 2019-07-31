import math
from multiprocessing import managers
from multiprocessing.pool import Pool
import multiprocessing
from multiprocessing import Process
import time

FLAG_ALL_DONE = b'WORK_FINISHED'
FLAG_WORKER_FINISHED_PROCESSING = b'WORKER_FINISHED_PROCESSING'
'''
def check_prime(n):
    if n%2==0:
        return False
    from_i = 3
    to_i = math.sqrt(n) + 1
    for i in range(from_i, int(to_i), 2):
        if n%i==0:
            return False
    return True
'''

def check_prime(possible_primes_queue, definite_primes_queue):
    while True:
        n = possible_primes_queue.get()
        if n == FLAG_ALL_DONE:
            definite_primes_queue.put(FLAG_WORKER_FINISHED_PROCESSING)
        else:
            if n%2==0:
                continue
            for i in range(3, int(math.sqrt(n)+1), 2):
                if n % i == 0:
                    break
            definite_primes_queue.put(n)
        

def start():
    primes = []
    possible_primes_queue = managers.queue.Queue()
    definite_primes_queue = managers.queue.Queue()
    
    NUMBER_PROCESSES = 2
    pool = Pool(NUMBER_PROCESSES)
    processes = []
    for _ in range(NUMBER_PROCESSES):
        p = multiprocessing.Process(target=check_prime, args=(possible_primes_queue, definite_primes_queue))
        processes.append(p)
        p.start()

    t1 = time.time()
    number_range = range(100000000, 101000000)
    for possible_prime in number_range:
        possible_primes_queue.put(possible_prime)
    
    for _ in range(NUMBER_PROCESSES):
        possible_primes_queue.put(FLAG_ALL_DONE)

    # start consuming
    processes_indicating_they_have_finished = 0
    while True:
        new_result = definite_primes_queue.get()
        if new_result == FLAG_WORKER_FINISHED_PROCESSING:
            processes_indicating_they_have_finished+=1
            if processes_indicating_they_have_finished == NUMBER_PROCESSES:
                break
        else:
            primes.append(new_result)
    
    assert processes_indicating_they_have_finished == NUMBER_PROCESSES

    print("Took, {}".format(str(time.time()-t1)))
    print(len(primes), primes[:10], primes[-10:])
    
if __name__=='__main__':
    start()