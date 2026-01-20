#program to time the coroutines and calculate total time taken
import asyncio
import time

#coroutine job is defined
async def job(name, delay):
    start=time.time()
    print(f'Job {name} started at {time.strftime("%X")}')
    await asyncio.sleep(delay)
    end=time.time()
    tt=round(end-start,2)
    print(f'Job {name} is executed after {tt} seconds at {time.strftime("%X")}')
    return name, tt

async def main():
    t0=time.time()
    results=await asyncio.gather(
        job('A', 2),
        job('B', 3),
        job('C', 1)
        job('D', 4)
    )
    t1=time.time()
    print("Overall time taken to execute all jobs:", round(t1-t0,2), "seconds")
    print("Individual job times:")
    for name, tt in results:
        print(f"Job {name} took {tt} seconds")
        
asyncio.run(main())