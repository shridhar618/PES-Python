import asyncio
import time

#define a coroutine
async def task(name, delay):
    print(f'Task {name}: Starting')
    await asyncio.sleep(delay)
    end_time = time.strftime("%H:%M:%S", time.localtime())  
    print(f'Task {name}: Completed after {delay} seconds at {end_time}')
    return name, end_time


#define the main controller which is async in nature
async def main():
    results=await asyncio.gather(
        task('A', 2),
        task('B', 3),
        task('C', 1)
    )
    print("All tasks completed. Results:")
    for name,t in results:
        print(f'Task {name} finished at {t}')
        
asyncio.run(main())
#event loop is created and main() is scheduled to run in it