from multiprocessing import cpu_count
import logging
logging.basicConfig(filename="parutils.log", filemode='w', level=logging.INFO)

default_nprocs = cpu_count()
logging.info("number of cpus: {}".format(default_nprocs))

def distribute(nitems, nprocs=None):
    if nprocs is None:
        nprocs = default_nprocs
    nitems_per_proc = int((nitems+nprocs-1)/nprocs)
    logging.info("number of items per process:{}".format(nitems))
    return [(i, min(nitems, nitems_per_proc)) for i in range(0, nitems, nitems_per_proc)]

if __name__ == '__main__':
    result = distribute(100)
    print("result:", result)