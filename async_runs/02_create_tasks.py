import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
     # create_task() schedules the coroutine to run in the background and returns a Task object.
     # This allows the event loop to manage the execution of the coroutine concurrently with other tasks.
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    # This line awaits the completion of task1. The event loop will pause the execution of main() 
    # until task1 is done, allowing other tasks if any in ready state to run in the meantime.
    result1 = await task1  
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")