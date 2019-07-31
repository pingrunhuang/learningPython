# python version 3.7

import asyncio

async def hello(name):
    print("Hello, ")
    # when reaching the await statement, the function gives back the control of the thread to the main function and let it execute other meaningful task first.
    await asyncio.sleep(2)
    print(name)
    return name

async def main():
    # collecting every task result from the sub task
    result = await asyncio.gather(hello("frank"), hello("franky"), hello("franklin"))
    return result 

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    result = asyncio.run(main())
    elapsed = time.perf_counter() - start
    print("Executed in {} seconds".format(elapsed))
    print(result)