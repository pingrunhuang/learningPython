"""
This script is used for demonstrate how to speed up your programe using multiprocessing and multithreading
Summary of this post: https://realpython.com/python-concurrency/
"""
import time

###############sequencial version##############################
import requests
def seq_download(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def seq_download_all(urls):
    with requests.Session() as sess:
        for url in urls:
            seq_download(url, sess)

################ threading version #############################
"""
the idea behind multitasking is to shorten the waiting time of IO
threading vs asyncio:
    same: multitasking in 1 processor
    different: the way they switch in between threads. threading use pre emptive and asyncio use coorperative
"""

import threading
from concurrent import futures  # for getting a pool

local_thread = threading.local()

def get_session():
    # share the same session in the whole current thread
    if not getattr(local_thread, "session", None):
        local_thread.session = requests.Session()
    return local_thread.session

def threading_download(url):
    # why each thread should have it's own session? https://github.com/kennethreitz/requests/issues/2766
    sess = get_session()
    seq_download(url, sess)

def threading_download_all(urls):
    """
    Create a pool of threads/tasks, each can run concurrently.
    Thread
    Pool: pool of threads
    executor: control how to switch threads
    """
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(threading_download, urls)


################## asyncio version ###########################
"""
asyncio is here to solve the problem caused in threading package: race condition
"""
import asyncio
import aiohttp

async def async_download(url, sess):
    async with sess.get(url) as response:
        print(f"Read {response.content_length} from {url}")

async def async_download_all(urls):
    tasks = []
    async with aiohttp.ClientSession() as sess:
        for url in urls:
            # it creates a list of tasks using asyncio.ensure_future(), 
            # which also takes care of starting them. Once all the tasks are created, 
            # this function uses asyncio.gather() to keep the session context alive until all of the tasks have completed
            tasks.append(asyncio.ensure_future(async_download(url, sess)))
        await asyncio.gather(*tasks,return_exceptions=True)


#################### multiprocessing version##########################
import multiprocessing
sess = None

def set_session_for_each_process():
    # initializer=set_global_session part of that call. 
    # Remember that each process in our Pool has its own memory space. That means that they cannot share things like a Session object. 
    global sess
    if not sess:
        sess = requests.Session()
    
def multiprocess_download_one(url):
    assert sess is not None
    with sess.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def multiprocess_download_all(urls):
    with multiprocessing.Pool(initializer=set_session_for_each_process) as pool:
        pool.map(multiprocess_download_one, urls)
        # if the given function require multiple args: 
        # pool.starmap(multiprocess_download_one, args) 

def run():
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start = time.time()
    # seq_download_all(urls)
    # threading_download_all(urls)
    # asyncio.get_event_loop().run_until_complete(async_download_all(urls))
    multiprocess_download_all(urls)
    duration = time.time()-start
    print(f"Download {len(urls)} in {duration} seconds")

if __name__ == "__main__":
    """
    For CPU-bound problems only really gain from using multiprocessing. threading and asyncio did not help this type of problem at all.

    For I/O-bound problems, there’s a general rule of thumb in the Python community: “Use asyncio when you can, threading when you must.” 
    asyncio can provide the best speed up for this type of program, but sometimes you will require critical libraries that have not been ported to take advantage of asyncio.
    Remember that any task that doesn’t give up control to the event loop will block all of the other tasks
    """
    run()