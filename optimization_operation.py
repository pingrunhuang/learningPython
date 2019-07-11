import time
from functools import wraps
import scipy.sparse as sp
import numpy as np
import multiprocessing
import numba
import cython

def timing(func):
    @wraps(func)
    def call(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time()-start)
        return result
    return call


# dataset that is pretty huge
data = []

def complex_func(index):
    return len(data[index])

# use cores

NUM_CHUNK = 10
NUM_PROC = 4


pool = multiprocessing.Pool(NUM_PROC)
result = pool.map(complex_func, data)


# sparse matrix
one_hot = np.array([1,0,0,0,0,1,1,0,0,0,0,0,0,1,0])
one_hot_sparse = sp.csc_matrix(one_hot)

@timing
def matrix_sum(matrix):
    res = 0
    for row in matrix:
        for col in row:
            res += col
    return res

@timing
@numba.njit()
def matrix_sum_nb(np_matrix):
    res = 0
    rows = len(np_matrix)
    cols = len(np_matrix[0])
    # numba require numpy together
    for row in range(rows):
        for col in range(cols):
            res += np_matrix[row][col]
    return res

def test_loop():
    rows = 12800
    cols = 1280
    matrix = [[col for col in range(cols)] for _ in range(rows)]
    print(matrix_sum(matrix))
    np_matrix = np.matrix(matrix)
    print(matrix_sum_nb(np_matrix))

if __name__ == "__main__":
    test_loop()
    