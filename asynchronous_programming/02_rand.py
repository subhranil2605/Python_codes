import asyncio
import random

c = (
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m",
)


async def makerandom(idx: int, thrshold: int = 2) -> int:
    print(c[idx + 1] + f'Initiated makerandom({idx}).')
    i = random.randint(0, 10)
    while i < thrshold:
        print(c[idx + 1] + f'Initiated makerandom({idx})=={i} too low; retrying.')
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f'--> Finished: makerandom({idx})=={i}' + c[0])
    return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == '__main__':
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1},r2: {r2},r3: {r3}")
