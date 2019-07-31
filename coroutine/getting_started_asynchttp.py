import aiohttp
import asyncio

URL = "https://www.klook.com/en-HK/"

# async def fetch(url: str, session: aiohttp.ClientSession):
#     async with session.get(url) as response:
#         return await response.status

# async def main():
#     urls = [URL] * 10
#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             status =  fetch(URL, )

async def fetch(session:aiohttp.ClientSession, url:str) -> str:
    async with session.get(url, verify_ssl=False) as response:
        # return await response.text()
        return response.status

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())