#!/usr/bin/env python

import threading
from slow_calc import slow_mult, slow_divide

def find_prod(a, b):
    res = slow_mult(a, b)
    print(threading.current_thread().name, res)

def find_quotient(n, d):
    quot, rem = slow_divide(n, d)
    print(threading.current_thread().name, quot, rem)

# Main
pr1 = threading.Thread(target=find_prod, name="PR1", args=(12, 78))

# Add another thread for doing division
dv1 = threading.Thread(target=find_quotient, name="DV1", args=(7657788877, 67))

import time
start = time.time()

pr1.start()
dv1.start()

print("Done")
print("Time taken", time.time() - start)
