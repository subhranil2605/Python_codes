import time
import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed_time = time.perf_counter() - s

    print(f"{__file__} executes in {elapsed_time:0.2f} seconds.")