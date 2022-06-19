import time
from multiprocessing import Process


def task():
    print("Sleeping for 0.5 seconds")
    time.sleep(1)
    print("Finished sleeping")


if __name__ == "__main__":
    start_time = time.perf_counter()

    # creates two multiprocess
    p1 = Process(target=task)
    p2 = Process(target=task)

    # starts both processes
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    total_time = time.perf_counter() - start_time
    print(f"It takes {total_time:0.2f} seconds!")
