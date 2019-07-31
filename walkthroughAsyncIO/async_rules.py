"""
In the async_hello example, the asyncio.sleep is a native coroutine. We can augment any time consuming operation here. 
Time consuming function here refer to asynchronous generator.

native coroutine:
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r

async generator:
    async def g(x):
        yield x  # OK - this is an async generator

    @asyncio.coroutine syntax is outdated
"""
import time
import asyncio
import requests

url = "http://localhost:8080/{}"

async def task(i: int) -> int:
    print("start {}".format(i))
    response = requests.get(url.format(i))
    return response.text

async def run():
    result = []
    for i in range(10):
        result.append(await task(i))
    print("finished run()")
    return result

if __name__ == "__main__":
    result= asyncio.run(run())
    print(result) 