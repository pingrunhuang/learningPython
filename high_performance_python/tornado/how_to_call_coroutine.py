
from tornado import gen
from tornado.httpclient import AsyncHTTPClient 

@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch("https://www.baidu.com")
    print(response.body)

# 1. call from another coroutine
@gen.coroutine
def outer_coroutine():
    print("Start call from another coroutine")
    yield coroutine_visit()
    print("end")

# 2. use IOLoop when it is not started yet
from tornado.ioloop import IOLoop
def func_block():
    # this way will block untill the function in run_sync finished
    print("Start to call from run_sync")
    IOLoop.current().run_sync(lambda:coroutine_visit())
    print("end run_sync")

# 3. use IOLoop when it already started
def func_non_block():
    # this way won't block
    print("Start to call from run_sync")
    # there is no way to get the result from spawn_callback, therefore it is only used for function that has no return
    IOLoop.current().spawn_callback(coroutine_visit)
    print("end run_sync")

if __name__ == "__main__":
    func_non_block()