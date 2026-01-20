import asyncio
import time

#define a coroutine
async def task(name, delay):
    print(f'Task {name}: Starting')
    await asyncio.sleep(delay)
    print(f'Task {name}: Completed after {delay} seconds')