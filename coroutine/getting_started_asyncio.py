import asyncio
import random

async def my_sleep(i: int):
    print("Started coroutine {}".format(i))
    interval = random.randint(1, 5)
    # here is the core section to make the code async
    # give back the control of the program to eventloop
    await asyncio.sleep(interval)
    print("Finished coroutine {} in {} seconds".format(i, interval))

async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(my_sleep(i)))
    await asyncio.gather(*tasks)




if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.close()

    