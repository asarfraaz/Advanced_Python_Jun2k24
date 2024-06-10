# Copyright 2024 Sarfraaz Ahmed. All rights reserved.

###########################################################################
#                                                                         #
#                  Please DO NOT EXECUTE this file.                       #
#                                                                         #
#          This is only a screenshot of a Python/Linux shell              #
#              This file uses .py extension so as to                      #
#            enable syntax highlighting in your editor                    #
#                                                                         #
###########################################################################


>>> # GYAN SESSION
>>>
>>> a = [1, 2, 3, 4, 5]
>>> b = a
>>> b
[1, 2, 3, 4, 5]
>>> a == b
True
>>> a is b
True
>>> id(a), id(b)
(4312240320, 4312240320)
>>> a[0] = 99
>>> a
[99, 2, 3, 4, 5]
>>> b
[99, 2, 3, 4, 5]
>>> aa = a[1:4]
>>> aa
[2, 3, 4]
>>> aa[0] = 55
>>> aa
[55, 3, 4]
>>> a
[99, 2, 3, 4, 5]
>>> id(a), id(b), id(aa)
(4312240320, 4312240320, 4314463104)
>>>
>>> x = "Hello"
>>> y = x
>>> y
'Hello'
>>> x == y
True
>>> x is y
True
>>> id(x), id(y)
(4314531280, 4314531280)
>>> xx = x[1:4]
>>> xx
'ell'
>>> id(x), id(y), id(xx)
(4314531280, 4314531280, 4314531232)
>>>


>>> a
[99, 2, 3, 4, 5]
>>> b
[99, 2, 3, 4, 5]
>>> aa
[55, 3, 4]
>>> id(a), id(b), id(aa)
(4312240320, 4312240320, 4314463104)
>>> c = a[:]
>>> c
[99, 2, 3, 4, 5]
>>> a == c
True
>>> a is c
False
>>> id(a), id(b), id(aa), id(c)
(4312240320, 4312240320, 4314463104, 4312628992)
>>> c[-1] = 77
>>> c
[99, 2, 3, 4, 77]
>>> a
[99, 2, 3, 4, 5]
>>>
>>> x
'Hello'
>>> y
'Hello'
>>> xx
'ell'
>>> id(x), id(y), id(xx)
(4314531280, 4314531280, 4314531232)
>>> z = x[:]
>>> z
'Hello'
>>> x == z
True
>>> x is z
True
>>> id(x), id(y), id(xx), id(z)
(4314531280, 4314531280, 4314531232, 4314531280)
>>> crazy = "He" + "llo"
>>> crazy
'Hello'
>>> x == crazy
True
>>> x is crazy
True
>>> id(x), id(y), id(xx), id(z), id(crazy)
(4314531280, 4314531280, 4314531232, 4314531280, 4314531280)
>>> quit()
Monte-Aire:DB_Access (main) surf$ cd ../Threads/
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python threads_simple.py
PR1 936
Done
Time taken 0.01892876625061035
DV1 114295356 25
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python threads_simple.py
PR1 936
DV1 1 9
Done
Time taken 0.0001919269561767578
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python threads_simple.py
PR1 936
Done
Time taken 0.012745857238769531
DV1 114295356 25
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python threads_simple.py
PR1 936
DV1 114295356 25
Done
Time taken 4.733793020248413
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python event_no_threads.py
      Asia : 0 -->
      Asia :<-- 1
      Asia : 1 -->
      Asia :<-- 2
    Africa : 2 -->
    Africa :<-- 3
    Africa : 3 -->
    Africa :<-- 4
 Australia : 4 -->
 Australia :<-- 5
 Australia : 5 -->
 Australia :<-- 6
   America : 6 -->
   America :<-- 7
   America : 7 -->
   America :<-- 8
    Europe : 8 -->
    Europe :<-- 9
    Europe : 9 -->
    Europe :<-- 10
==============================
Total logins 10
Time taken : 7.200241088867188e-05
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python event_threads.py
      Asia : 0 -->
    Africa : 0 -->
    Africa :<-- 2
      Asia :<-- 1
 Australia : 1 -->
      Asia : 2 -->
      Asia :<-- 4
   America : 2 -->
   America :<-- 5
 Australia :<-- 3
 Australia : 5 -->
 Australia :<-- 6
    Europe : 2 -->
    Africa : 2 -->
    Africa :<-- 8
    Europe :<-- 7
   America : 5 -->
   America :<-- 9
    Europe : 8 -->
    Europe :<-- 10
==============================
Total logins 10
Time taken : 0.0008418560028076172
Monte-Aire:Threads (main) surf$ python event_threads.py
Monte-Aire:Threads (main) surf$ python event_threads.py
      Asia : 0 -->
    Africa : 0 -->
    Africa :<-- 2
      Asia :<-- 1
      Asia : 2 -->
      Asia :<-- 3
   America : 2 -->
   America :<-- 4
   America : 4 -->
   America :<-- 5
    Africa : 5 -->
    Africa :<-- 6
    Europe : 5 -->
    Europe :<-- 7
    Europe : 7 -->
 Australia : 1 -->
 Australia :<-- 9
    Europe :<-- 8
 Australia : 9 -->
 Australia :<-- 10
==============================
Total logins 10
Time taken : 0.0008749961853027344
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python event_threads.py
      Asia : 0 -->
    Africa : 0 -->
 Australia : 0 -->
   America : 0 -->
    Europe : 0 -->
   America :<-- 1
    Africa :<-- 2
   America : 2 -->
    Africa : 2 -->
 Australia :<-- 3
 Australia : 3 -->
      Asia :<-- 4
      Asia : 4 -->
    Europe :<-- 5
    Europe : 5 -->
    Europe :<-- 6
   America :<-- 7
    Africa :<-- 8
      Asia :<-- 10
 Australia :<-- 9
==============================
Total logins 10
Time taken : 0.6098699569702148
Monte-Aire:Threads (main) surf$ python event_threads.py
Monte-Aire:Threads (main) surf$ python event_threads.py python event_
Monte-Aire:Threads (main) surf$ python event_threads_sync.py
      Asia : 0 -->
      Asia :<-- 1
      Asia : 1 -->
      Asia :<-- 2
    Africa : 2 -->
    Africa :<-- 3
    Africa : 3 -->
    Africa :<-- 4
   America : 4 -->
   America :<-- 5
   America : 5 -->
   America :<-- 6
 Australia : 6 -->
 Australia :<-- 7
 Australia : 7 -->
 Australia :<-- 8
    Europe : 8 -->
    Europe :<-- 9
    Europe : 9 -->
    Europe :<-- 10
==============================
Total logins 10
Time taken : 0.0006380081176757812
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python event_threads_sync.py
      Asia : 0 -->
      Asia :<-- 1
      Asia : 1 -->
      Asia :<-- 2
    Africa : 2 -->
    Africa :<-- 3
    Africa : 3 -->
    Africa :<-- 4
 Australia : 4 -->
 Australia :<-- 5
 Australia : 5 -->
 Australia :<-- 6
   America : 6 -->
   America :<-- 7
   America : 7 -->
   America :<-- 8
    Europe : 8 -->
    Europe :<-- 9
    Europe : 9 -->
    Europe :<-- 10
==============================
Total logins 10
Time taken : 0.0005919933319091797
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python event_threads_sync.py
      Asia : 0 -->
      Asia :<-- 1
      Asia : 1 -->
      Asia :<-- 2
 Australia : 2 -->
 Australia :<-- 3
 Australia : 3 -->
 Australia :<-- 4
    Europe : 4 -->
    Europe :<-- 5
    Europe : 5 -->
    Europe :<-- 6
    Africa : 6 -->
    Africa :<-- 7
    Africa : 7 -->
    Africa :<-- 8
   America : 8 -->
   America :<-- 9
   America : 9 -->
   America :<-- 10
==============================
Total logins 10
Time taken : 0.0006701946258544922
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python urls_serial.py
Fetching https://jsonplaceholder.typicode.com/posts/1
Fetching https://jsonplaceholder.typicode.com/posts/1
Fetching https://jsonplaceholder.typicode.com/posts/2
Fetching https://jsonplaceholder.typicode.com/posts/2
Fetching https://jsonplaceholder.typicode.com/posts/3
Fetching https://jsonplaceholder.typicode.com/posts/3
Fetching https://jsonplaceholder.typicode.com/posts/4
Fetching https://jsonplaceholder.typicode.com/posts/4
Fetching https://jsonplaceholder.typicode.com/posts/5
Fetching https://jsonplaceholder.typicode.com/posts/5
Fetching https://jsonplaceholder.typicode.com/posts/6
Fetching https://jsonplaceholder.typicode.com/posts/6
Fetching https://jsonplaceholder.typicode.com/posts/7
Fetching https://jsonplaceholder.typicode.com/posts/7
Fetching https://jsonplaceholder.typicode.com/posts/8
Fetching https://jsonplaceholder.typicode.com/posts/8
Fetching https://jsonplaceholder.typicode.com/posts/9
Fetching https://jsonplaceholder.typicode.com/posts/9
Fetching https://jsonplaceholder.typicode.com/posts/10
Fetching https://jsonplaceholder.typicode.com/posts/10
Fetching https://jsonplaceholder.typicode.com/posts/11
Fetching https://jsonplaceholder.typicode.com/posts/11
Fetching https://jsonplaceholder.typicode.com/posts/12
Fetching https://jsonplaceholder.typicode.com/posts/12
Fetching https://jsonplaceholder.typicode.com/posts/13
Fetching https://jsonplaceholder.typicode.com/posts/13
Fetching https://jsonplaceholder.typicode.com/posts/14
Fetching https://jsonplaceholder.typicode.com/posts/14
2335
==============================
Time taken : 5.32323694229126
Monte-Aire:Threads (main) surf$
Monte-Aire:Threads (main) surf$ python urls_threads.py
Fetching https://jsonplaceholder.typicode.com/posts/1
Fetching https://jsonplaceholder.typicode.com/posts/2
Fetching https://jsonplaceholder.typicode.com/posts/3
Fetching https://jsonplaceholder.typicode.com/posts/4
Fetching https://jsonplaceholder.typicode.com/posts/7
Fetching https://jsonplaceholder.typicode.com/posts/5
Fetching https://jsonplaceholder.typicode.com/posts/8
Fetching https://jsonplaceholder.typicode.com/posts/6
Fetching https://jsonplaceholder.typicode.com/posts/9
Fetching https://jsonplaceholder.typicode.com/posts/10
Fetching https://jsonplaceholder.typicode.com/posts/11
Fetching https://jsonplaceholder.typicode.com/posts/12
Fetching https://jsonplaceholder.typicode.com/posts/13
Fetching https://jsonplaceholder.typicode.com/posts/14
2335
==============================
Time taken : 1.3316490650177002
Monte-Aire:Threads (main) surf$ # I/O Bound operations : Multi threading
Monte-Aire:Threads (main) surf$ # CPU Bound operations : Multi Processing
Monte-Aire:Threads (main) surf$
Monte-Aire:day04 (main) surf$
Monte-Aire:day04 (main) surf$ python date.py
6-6-2024
20-6-2024
Monte-Aire:day04 (main) surf$ python date.py
Printing in format: html
6-6-2024
Printing in format: html
6-6-2024
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py", line 27,
 in <module>
    event.display()
TypeError: Date.display() missing 1 required positional argument: 'fmt'
Monte-Aire:day04 (main) surf$ python date.py
Printing in format: html
6-6-2024
Printing in format: html
6-6-2024
Printing in format: html
20-6-2024
Monte-Aire:day04 (main) surf$ python date.py
Printing in format: html
6-6-2024
Printing in format: html
6-6-2024
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py", line 22,
 in <module>
    event = Date.from_string(event_str)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Date.from_string() missing 1 required positional argument: 'date_str'
Monte-Aire:day04 (main) surf$ python date.py
Printing in format: html
6-6-2024
Printing in format: html
6-6-2024
Printing in format: html
20-6-2024
Monte-Aire:day04 (main) surf$
Monte-Aire:day04 (main) surf$ cd ../Food_Mart/
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory.csv Data/prices.csv
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 76, in <module>
    main(sys.argv)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 70, in main
    inventory_report(invfile, pricefile)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 61, in inventory_report
    print_report(report)
TypeError: print_report() missing 1 required positional argument: 'formatter'
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory.csv Data/prices.csv
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 76, in <module>
    main(sys.argv)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 70, in main
    inventory_report(invfile, pricefile)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 61, in inventory_report
    print_report(report, formatter)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 42, in print_report
    formatter.headings(headers)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/tableformat.py
", line 13, in headings
    raise NotImplementedError
NotImplementedError
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.cs
v
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL         50       9.22     -17.88
     BREAD        250      44.85       1.70
      MINT         25      20.89     -29.26
     PASTE        125     106.28      54.18
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.cs
v
Name,Quantity,Price,Change
OIL,50,9.22,-17.88
BREAD,250,44.85,1.70
MINT,25,20.89,-29.26
PASTE,125,106.28,54.18
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.cs
v csv
Usage: report.py invfile pricefile
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.csv txt
Usage: report.py invfile pricefile
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.csv txt
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL         50       9.22     -17.88
     BREAD        250      44.85       1.70
      MINT         25      20.89     -29.26
     PASTE        125     106.28      54.18
Monte-Aire:Food_Mart (main) surf$

Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.csv csv
Name,Quantity,Price,Change
OIL,50,9.22,-17.88
BREAD,250,44.85,1.70
MINT,25,20.89,-29.26
PASTE,125,106.28,54.18
Monte-Aire:Food_Mart (main) surf$


Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.csv html
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 77, in <module>
    main(sys.argv)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 71, in main
    inventory_report(invfile, pricefile, fmt)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 60, in inventory_report
    formatter = tableformat.create_formatter(fmt)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/tableformat.py
", line 11, in create_formatter
    raise RuntimeError(f'Unknown format: {fmt}')
RuntimeError: Unknown format: html
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

>>> def fun(x=0):
...     return x + 10
...
>>> fun(5)
15
>>> num = 20
>>> fun(num)
30
>>> fun()
10
>>> fun(num)
30
>>> fun(num)
30
>>> fun()
10
>>>






>>> def magic(xl=[]):
...     xl.append(10)
...     print(xl)
...
>>> magic([3, 4, 5])
[3, 4, 5, 10]
>>> nums = [6, 7, 8]
>>> magic(nums)
[6, 7, 8, 10]
>>> magic()
[10]
>>> magic(nums)
[6, 7, 8, 10, 10]
>>> magic(nums)
[6, 7, 8, 10, 10, 10]
>>> magic()
[10, 10]
>>> magic()
[10, 10, 10]
>>> nums
[6, 7, 8, 10, 10, 10]
>>>

>>> def boring(xl=[]):
...     tmp = xl[:]
...     tmp.append(10)
...     print(tmp)
...
>>> nums = [1, 2, 3]
>>> boring(nums)
[1, 2, 3, 10]
>>> boring(nums)
[1, 2, 3, 10]
>>> boring(nums)
[1, 2, 3, 10]
>>> boring(nums)
[1, 2, 3, 10]
>>> boring()
[10]
>>> boring()
[10]
>>> boring()
[10]
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.csv csv
Name,Quantity,Price,Change
OIL,50,9.22,-17.88
BREAD,250,44.85,1.70
MINT,25,20.89,-29.26
PASTE,125,106.28,54.18
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

>>> from fileparse import parse_csv
>>> with open('Data/inventory.csv') as FH:
...     parse_csv(FH, types=[str, int, float])
...
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price': 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 200, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>> with open('Data/missing.csv') as FH:
...     parse_csv(FH, types=[str, int, float])
...
Row 4: Couldn't convert ['MINT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['PASTE', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price': 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}]
>>> help(parse_csv)
Help on function parse_csv in module fileparse:

parse_csv(lines, select: list[str] = None, types=None, has_headers: bool = True, deli
miter: str = ',', silence_errors: bool = False) -> list[dict[str, str | int | float]]
 | list[tuple[str, int, float]]
    Parse a CSV file into a list of records
    based on a given select list of columns
    and convert them to the given datatypes
    Also supports reading CSV files without headers
    Supports supressing of errors messages

>>>
>>> with open('Data/missing.csv') as FH:
...     parse_csv(FH, types=[str, int, float], silence_errors=True)
...
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price': 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}]
>>>
>>> from report import read_inventory
>>> help(read_inventory)
Help on function read_inventory in module report:

read_inventory(filename: str) -> list[dict[str, str | int | float]]

>>> read_inventory('Data/missing.csv', silence_errors=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: read_inventory() got an unexpected keyword argument 'silence_errors'
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>



>>> from report import read_inventory
>>> read_inventory('Data/missing.csv', silence_errors=True)
type(opts)=<class 'dict'>
opts={'silence_errors': True}
Row 4: Couldn't convert ['MINT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['PASTE', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
[<product.Product object at 0x100eaa3c0>, <product.Product object at 0x100eaa3f0>, <product.Product object at 0x100eaa390>, <product.Product object at 0x100eaa420>, <product.Product object at 0x100eaa450>]
>>>
>>> read_inventory('Data/missing.csv', silence_errors=True, debug=True)
type(opts)=<class 'dict'>
opts={'silence_errors': True, 'debug': True}
Row 4: Couldn't convert ['MINT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['PASTE', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
[<product.Product object at 0x100eaa690>, <product.Product object at 0x100eaa4b0>, <product.Product object at 0x100eaa600>, <product.Product object at 0x100eaa6c0>, <product.Product object at 0x100eaa6f0>]
>>>

>>> read_inventory('Data/missing.csv', silence_errors=True)
type(opts)=<class 'dict'>
opts={'silence_errors': True}
Row 4: Couldn't convert ['MINT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['PASTE', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
[<product.Product object at 0x100eaa420>, <product.Product object at 0x100eaa300>, <product.Product object at 0x100eaa2d0>, <product.Product object at 0x100eaa450>, <product.Product object at 0x100eaa360>]
>>> quit()
Monte-Aire:Food_Mart (main) surf$

Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

>>> from report import read_inventory
>>> read_inventory('Data/missing.csv')
type(opts)=<class 'dict'>
opts={}
Row 4: Couldn't convert ['MINT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['PASTE', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
[<product.Product object at 0x100afa360>, <product.Product object at 0x100afa390>, <product.Product object at 0x100afa330>, <product.Product object at 0x100afa3c0>, <product.Product object at 0x100afa3f0>]
>>>


>>> read_inventory('Data/missing.csv', silence_errors=True)
type(opts)=<class 'dict'>
opts={'silence_errors': True}
[<product.Product object at 0x100afa600>, <product.Product object at 0x100afa450>, <product.Product object at 0x100afa5a0>, <product.Product object at 0x100afa630>, <product.Product object at 0x100afa660>]
>>>

>>> read_inventory('Data/missing.csv')
type(opts)=<class 'dict'>
opts={}
Row 4: Couldn't convert ['MINT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['PASTE', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
[<product.Product object at 0x100afa240>, <product.Product object at 0x100afa3f0>, <product.Product object at 0x100afa3c0>, <product.Product object at 0x100afa2d0>, <product.Product object at 0x100afa420>]
>>> read_inventory('Data/missing.csv', silence_errors=True)
type(opts)=<class 'dict'>
opts={'silence_errors': True}
[<product.Product object at 0x100afa660>, <product.Product object at 0x100afa600>, <product.Product object at 0x100afa630>, <product.Product object at 0x100afa570>, <product.Product object at 0x100afa5d0>]
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> from report import read_inventory
>>> read_inventory('Data/missing.csv', silence_errors=True)
type(opts)=<class 'dict'>
opts={'silence_errors': True}
[Product(OIL, 100, 32.2), Product(PASTE, 50, 91.1), Product(CELL, 150, 83.44), Product(SOAP, 95, 40.37), Product(MINT, 50, 65.1)]
>>> from product import Product
>>> pr = Product('MINT', 100, 149.1)
>>> pr
Product(MINT, 100, 149.1)
>>>



>>> from datetime import date
>>> d = date(2024, 10, 23)
>>> print(d)
2024-10-23
>>> d
datetime.date(2024, 10, 23)
>>> x = datetime.date(2024, 10, 23)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?
>>> import datetime
>>> x = datetime.date(2024, 10, 23)
>>> print(x)
2024-10-23
>>>
>>> pr = Product('MINT', 100, 149.1)
>>> pr
Product(MINT, 100, 149.1)
>>> z = Product(MINT, 100, 149.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'MINT' is not defined
>>> name = "Ajay"
>>> print(f'{name}')
Ajay
>>> print(name)
Ajay
>>> name
'Ajay'
>>> repr(name)
"'Ajay'"
>>> print(repr(name))
'Ajay'
>>> print(f'{name}')
Ajay
>>> print(f'{name!r}')
'Ajay'
>>> quit()
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from product import Product
>>> pr = Product('MINT', 100, 149.1)
>>> pr
Product('MINT', 100, 149.1)
>>> z = Product('MINT', 100, 149.1)
>>> z
Product('MINT', 100, 149.1)
>>> z.cost()
14910.0
>>> count = 10
>>> print(count)
10
>>> count
10
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from tableformat import create_formatter, FormatError
>>> try:
...     formatter = create_formatter('xls')
... except FormatError as e:
...     print(e)
...
Unknown format: xls
>>>


>>> todos = "https://jsonplaceholder.typicode.com/todos"
>>> import requests
>>> resp = requests.get(todos)
>>> resp.status_code
200
>>> res = resp.json()
>>> type(res)
<class 'list'>
>>> len(res)
200
>>> res[0]
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
>>> res[:5]
[{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}, {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}, {'userId': 1, 'id': 4, 'title': 'et porro tempora', 'completed': True}, {'userId': 1, 'id': 5, 'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum', 'completed': False}]
>>> from pprint import pprint
>>> pprint(res[:5])
[{'completed': False, 'id': 1, 'title': 'delectus aut autem', 'userId': 1},
 {'completed': False,
  'id': 2,
  'title': 'quis ut nam facilis et officia qui',
  'userId': 1},
 {'completed': False, 'id': 3, 'title': 'fugiat veniam minus', 'userId': 1},
 {'completed': True, 'id': 4, 'title': 'et porro tempora', 'userId': 1},
 {'completed': False,
  'id': 5,
  'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum','userId': 1}]
>>>
>>>
>>> len([ elm for elm in res if elm['completed'] == True ])
90
>>> pprint(res[-5:])
[{'completed': True,
  'id': 196,
  'title': 'consequuntur aut ut fugit similique',
  'userId': 10},
 {'completed': True,
  'id': 197,
  'title': 'dignissimos quo nobis earum saepe',
  'userId': 10},
 {'completed': True,
  'id': 198,
  'title': 'quis eius est sint explicabo',
  'userId': 10},
 {'completed': True,
  'id': 199,
  'title': 'numquam repellendus a magnam',
  'userId': 10},
 {'completed': False,
  'id': 200,
  'title': 'ipsam aperiam voluptates qui',
  'userId': 10}]
>>>
>>>
>>> res[0]
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
>>>
>>> { elm['userId'] for elm in res }
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> len({ elm['userId'] for elm in res })
10
>>> users = "https://jsonplaceholder.typicode.com/users"
>>> resp = requests.get(users)
>>> resp.status_code
200
>>> res = resp.json()
>>> type(res)
<class 'list'>
>>> len(res)
10
>>> res[0]
{'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz','address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}
>>>
>>> pprint(res[0])
{'address': {'city': 'Gwenborough',
             'geo': {'lat': '-37.3159', 'lng': '81.1496'},
             'street': 'Kulas Light',
             'suite': 'Apt. 556',
             'zipcode': '92998-3874'},
 'company': {'bs': 'harness real-time e-markets',
             'catchPhrase': 'Multi-layered client-server neural-net',
             'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
>>> res[0]['username']
'Bret'
>>> res[0]['address']['city']
'Gwenborough'
>>> # Which company does he work for ?
>>> res[0]['company']['name']
'Romaguera-Crona'
>>> # lat ??
>>> res[0]['address']['geo']['lat']
'-37.3159'
>>>
>>> len(res)
10
>>> # print all company names of all the users
>>> pprint(res[0])
{'address': {'city': 'Gwenborough',
             'geo': {'lat': '-37.3159', 'lng': '81.1496'},
             'street': 'Kulas Light',
             'suite': 'Apt. 556',
             'zipcode': '92998-3874'},
 'company': {'bs': 'harness real-time e-markets',
             'catchPhrase': 'Multi-layered client-server neural-net',
             'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
>>> [ elm['company']['name'] for elm in res ]
['Romaguera-Crona', 'Deckow-Crist', 'Romaguera-Jacobson', 'Robel-Corkery', 'Keebler LLC', 'Considine-Lockman', 'Johns Group', 'Abernathy Group', 'Yost and Sons', 'HoegerLLC']
>>> quit()
Monte-Aire:Food_Mart (main) surf$ cd ../Web/flask_project/
Monte-Aire:flask_project (main) surf$ ls
src
Monte-Aire:flask_project (main) surf$ cd src
Monte-Aire:src (main) surf$ ls
mychoice.py
Monte-Aire:src (main) surf$ source ../src/mychoice.py
Monte-Aire:src (main) surf$ cd ..
Monte-Aire:flask_project (main) surf$ ls
src
Monte-Aire:flask_project (main) surf$ cd ..
Monte-Aire:Web (main) surf$ source flsk_env/bin/activate
(flsk_env) Monte-Aire:Web (main) surf$ cd -
/Users/surf/work/python/corp/soc_advpy_jun2k24/code/Web/flask_project
(flsk_env) Monte-Aire:flask_project (main) surf$ cd src
(flsk_env) Monte-Aire:src (main) surf$ python mychoice.py
 * Serving Flask app 'mychoice' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [06/Jun/2024 16:38:08] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 16:38:08] "GET /favicon.ico HTTP/1.1" 404 -
^C(flsk_env) Monte-Aire:src (main) surf$
(flsk_env) Monte-Aire:src (main) surf$
(flsk_env) Monte-Aire:src (main) surf$ python mychoice.py
 * Serving Flask app 'mychoice' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 643-607-160
 * Detected change in '/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Web/flask
_project/src/mychoice.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 643-607-160
127.0.0.1 - - [06/Jun/2024 16:50:31] "GET /home HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 16:50:34] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 16:50:57] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 16:51:00] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 16:51:04] "GET /home HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 16:54:38] "GET /home HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 16:54:39] "GET /home HTTP/1.1" 200 -
 * Detected change in '/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Web/flask
_project/src/mychoice.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 643-607-160
127.0.0.1 - - [06/Jun/2024 16:55:07] "GET /home HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 17:04:34] "GET /home HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 17:04:34] "GET /static/img/cart_001.jpeg HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 17:04:57] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 17:05:04] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2024 17:05:04] "GET /static/img/cart_001.jpeg HTTP/1.1" 304 -
(flsk_env) Monte-Aire:src (main) surf$ cd ../
(flsk_env) Monte-Aire:flask_project (main) surf$ cd ..
(flsk_env) Monte-Aire:Web (main) surf$ cd ..
(flsk_env) Monte-Aire:code (main) surf$ cd day04
(flsk_env) Monte-Aire:day04 (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from date import Date
Printing in format: html
6-6-2024
Printing in format: html
6-6-2024
Printing in format: html
20-6-2024
>>>

>>> d = Date(12, 4, 2024)
>>> d.d
12
>>> d.m
4
>>> d._tz
'IST'
>>> d.__country
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Date' object has no attribute '__country'
>>> dir(d)
['_Date__country', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_tz', 'd', 'display', 'from_string', 'm', 'y']
>>>
>>> d.__dict__
{'d': 12, 'm': 4, 'y': 2024, '_tz': 'IST', '_Date__country': 'India'}
>>> getattr(d, 'm')
4
>>> d.__dict__['m']
4
>>> d.m
4
>>> d._tz
'IST'
>>> d.__country
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Date' object has no attribute '__country'
>>> d._Date__country
'India'
>>> d.__dict__
{'d': 12, 'm': 4, 'y': 2024, '_tz': 'IST', '_Date__country': 'India'}
>>> class MyDate(Date):
...     def __init__(self):
...             self.__country = "Australia"
...
>>> md = MyDate()
>>> md.__country
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyDate' object has no attribute '__country'
>>> md._Australia__country
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyDate' object has no attribute '_Australia__country'
>>> md._MyDate__country
'Australia'
>>> d._Date__country
'India'
>>>
>>> def fun(x):
...     return 10
...
>>> fun.__dict__
{}
>>> dir(fun)
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__']
>>> fun()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: fun() missing 1 required positional argument: 'x'
>>>
>>> hasattr('Date', 'today')
False
>>> def today(self):
...     return "Thursday"
...
>>> Date.today = today
>>> hasattr('Date', 'today')
False
>>> hasattr(Date, 'today')
True
>>> hasattr(Date, 'todays')
False
>>> hasattr(Date, 'today')
True
>>> d
<date.Date object at 0x100e5ba70>
>>> d.today()
'Thursday'
>>> d.__dict__
{'d': 12, 'm': 4, 'y': 2024, '_tz': 'IST', '_Date__country': 'India'}
>>> d.__class__
<class 'date.Date'>
>>> d.__class__.__dict__
mappingproxy({'__module__': 'date', '__init__': <function Date.__init__ at 0x10102bba0>, 'display': <function Date.display at 0x10102bc40>, 'from_string': <classmethod(<function Date.from_string at 0x10102bce0>)>, '__dict__': <attribute '__dict__' of 'Date' objects>, '__weakref__': <attribute '__weakref__' of 'Date' objects>, '__doc__': None, 'today': <function today at 0x10102bec0>})
>>> from pprint import pprint
>>> pprint(d.__class__.__dict__)
mappingproxy({'__dict__': <attribute '__dict__' of 'Date' objects>,
              '__doc__': None,
              '__init__': <function Date.__init__ at 0x10102bba0>,
              '__module__': 'date',
              '__weakref__': <attribute '__weakref__' of 'Date' objects>,
              'display': <function Date.display at 0x10102bc40>,
              'from_string': <classmethod(<function Date.from_string at 0x10102bce0>)
>,
              'today': <function today at 0x10102bec0>})
>>> d.__class__.__dict__.today()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'mappingproxy' object has no attribute 'today'
>>> d.__class__.__dict__.today(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'mappingproxy' object has no attribute 'today'
>>> d.__class__.__dict__['today']
<function today at 0x10102bec0>
>>> d.__class__.__dict__['today']()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: today() missing 1 required positional argument: 'self'
>>> d.__class__.__dict__['today'](d)
'Thursday'
>>> d.today()
'Thursday'
>>> dir(d)
['_Date__country', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_tz', 'd', 'display', 'from_string', 'm', 'today', 'y']
>>> quit()
(flsk_env) Monte-Aire:day04 (main) surf$ ls
__pycache__ date.py
(flsk_env) Monte-Aire:day04 (main) surf$ vi date.py
(flsk_env) Monte-Aire:day04 (main) surf$ python date.py
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(12)display()
-> print("Printing in format:", fmt)
(Pdb) l
  7             self._tz = "IST"
  8             self.__country = "India"
  9
 10         def display(self, fmt):
 11             breakpoint()
 12  ->         print("Printing in format:", fmt)
 13             print(f'{self.d}-{self.m}-{self.y}')
 14
 15         @classmethod
 16         def from_string(cls, date_str):
 17             parts = list(map(int, date_str.split('-')))
(Pdb) where
  /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(22)<module>()
-> today.display('html')
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(12)display()
-> print("Printing in format:", fmt)
(Pdb) fmt
'html'
(Pdb) self.d
6
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) n
Printing in format: html
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(13)display()
-> print(f'{self.d}-{self.m}-{self.y}')
(Pdb) l
  8             self.__country = "India"
  9
 10         def display(self, fmt):
 11             breakpoint()
 12             print("Printing in format:", fmt)
 13  ->         print(f'{self.d}-{self.m}-{self.y}')
 14
 15         @classmethod
 16         def from_string(cls, date_str):
 17             parts = list(map(int, date_str.split('-')))
 18             return Date(parts[0], parts[1], parts[2])
(Pdb) n
6-6-2024
--Return--
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(13)display()->No
ne
-> print(f'{self.d}-{self.m}-{self.y}')
(Pdb) c
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(12)display()
-> print("Printing in format:", fmt)
(Pdb) where
  /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(23)<module>()
-> Date.display(today, 'html')
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(12)display()
-> print("Printing in format:", fmt)
(Pdb) n
Printing in format: html
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(13)display()
-> print(f'{self.d}-{self.m}-{self.y}')
(Pdb)
6-6-2024
--Return--
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(13)display()->No
ne
-> print(f'{self.d}-{self.m}-{self.y}')
(Pdb) c
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(12)display()
-> print("Printing in format:", fmt)
(Pdb) where
  /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(31)<module>()
-> event.display('html')
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(12)display()
-> print("Printing in format:", fmt)
(Pdb) n
Printing in format: html
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(13)display()
-> print(f'{self.d}-{self.m}-{self.y}')
(Pdb) m
*** NameError: name 'm' is not defined
(Pdb) n
20-6-2024
--Return--
> /Users/surf/work/github/priv/Advanced_Python_Jun2k24/day04/date.py(13)display()->No
ne
-> print(f'{self.d}-{self.m}-{self.y}')
(Pdb) c
(flsk_env) Monte-Aire:day04 (main) surf$

# Copyright 2024 Sarfraaz Ahmed. All rights reserved.
