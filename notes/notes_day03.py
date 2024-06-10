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


>>> a = [1, 2, 3, 4, 5]
>>> b = [10, 20, 30]
>>>
>>> c = a + b
>>> len(c)
8
>>> d = [a, b]
>>> len(d)
2
>>> d
[[1, 2, 3, 4, 5], [10, 20, 30]]
>>>
>>> e = [*a, b]
>>> e
[1, 2, 3, 4, 5, [10, 20, 30]]
>>> len(e)
6
>>> e = [*a, *b]
>>> e
[1, 2, 3, 4, 5, 10, 20, 30]
>>> len(e)
8
>>> # List Concatenation
>>> # [*a, *b] : Unpacking contents of list a and list b
>>>
>>> x = {'a' : 10, 'b' : 20, 'c' : 30 }
>>> y = { 'm' : 230, 'n' : 450 }
>>> len(x)
3
>>> len(y)
2
>>> x + y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> z = {**x, **y} # Unpacking dictionaries x and y
>>> z
{'a': 10, 'b': 20, 'c': 30, 'm': 230, 'n': 450}
>>> len(z)
5
>>>


>>> defaults = {'user' : 'test', 'passwd' : 12345, 'debug': False}
>>> inputs = {'server': 'mars', 'passwd' : "$%GF02jjj", 'log_errors' : True}
>>>
>>> config = {**defaults, **inputs}
>>> config
{'user': 'test', 'passwd': '$%GF02jjj', 'debug': False, 'server': 'mars', 'log_errors
': True}
>>>
>>> inputs = {'server': 'mars', 'log_errors' : True}
>>> config = {**defaults, **inputs}
>>> config
{'user': 'test', 'passwd': 12345, 'debug': False, 'server': 'mars', 'log_errors': True}
>>> inputs = {'server': 'mars', 'debug' : True}
>>> config = {**defaults, **inputs}
>>> config
{'user': 'test', 'passwd': 12345, 'debug': True, 'server': 'mars'}
>>> quit()
Monte-Aire:Food_Mart (main) surf$ 
Monte-Aire:Food_Mart (main) surf$ python report.py
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
Monte-Aire:Food_Mart (main) surf$ python -i report.py
>>> inventory_report('Data/inventory.csv', 'Data/prices.csv')
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
>>>
>>> inventory_report('Data/inventory.csv', 'Data/prices.csv')
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
>>> inventory_report('Data/inventory2.csv', 'Data/prices.csv')
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL         50       9.22     -17.88
     BREAD        250      44.85       1.70
      MINT         25      20.89     -29.26
     PASTE        125     106.28      54.18
>>> files = ['Data/inventory.csv', 'Data/inventory2.csv']
>>> for name in files:
...     print(f'{name:-^43s}')
...     inventory_report(name, 'Data/prices.csv')
...     print()
...
------------Data/inventory.csv-------------
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84

------------Data/inventory2.csv------------
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL         50       9.22     -17.88
     BREAD        250      44.85       1.70
      MINT         25      20.89     -29.26
     PASTE        125     106.28      54.18

>>>
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import invcost
Total cost: 44671.15
>>> import report
>>> quit()
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import invcost
Total cost: 44671.15
>>> import report
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
>>> import fileparse
>>> help(fileparse)
Help on module fileparse:

NAME
    fileparse - Parse a csv file into a list of entries

FUNCTIONS
    parse_csv(filename: str, select: list[str] = None, types=None, has_headers: bool
= True, delimiter: str = ',', silence_errors: bool = False) -> list[dict[str, str | i
nt | float]] | list[tuple[str, int, float]]
        Parse a CSV file into a list of records
        based on a given select list of columns
        and convert them to the given datatypes
        Also supports reading CSV files without headers
        Supports supressing of errors messages

FILE
    /Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/fileparse.py


>>> dir(fileparse)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__pa
ckage__', '__spec__', 'csv', 'parse_csv']
>>> help(fileparse.parse_csv)
Help on function parse_csv in module fileparse:

parse_csv(filename: str, select: list[str] = None, types=None, has_headers: bool = Tr
ue, delimiter: str = ',', silence_errors: bool = False) -> list[dict[str, str | int |
 float]] | list[tuple[str, int, float]]
    Parse a CSV file into a list of records
    based on a given select list of columns
    and convert them to the given datatypes
    Also supports reading CSV files without headers
    Supports supressing of errors messages

>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import fileparse
>>> help(fileparse)
Help on module fileparse:

NAME
    fileparse - Parse a csv file into a list of entries

FUNCTIONS
    parse_csv(filename: str, select: list[str] = None, types=None, has_headers: bool
= True, delimiter: str = ',', silence_errors: bool = False) -> list[dict[str, str | i
nt | float]] | list[tuple[str, int, float]]
        Parse a CSV file into a list of records
        based on a given select list of columns
        and convert them to the given datatypes
        Also supports reading CSV files without headers
        Supports supressing of errors messages

>>>
>>>
>>> fileparse.parse_csv('Data/inventory.csv',
...                     select=['name', 'quant', 'price'],
...                     types=[str, int, float]
...                     )
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price': 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 200, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>> inv = _
>>> inv
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price': 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 200, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>>
>>> 10 + 20
30
>>> _ * 1.1
33.0
>>> 50 - _
17.0
>>> bal = _
>>> bal
17.0
>>> inv
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price': 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 200, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>> from pprint import pprint
>>> pprint(inv)
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100}]
>>> quit()
Monte-Aire:Food_Mart (main) surf$ python report.py
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from fileparse import parse_csv
>>>
>>> help(parse_csv)
Help on function parse_csv in module fileparse:

parse_csv(filename: str, select: list[str] = None, types=None, has_headers: bool = Tr
ue, delimiter: str = ',', silence_errors: bool = False) -> list[dict[str, str | int |
 float]] | list[tuple[str, int, float]]
    Parse a CSV file into a list of records
    based on a given select list of columns
    and convert them to the given datatypes
    Also supports reading CSV files without headers
    Supports supressing of errors messages

>>> parse_csv('Data/prices.csv', types=[str, float], has_headers=False)
[('ALMOND', 49.16), ('APPLES', 28.47), ('BANANA', 24.22), ('BREAD', 44.85), ('BUNS',51.94), ('BUTTER', 24.85), ('CELL', 35.46), ('CHEESE', 3.72), ('CHERRIES', 23.16), ('CHIPS', 27.58), ('COCONUT', 58.99), ('COFFEE', 26.11), ('COOKIES', 57.1), ('DEODRANT', 15.19), ('EGGS', 24.79), ('FRESHNER', 52.61), ('GRAPES', 0.75), ('MAT', 49.74), ('MILK', 11.27), ('MINT', 20.89), ('OIL', 9.22), ('ONIONS', 55.16), ('PASTE', 106.28), ('PEPPER', 15.72), ('SOAP', 13.48), ('TEA', 36.9), ('TISSUES', 29.26), ('TOMATOES', 34.35), ('TOWEL', 69.35), ('YOGURT', 66.67)]
>>> prices = _
>>> prices = dict(prices)
>>> prices
{'ALMOND': 49.16, 'APPLES': 28.47, 'BANANA': 24.22, 'BREAD': 44.85, 'BUNS': 51.94, 'BUTTER': 24.85, 'CELL': 35.46, 'CHEESE': 3.72, 'CHERRIES': 23.16, 'CHIPS': 27.58, 'COCONUT': 58.99, 'COFFEE': 26.11, 'COOKIES': 57.1, 'DEODRANT': 15.19, 'EGGS': 24.79, 'FRESHNER': 52.61, 'GRAPES': 0.75, 'MAT': 49.74, 'MILK': 11.27, 'MINT': 20.89, 'OIL': 9. 22, 'ONIONS': 55.16, 'PASTE': 106.28, 'PEPPER': 15.72, 'SOAP': 13.48, 'TEA': 36.9, 'TISSUES': 29.26, 'TOMATOES': 34.35, 'TOWEL': 69.35, 'YOGURT': 66.67}
>>> quit()
Monte-Aire:Food_Mart (main) surf$ python report.py
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
Monte-Aire:Food_Mart (main) surf$ python invcost.py
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
Total cost: 44671.15
Monte-Aire:Food_Mart (main) surf$ python invcost.py
Total cost: 44671.15
Monte-Aire:Food_Mart (main) surf$ python report.py
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
Monte-Aire:Food_Mart (main) surf$ python
Monte-Aire:Food_Mart (main) surf$ python report.py
Usage: report.py invfile pricefile
Monte-Aire:Food_Mart (main) surf$ mkdir
usage: mkdir [-pv] [-m mode] directory_name ...
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory.csv Data/prices.csv
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.csv
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL         50       9.22     -17.88
     BREAD        250      44.85       1.70
      MINT         25      20.89     -29.26
     PASTE        125     106.28      54.18
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from fileparse import parse_csv
>>> with open('Data/inventory.csv') as FH:
...     inv = parse_csv(FH, types=[str, int, float])
...
>>> inv
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price' : 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 200, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>> import gzip
>>> with gzip.open('Data/inventory.csv.gz', 'rt') as FH:
...     inv = parse_csv(FH, types=[str, int, float])
...
>>> inv
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price': 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 200, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python invcost.py
Total cost: 44671.15
Monte-Aire:Food_Mart (main) surf$ python report.py
Usage: report.py invfile pricefile
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.cs
v
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL         50       9.22     -17.88
     BREAD        250      44.85       1.70
      MINT         25      20.89     -29.26
     PASTE        125     106.28      54.18
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python -i report.py
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 65, in <module>
    main(sys.argv)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", li
ne 55, in main
    raise SystemExit(f'Usage: {args[0]} invfile pricefile')
SystemExit: Usage: report.py invfile pricefile
>>> inv = read_inventory('Data/inventory.csv')
>>> inv
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price'
: 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 20
0, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', '
quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>> from pprint import pprint
>>> pprint(inv)
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100}]
>>> prod_names = [ pr['name'] for pr in inv ]
>>> prod_names
['OIL', 'PASTE', 'CELL', 'MINT', 'SOAP', 'MINT', 'PASTE']
>>>
>>> inv = read_inventory('Data/inventory.csv')
>>> pprint(inv)
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100}]
>>>
>>> prod_names = [ pr['name'] for pr in inv ]
>>> prod_names
['OIL', 'PASTE', 'CELL', 'MINT', 'SOAP', 'MINT', 'PASTE']
>>>
>>> # products whose price is > 60
>>> costly = [ pr['name'] for pr in inv if pr['price'] > 60 ]
>>> costly
['PASTE', 'CELL', 'MINT', 'PASTE']
>>> # products whose price is > 60 and have at least 100 units
>>> costly = [ pr['name'] for pr in inv if pr['price'] > 60 and pr['quant'] >= 100 ]
>>> costly
['CELL', 'PASTE']
>>> # Declarative style of programming
>>> # DB : SQL like syntax
>>>
>>>
>>> # list of Cost of each product in inventory
>>> [ pr['quant'] * pr['price'] for pr in inv ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995
, 7044.0]
>>> sum(_)
44671.15
>>>
>>> # Total cost of inventory
>>> sum( [ pr['quant'] * pr['price'] for pr in inv ] )
44671.15
>>>
>>> # Like Map and Reduce for Big Data
>>> total = sum( [ pr['quant'] * pr['price'] for pr in inv ] )
>>> total
44671.15
>>> # Calculate the latest cost of inventory : using latest price from read_prices
>>> prices = read_prices('Data/prices.csv')
>>> latest = sum( [ pr['quant'] * prices[ pr['name'] ] for pr in inv]  )
>>> latest
28686.1
>>> latest - total
-15985.050000000003
>>>
>>> prod_names
['OIL', 'PASTE', 'CELL', 'MINT', 'SOAP', 'MINT', 'PASTE']
>>>
>>> # Fetch all the unique product names in inventory
>>> set(prod_names)
{'CELL', 'MINT', 'OIL', 'SOAP', 'PASTE'}
>>>
>>> names = { pr['name'] for pr in inv }
>>> names
{'CELL', 'MINT', 'OIL', 'SOAP', 'PASTE'}
>>>
>>> # Dictionary representing quantity for every product
>>> sales = { pr['name']:0 for pr in inv }
>>> sales
{'OIL': 0, 'PASTE': 0, 'CELL': 0, 'MINT': 0, 'SOAP': 0}
>>> sales = {name:0 for name in names}
>>> sales
{'CELL': 0, 'MINT': 0, 'OIL': 0, 'SOAP': 0, 'PASTE': 0}
>>> # Tabulate quantity for each product in inventory
>>> for prod in inv:
...     sales[prod['name']] += prod['quant']
...
>>> sales
{'CELL': 150, 'MINT': 250, 'OIL': 100, 'SOAP': 95, 'PASTE': 150}
>>> pprint(inv)
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100}]
>>> # Latest price for each product
>>> latest = {name: prices[name] for name in names}
>>> latest
{'CELL': 35.46, 'MINT': 20.89, 'OIL': 9.22, 'SOAP': 13.48, 'PASTE': 106.28}
>>>
>>> scores = [3, 24, 189, 99, 115, 147, 76, 729, 100, 50]
>>> len(scores)
10
>>> for num in scores:
...     if num > 99:
...             scores.remove(num)
...
>>> scores
[3, 24, 99, 147, 76, 100, 50]
>>> # Never iterate on a list that is getting modified
>>>
>>> scores = [3, 24, 189, 99, 115, 147, 76, 729, 100, 50]
>>> tmp = scores[:]
>>> for num in tmp:
...     if num > 99:
...             scores.remove(num)
...
>>> scores
[3, 24, 99, 76, 50]
>>> scores = [3, 24, 189, 99, 115, 147, 76, 729, 100, 50]
>>> for num in scores[:]:
...     if num > 99:
...             scores.remove(num)
...
>>> scores
[3, 24, 99, 76, 50]
>>> tmp = scores.copy()
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python -i new.py
>>> a = Player(1, 3)
>>> a.x
1
>>> a.y
3
>>> a.health
100
>>> a.move(10, 20)
>>> a.x
11
>>> a.y
23
>>> a.move(10, 20)
>>> Player.move(a, 10, 20)
>>> quit()
Monte-Aire:Food_Mart (main) surf$ python -i new.py
>>>
>>> a = Player(1, 3)
>>> a.move(10, 20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Player.move() takes 2 positional arguments but 3 were given
>>> Player.move(a, 10, 20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Player.move() takes 2 positional arguments but 3 were given
>>>
>>>

>>> x = "Hello"
>>> y = "world"
>>>
>>> x + y
'Helloworld'
>>>
>>> 10 + 20
30
>>> x + y
'Helloworld'
>>> x.__add__(y)
'Helloworld'
>>>
>>> type(x)
<class 'str'>
>>> type(a)
<class '__main__.Player'>
>>> x + y
'Helloworld'
>>> str.__add__(x, y)
'Helloworld'
>>> c = Player(4, 6)
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import product
>>> a = product.Product('MINT', 100, 490.10)
>>> a.name
'MINT'
>>> a.quant
100
>>> a.price
490.1
>>> b = product.Product('OIL', 50, 122.34)
>>> c = product.Product('PASTE', 75, 91.75)
>>> b.quant * b.price
6117.0
>>> 50 * 122.34
6117.0
>>> c.quant * c.price
6881.25
>>> inv = [a, b, c]
>>> inv
[<product.Product object at 0x102cc1b20>, <product.Product object at 0x102b59820>, <product.Product object at 0x102b5b650>]
>>> for pr in inv:
...     print(f'{pr.name:>10} {pr.quant:>10} {pr.price:>10.2f}')
...
      MINT        100     490.10
       OIL         50     122.34
     PASTE         75      91.75
>>> quit()
Monte-Aire:Food_Mart (main) surf$ python
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

>>> import product
>>> a = product.Product('MINT', 100, 490.10)
>>> a.cost()
49010.0
>>> quit()
Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import product
>>> a = product.Product('MINT', 100, 490.10)
>>> a.cost()
49010.0
>>> a.quant
100
>>> a.sell(25)
>>> a.quant
75
>>> a.cost()
36757.5
>>> 75 * 490.1
36757.5
>>>
>>> from fileparse import parse_csv
>>> with open('Data/inventory.csv') as FH:
...     invdicts = parse_csv(FH, types=[str, int, float])
...
>>> invdicts
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price' : 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 200, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', 'quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>> # List of Product instances
>>> inv = [ product.Product(pr['name'], pr['quant'], pr['price']) for pr in invdicts
]
>>> inv
[<product.Product object at 0x101196570>, <product.Product object at 0x101196600>, <p roduct.Product object at 0x101196630>, <product.Product object at 0x101196660>, <product.Product object at 0x101196690>, <product.Product object at 0x1011966c0>, <product.Product object at 0x1011966f0>]
>>> p = inv[0]
>>> p
<product.Product object at 0x101196570>
>>> p.name
'OIL'
>>> p.quant
100
>>> p.price
32.2
>>> p.cost()
3220.0000000000005
>>> [ p.cost() for p in inv ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>> sum([ p.cost() for p in inv ])
44671.15
>>>
>>> sum( p.cost() for p in inv )
44671.15
>>> # Generator Expression : ()
>>> all_costs = (p.cost() for p in inv)
>>> all_costs
<generator object <genexpr> at 0x100ecb920>
>>> next(all_costs)
3220.0000000000005
>>> next(all_costs)
4555.0
>>> next(all_costs)
12516.0
>>> all_costs = (p.cost() for p in inv)
>>> sum(all_costs)
44671.15
>>> quit()
Monte-Aire:Food_Mart (main) surf$
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.cs
v
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", line 68, in <module>
    main(sys.argv)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", line 62, in main
    inventory_report(invfile, pricefile)
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", line 52, in inventory_report
    report = make_report(inventory, prices)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/report.py", line 30, in make_report
    name   = pr['name']
             ~~^^^^^^^^
TypeError: 'Product' object is not subscriptable
Monte-Aire:Food_Mart (main) surf$ python report.py Data/inventory2.csv Data/prices.csv
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL         50       9.22     -17.88
     BREAD        250      44.85       1.70
      MINT         25      20.89     -29.26
     PASTE        125     106.28      54.18
Monte-Aire:Food_Mart (main) surf$ python invcost.py
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/invcost.py", l
ine 22, in <module>
    cost = inventory_cost(filename)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/invcost.py", l
ine 13, in inventory_cost
    total_cost += pr['quant'] * pr['price']
                  ~~^^^^^^^^^
TypeError: 'Product' object is not subscriptable
Monte-Aire:Food_Mart (main) surf$ python invcost.py
Total cost: 44671.15
Monte-Aire:Food_Mart (main) surf$ python invcost.py
Total cost: 44671.15
Monte-Aire:Food_Mart (main) surf$ cd ../DB_Access/
Monte-Aire:DB_Access (main) surf$ ls
db_prog.py              students_info_db.sqlite
Monte-Aire:DB_Access (main) surf$ ls -ltr
total 40
-rw-r--r--  1 surf  staff  16384 Jun  3 23:26 students_info_db.sqlite
-rw-r--r--  1 surf  staff    484 Jun  3 23:27 db_prog.py
Monte-Aire:DB_Access (main) surf$ python db_prog.py
Monte-Aire:DB_Access (main) surf$ python db_prog.py
Venkat       4 Python
Amit         0 Python
Girish       8 Shell Scripting
Sumit        0 Shell Scripting
Nipun        3 Python
Monte-Aire:DB_Access (main) surf$ ls
db_prog.py              students_info_db.sqlite
Monte-Aire:DB_Access (main) surf$ python db_prog.py
Venkat       4 Python
Girish       8 Shell Scripting
Nipun        3 Python
Monte-Aire:DB_Access (main) surf$ python db_prog.py
Nipun        3 Python
Venkat       4 Python
Girish       8 Shell Scripting
Monte-Aire:DB_Access (main) surf$
Monte-Aire:DB_Access (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> colors = { 'Red', 'Blue', 'Green', 'Red', 'Black'}
>>> len(colors)
4
>>> colors
{'Black', 'Blue', 'Red', 'Green'}
>>>
>>> if "day" > "night":
...     print("Summer")
... else:
...     print("Winter")
...
Winter
>>> if "daylight" > "night":
...     print("Summer")
... else:
...     print("Winter")
...
Winter
>>> one = "2#3"
>>> two = 2#3
>>> print(one * two)
2#32#3
>>> # comment
>>> 2 #3
2
>>> 2#3
2
>>> one * 2
'2#32#3'
>>>

# Copyright 2024 Sarfraaz Ahmed. All rights reserved.
