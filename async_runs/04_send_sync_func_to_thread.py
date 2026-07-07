import asyncio
import time


def fetch_data(param):
    print(f"Do something with {param}...", flush=True)
    time.sleep(param) # This is a blocking call, simulating a long-running operation
    print(f"Done with {param}", flush=True)
    return f"Result of {param}"


async def main():
    # asyncio.to_thread will run fetch_data(2) in a separate thread, 
    # allowing the event loop to continue running other tasks concurrently.
    # Useful for I/O-bound operations that are blocking, like file I/O or network requests.
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 2)) 
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 5))
    result1 = await task1
    print("Thread 1 fully completed")
    result2 = await task2
    print("Thread 2 fully completed")

    return [result1, result2]


if __name__ == "__main__":
    t1 = time.perf_counter()

    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()
    print(f"Finished in {t2 - t1:.2f} seconds")