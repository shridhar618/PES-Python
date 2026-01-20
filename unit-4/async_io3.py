# import asyncio
# import time
# import aiohttp

# URL=['https://google.com',
#      'https://github.com',
#      'https://www.python.org',
#      'https://www.wikipedia.org'
#      ]

# async def fetch_url(session, url):
#     #one HTTP request per call
#     start=time.time()
#     try:
#         async with session.get(url) as response:
#             await response.read()
#             end=time.time()
#             tt=round(end-start,2)
#             return url, response.status, tt
#     except Exception:
#         end=time.time()
#         tt=round(end-start,2)
#         return url, -1, tt
    
    
# async def main():
#     async with aiohttp.ClientSession() as session:
#         results=await asyncio.gather(*[fetch_url(session, url) for url in URL])
#         print("URL Fetch Results:")
#         for url, status, tt in results:
#             if status == -1:
#                 print(f"URL: {url} could not be fetched. Time taken: {tt} seconds")
#             else:
#                 print(f"URL: {url}, Status: {status}, Time taken: {tt} seconds")
                
                
                
# asyncio.run(main())



import asyncio
import time
import aiohttp
import ssl

URL = [
    'https://google.com',
    'https://github.com',
    'https://www.python.org',
    'https://www.wikipedia.org'
]

# Disable SSL verification (safe for learning/testing)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

async def fetch_url(session, url):
    start = time.time()
    try:
        async with session.get(
            url,
            ssl=ssl_context,
            headers=HEADERS,
            timeout=aiohttp.ClientTimeout(total=10)
        ) as response:
            await response.read()
            tt = round(time.time() - start, 2)
            return url, response.status, tt
    except Exception as e:
        tt = round(time.time() - start, 2)
        return url, -1, tt

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[fetch_url(session, url) for url in URL]
        )

        print("URL Fetch Results:")
        for url, status, tt in results:
            if status == -1:
                print(f"❌ {url} could not be fetched ({tt}s)")
            else:
                print(f"✅ {url} | Status: {status} | Time: {tt}s")

asyncio.run(main())

