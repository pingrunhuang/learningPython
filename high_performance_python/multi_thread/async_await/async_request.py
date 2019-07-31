import asyncio
import requests
urls = []
result = []
async def my_get():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(None, requests.get, urls) 
    ]
    for x in await asyncio.gather(*futures):
        result.append(x)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_get())
    for r in result:
        if not r.ok:
            print(r.json())