import time


def count():
    print("One")
    time.sleep(1)
    print("Tow")


def main():
    [count() for _ in range(3)]


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed_time:0.2f} second(s).")
