#!/usr/bin/env python
# To show race condition

import threading
from multiprocessing.pool import ThreadPool
import time

login_counter = 0

def login(lock):
    global login_counter
    thr_name = threading.current_thread().name
    print(f"{thr_name:>10} : {login_counter} -->")
    #time.sleep(.3)
    login_counter += 1
    print(f"{thr_name:>10} :<-- {login_counter}")
    #time.sleep(.2)

def visitors(lock, num):
    for _unused in range(num):
        lock.acquire()
        login(lock)
        lock.release()

def campaign():
    n_visitors = 2
    continents = ["Asia", "Africa", "Australia", "America", "Europe"]
    threads = list()
    lock = threading.Lock()

    #######
    # visit = lambda x: threading.Thread(target=visitors, name=x, args=(lock, n_visitors,))
    # threads = list(map(visit, continents))
    ######
    visit = lambda x: visitors(lock, n_visitors)
    with ThreadPool() as pool:
        pool.map(visit, continents)


def main():
    start = time.time()
    campaign()
    print("=" * 30)
    print("Total logins", login_counter)
    print("Time taken :", time.time() - start)


if __name__ == "__main__":
    main()
