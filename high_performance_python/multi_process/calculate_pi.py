import random
from multiprocessing.dummy import Pool
# from multiprocessing.pool import Pool
import time
import numpy as np

'''
Making 25000000.0 samples per worker
Estimated pi 3.14139516
Delta: 37.718677043914795

dummy:
Making 25000000.0 samples per worker
Estimated pi 3.14165788
Delta: 72.74466896057129

numpy on pool:
Making 25000000 samples per worker
Estimated pi 3.14157976
Delta: 6.39003586769104

numpy on dummy:
Making 25000000 samples per worker
Estimated pi 3.1416658
Delta: 4.654613971710205
'''



def estimate_number_points_in_quarter_circle_numpy(number_samples):
    np.random.seed()
    xs = np.random.uniform(0, 1, number_samples)
    ys = np.random.uniform(0, 1, number_samples)
    extimate_inside_quarter_unit_circle = (xs**2+ys**2)<=1
    number_trials_in_quarter_unit_circle = np.sum(extimate_inside_quarter_unit_circle)
    return number_trials_in_quarter_unit_circle


def estimate_number_points_in_quarter_circle(number_estimates):
    number_trials_in_quarter_unit_circle = 0
    for _ in range(int(number_estimates)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_unit_circle = (x**2 + y**2 <=1.0)
        number_trials_in_quarter_unit_circle += is_in_unit_circle
    return number_trials_in_quarter_unit_circle

def test(func):
    number_samples_in_total = 1e8
    number_parallel_blocks = 4
    pool = Pool(processes=number_parallel_blocks)
    number_samples_per_process = int(number_samples_in_total / number_parallel_blocks)
    print("Making {} samples per worker".format(number_samples_per_process))

    number_trials_per_process = [number_samples_per_process] * number_parallel_blocks
    start = time.time()
    # single thread
    # pi_estimate = sum(estimate_number_points_in_quarter_circle(number_samples_per_process) for _ in range(4))*4 / number_samples_in_total

    number_in_unit_circles = pool.map(func, number_trials_per_process)
    pi_estimate = sum(number_in_unit_circles) * 4 /number_samples_in_total
    print("Estimated pi", pi_estimate)
    print('Delta:', time.time()-start)






if __name__=='__main__':
    test(estimate_number_points_in_quarter_circle)
