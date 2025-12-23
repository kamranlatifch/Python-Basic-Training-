"""
===========================================
PYTHON TUTORIAL: Asynchronous Programming and Asyncio
===========================================
This file covers async/await, coroutines, and asyncio.
Run this file with: python3 09_async_asyncio.py
"""

print("=" * 60)
print("PART 1: WHAT IS ASYNCHRONOUS PROGRAMMING?")
print("=" * 60)

print("\nAsynchronous programming allows tasks to run concurrently.")
print("Instead of waiting for one task to finish, start multiple tasks")
print("and handle them as they complete.")
print("\nBenefits:")
print("- Non-blocking: don't wait for I/O operations")
print("- Efficient: handle many tasks simultaneously")
print("- Better performance for I/O-bound operations")

print("\n" + "=" * 60)
print("PART 2: ASYNC/AWAIT SYNTAX AND COROUTINES")
print("=" * 60)

import asyncio
import time


# Coroutine: function defined with async def
async def say_hello(name):
    """This is a coroutine function"""
    print(f"Hello {name}!")
    await asyncio.sleep(1)  # Simulate async operation
    return f"Greeted {name}"


print("\nDefining a coroutine:")
print("async def function_name():  # Creates a coroutine")
print("await async_operation()    # Waits for async operation")


# Running a single coroutine
async def main():
    result = await say_hello("Alice")
    print(f"Result: {result}")


print("\nRunning a coroutine:")
print("asyncio.run(coroutine())  # Runs coroutine in event loop")
asyncio.run(main())

print("\n" + "=" * 60)
print("PART 3: CONCURRENT EXECUTION")
print("=" * 60)


async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} completed")
    return f"Task {name} done"


async def concurrent_example():
    print("\nRunning tasks concurrently:")
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 1))
    task3 = asyncio.create_task(task("C", 3))
    results = await asyncio.gather(task1, task2, task3)
    print(f"All tasks completed: {results}")


asyncio.run(concurrent_example())

print("\n" + "=" * 60)
print("PART 4: ASYNCIO.SLEEP VS TIME.SLEEP")
print("=" * 60)


def sync_example():
    print("\nSynchronous (blocking):")
    start = time.time()
    time.sleep(1)
    time.sleep(1)
    print(f"Time: {time.time() - start:.2f} seconds")


async def async_concurrent():
    print("\nAsynchronous (concurrent):")
    start = time.time()
    await asyncio.gather(asyncio.sleep(1), asyncio.sleep(1))
    print(f"Time: {time.time() - start:.2f} seconds (concurrent!)")


sync_example()
asyncio.run(async_concurrent())

print("\n" + "=" * 60)
print("PART 5: PRACTICAL EXAMPLE")
print("=" * 60)


async def download_file(filename, size_mb):
    print(f"Starting download: {filename}")
    await asyncio.sleep(size_mb * 0.5)
    print(f"Completed: {filename} ({size_mb}MB)")
    return f"{filename} downloaded"


async def download_example():
    print("\nSequential (slow):")
    start = time.time()
    await download_file("file1.zip", 2)
    await download_file("file2.zip", 2)
    print(f"Time: {time.time() - start:.2f} seconds")

    print("\nConcurrent (fast):")
    start = time.time()
    await asyncio.gather(download_file("file1.zip", 2), download_file("file2.zip", 2))
    print(f"Time: {time.time() - start:.2f} seconds")


asyncio.run(download_example())

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nKey Takeaways:")
print("- async def: defines a coroutine function")
print("- await: waits for async operation without blocking")
print("- asyncio.run(): runs coroutine in event loop")
print("- asyncio.create_task(): creates concurrent tasks")
print("- asyncio.gather(): runs multiple coroutines concurrently")
print("- asyncio.sleep(): non-blocking sleep (use instead of time.sleep)")
print("- Best for I/O-bound operations (network, files, databases)")
print("\nAsynchronous programming improves performance for I/O-bound tasks!")
