#!/usr/bin/python3.7
import requests
import asyncio
import time

url = "http://localhost:8080/{}"

# ANSI colors
colors = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def get_rand(seed:int)->str:
    return requests.get(url.format(str(seed))).text

##############################################################################
# using queue
##############################################################################
async def produce(nprod: int, q:asyncio.Queue) -> None:
    for _ in range(nprod):
        result = await get_rand(nprod)
        t = time.perf_counter()
        await q.put((result, t))
        print(colors[nprod%len(colors)] + f"producer {nprod} added <{result}> to queue." + colors[0])

async def consume(ncon:int, q:asyncio.Queue) -> None:
    while True:
        result,t = await q.get()
        now = time.perf_counter()
        print(colors[ncon%len(colors)] + f"consumer {ncon} got element <{result}> in {now -t:0.5f} seconds." + colors[0])
        q.task_done()

async def main(nprod:int, ncon:int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n,q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n,q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()# Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()



##############################################################################

if __name__ == "__main__":
    asyncio.run(main(12,5))