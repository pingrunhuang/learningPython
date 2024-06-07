import threading
import time

def wait_and_print(msg):
    time.sleep(1)
    print(msg)

def async_wait_and_print(msg):
    timer = threading.Timer(1, lambda: print(msg))
    timer.start()

start = time.time()
# wait_and_print(1)
# wait_and_print(2)
# wait_and_print(3)
# print('async:')
async_wait_and_print(1)
async_wait_and_print(2)
async_wait_and_print(3)
print("Duration: {}".format(time.time()-start))




from concurrent.futures import ThreadPoolExecutor
import asyncio
from typing import List
import requests

loop = asyncio.get_event_loop()

executor = ThreadPoolExecutor(3)
async def fetch_urls(urls: List[str]):
    responses = []
    for url in urls:
        fut = await loop.run_in_executor(executor, requests.get, url)
        responses.append(fut)
    return responses

def fetch_urls_parallel(urls):
    return asyncio.gather(*[loop.run_in_executor(executor, requests.get, url) for url in urls])

print(fetch_urls_parallel(['http://www.baidu.com','http://www.douban.com','http://www.sina.com']))

