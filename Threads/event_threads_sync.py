#!/usr/bin/env python
# To show race condition

import threading
import time

login_counter = 0

def login(lock):
    global login_counter
    thr_name = threading.current_thread().name
    print(f"{thr_name:>10} : {login_counter} -->")
    #time.sleep(.3)
    login_counter += 1
    print(f"{thr_name:>10} :<-- {login_counter}")
    #time.sleep(.05)

def visitors(lock, num):
    for _unused in range(num):
        #lock.acquire()
        # Using a context manager for lock
        with lock:
            login(lock)
        #lock.release()

def campaign():
    n_visitors = 2
    continents = ["Asia", "Africa", "Australia", "America", "Europe"]
    threads = list()
    lock = threading.Lock()
    for cont in continents:
        thr = threading.Thread(target=visitors, 
                               name = cont,
                               args=(lock, n_visitors,),
                              )
        threads.append(thr)

    for thr in threads: thr.start()
    for thr in threads: thr.join()

def main():
    start = time.time()
    campaign()
    print("=" * 30)
    print("Total logins", login_counter)
    print("Time taken :", time.time() - start)


if __name__ == "__main__":
    main()
