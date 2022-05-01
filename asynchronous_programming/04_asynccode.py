import asyncio
import time

# Simulating a heavy task
async def fetchUserData():
    time.sleep(5)
    return 'Large Latte'

async def createOrderMessage():
    order = await fetchUserData()
    return f'Your order is {order}'



async def main():
    print('Fetching user order...')
    print(await createOrderMessage())
    print("Done")


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'Done in {elapsed:0.2f} second(s).')
    
