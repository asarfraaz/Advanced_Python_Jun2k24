#!/usr/bin/env python
# To show race condition

import time

login_counter = 0

def login(thr_name):
    global login_counter
    print(f"{thr_name:>10} : {login_counter} -->")
    login_counter += 1
    print(f"{thr_name:>10} :<-- {login_counter}")

def visitors(num, name):
    for _unused in range(num):
        login(name)

def campaign():
    n_visitors = 2
    continents = ["Asia", "Africa", "Australia", "America", "Europe"]
    for cont in continents:
        visitors(n_visitors, cont)

def main():
    start = time.time()
    campaign()
    print("=" * 30)
    print("Total logins", login_counter)
    print("Time taken :", time.time() - start)


if __name__ == "__main__":
    main()
