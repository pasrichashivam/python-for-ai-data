import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = fetch_data(1)  # This will create a coroutine object but not run it yet
    task2 = fetch_data(2)  
    result1 = await task1  # This will run the first coroutine and wait for it to complete before moving on to the next line
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main()) # This will run the event loop and execute the main coroutine, returning the results of the tasks.
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")