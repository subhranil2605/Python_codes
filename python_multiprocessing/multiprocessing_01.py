import time
from threading import Thread
from multiprocessing import Process

def toast_bread():
    print("toasting bread...")
    time.sleep(2)
    print("bread toasted!")


def make_some_coffee():
    print("turned on coffee maker..")
    time.sleep(3)
    print("Poured a nice cup of coffee!")


def boil_water_egg():
    print("boiling water...")
    time.sleep(5)
    print("water boiled")

# sync coding
##toast_bread()
##make_some_coffee()
##boil_water_egg()

##threadlist = []
##threadlist.append(Thread(target=toast_bread))
##threadlist.append(Thread(target=make_some_coffee))
##threadlist.append(Thread(target=boil_water_egg))


processlist = []
processlist.append(Process(target=toast_bread))
processlist.append(Process(target=make_some_coffee))
processlist.append(Process(target=boil_water_egg))


start_time = time.perf_counter()
for t in processlist:
    t.start()

for t in processlist:
    t.join()

# time counter
total_time = time.perf_counter() - start_time
print(f"It takes {total_time:0.2f} seconds!")










