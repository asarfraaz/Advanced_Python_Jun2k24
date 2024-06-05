#!/usr/bin/env python
'''
    Publisher/Consumer architecture
    Publisher : visitor_reception
    Consumer  : manager ( a daemon )
'''

import threading, queue
import time

login_counter = 0
counter_queue = queue.Queue()

def login_manager():
    global login_counter
    while True:
        val, thr_name = counter_queue.get()
        thr_name = threading.current_thread().name
        print(f"{thr_name:>10} : {login_counter} -->")
        login_counter += val

        # Uncomment below sleep to simulate delay
        #time.sleep(.3)
        print(f"{thr_name:>10} :<-- {login_counter}")
        counter_queue.task_done()


def visitor_reception(num):
    for _unused in range(num):
        thr_name = threading.current_thread().name

        # Each team member puts the filled up form in the work tray
        counter_queue.put((1, thr_name))

        # Uncomment below sleep to simulate delay
        #time.sleep(.2)

def campaign():
    # It does not matter whether we start the daemon process
    # before or after starting the PUT threads

    #manager = threading.Thread(target=login_manager)
    #manager.daemon = True
    #manager.start()
    #del manager

    # No. of team members in each team representing one of the 5 continents
    n_visitors = 2
    continents = ["Asia", "Africa", "Australia", "America", "Europe"]
    threads = list()
    for cont in continents:
        thr = threading.Thread( target=visitor_reception,
                                name=cont,
                                args=(n_visitors,)
                              )
        threads.append(thr)

    # Each team at the reception starts filling up the form
    # The bellboys provide the forms and stationery
    for thr in threads:
        thr.start()

    # The manager starts working on the forms in the work tray
    manager = threading.Thread(target=login_manager)
    manager.daemon = True
    manager.start()
    del manager

    # The bellboys waits for visitors to finish filling up the form
    print("Waiting on threads")
    for thr in threads:
        thr.join()
    print("All threads done")

    # The manager stays back to finish all forms in the work tray
    print("Waiting on queue")
    counter_queue.join()
    print("Queue jobs done")

def main():
    start = time.time()
    campaign()
    print("=" * 30)
    print("Total logins", login_counter)
    print("Time taken :", time.time() - start)


if __name__ == "__main__":
    main()
    # Program ends when the work tray is empty
