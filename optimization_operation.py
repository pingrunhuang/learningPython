from timeit import Timer

# dataset that is pretty huge
data = []


@Timer
def complex_func(index):
    return len(data[index])

# use cores
import multiprocessing
import timeit

NUM_CHUNK = 10
NUM_PROC = 4


pool = multiprocessing.Pool(NUM_PROC)
result = pool.map(complex_func, data)


# sparse matrix
import scipy.sparse as sp
import numpy as np
one_hot = np.array([1,0,0,0,0,1,1,0,0,0,0,0,0,1,0])
one_hot_sparse = sp.csc_matrix(one_hot)