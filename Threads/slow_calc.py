#!/usr/bin/env python

def slow_mult(n, m):
    ''' Return n * m
        by adding n to itself, m times
    '''
    res = 0
    for _ in range(m):
        res += n
    return res

def slow_divide(num, den):
    ''' Return num / den and num % den
    '''
    quot = 0
    rem = num
    while rem >= den:
        rem = num - den
        quot += 1
        num = rem

    return quot, rem

# Main
if __name__ == "__main__":
    import time
    start = time.time()
    print(slow_mult(9, 2))
    print(slow_mult(888888, 8746868))
    print(888888 * 8746868)
    print(slow_divide(9, 2))
    print(slow_divide(8897753577, 777))
    print(8897753577 // 777, 8897753577 % 777)
    print("Time taken", time.time() - start)
