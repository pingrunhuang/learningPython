from multiprocessing import Process, Pool
from rediscluster import RedisCluster
import time

HOST = "127.0.0.1"
CLUSTER_INFO = [
    {'host':HOST,'port':7000},
    {'host':HOST,'port':7001},
    {'host':HOST,'port':7002},
    {'host':HOST,'port':7003},
    {'host':HOST,'port':7004},
    {'host':HOST,'port':7005}]

def connect(cluster):
    client = RedisCluster(startup_nodes=cluster)
    result = client.get("hey")
    time.sleep(1)
    print(result)

if __name__ == "__main__":
    MAX_WORKERS = 100
    TASKS = MAX_WORKERS
    with Pool(MAX_WORKERS) as p:
        p.map(connect, [CLUSTER_INFO, CLUSTER_INFO, CLUSTER_INFO, CLUSTER_INFO, CLUSTER_INFO]*TASKS)