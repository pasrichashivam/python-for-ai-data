import asyncio
import time

# First Task
async def api_call(url:str, delay:int=3):
    print("Fetching data from: ", url)
    await asyncio.sleep(delay)
    print("Data fetched from: ", url)
    return url + ' return data'

# Second Task
async def execution():
    print("Started Execution Completed")
    time.sleep(5)
    print("Execution Completed")

# Third Task
async def transformation():
    print("Started Transformation")
    asyncio.sleep(4)
    print("Transformation Completed")

async def main():

    # Creating Tasks with Gather
    tasks = await asyncio.gather(
        api_call("https://api_1.com"),
        execution(),
        transformation(),   
        )
    print("All API calls completed.")
    print(tasks)

asyncio.run(main())
