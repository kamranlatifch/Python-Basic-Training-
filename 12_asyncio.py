# file name: 12_asyncio.py

import asyncio


async def function_1():

    print("Function 1 started")
    await asyncio.sleep(1)


async def function_2():
    print("Function 2 started")
    await asyncio.sleep(1)


async def function_3():
    print("Function 3 started")
    await asyncio.sleep(4)


async def main():
    L = await asyncio.gather(function_1(), function_2(), function_3())
    # task = asyncio.create_task(function_1())
    # # await function_1()
    # await function_2()
    # await function_3()

    print(L)


asyncio.run(main())
