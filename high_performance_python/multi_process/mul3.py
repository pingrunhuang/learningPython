from multiprocessing import Pool
import numpy
from time import time

'''
Used for:
launching different tasks in parallel
launching tasks with more than one argument
better control of task distribution
'''


ITERATE_NUM = 10000

def sqrt_mul():
    start   = time()
    pool    = Pool()
    results = [pool.apply_async(numpy.sqrt, (x,)) for x in range(ITERATE_NUM)]
    roots   = [r.get() for r in results]
    end     = time()
    print(len(roots))
    print("Time consuming using multiprocessing:{}".format(end -start))

def sqrt_sing():
    start   = time()
    results = [numpy.sqrt(i) for i in range(ITERATE_NUM)]
    end     = time()
    print(len(results))
    print("Time consuming using single process:{}".format(end -start))

if __name__ == "__main__":
    sqrt_mul()
    sqrt_sing()