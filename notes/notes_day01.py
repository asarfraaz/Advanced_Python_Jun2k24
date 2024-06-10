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

(py312_env) Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> FH = open("Data/inventory.csv")
>>> for line in FH:
...     print(line)
...     break
...
name,quant,price

>>> line
'name,quant,price\n'
>>> type(line)
<class 'str'>
>>> line.split(',')
['name', 'quant', 'price\n']
>>>
>>> line.split(',')[1]
'quant'
>>> line = '"OIL",100,32.20'
>>> line.split(',')[1]
'100'
>>> line.split(',')[2]
'32.20'
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ ls
Data       invcost.py
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py
Total cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> r = range(10)
>>> r
range(0, 10)
>>> print(r)
range(0, 10)
>>> list(r)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> r = range(10)
>>> # range(10) : Generator Function
>>> # r : Generator Object
>>> z = iter(r)
>>> next(z)
0
>>> next(z)
1
>>> next(z)
2
>>> next(z)
3
>>> for num in z:
...     print(num)
...
4
5
6
7
8
9
>>> next(z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> r = range(5)
>>> for num in r:
...     print(num)
...
0
1
2
3
4
>>> # Iterator Protocol
>>>
>>> scores = [12, 45, 78, 34, 56]
>>> z = iter(scores)
>>> type(scores)
<class 'list'>
>>> type(z)
<class 'list_iterator'>
>>> next(z)
12
>>> next(z)
45
>>> next(z)
78
>>> next(z)
34
>>> next(z)
56
>>> next(z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for num in scores:
...     print(num)
...
12
45
78
34
56
>>> scores
[12, 45, 78, 34, 56]
>>>
>>> FH = open("Data/inventory.csv")
>>> z = iter(FH)
>>> type(FH)
<class '_io.TextIOWrapper'>
>>> type(z)
<class '_io.TextIOWrapper'>
>>> next(z)
'name,quant,price\n'
>>> next(z)
'"OIL",100,32.20\n'
>>> next(z)
'"PASTE",50,91.10\n'
>>> next(z)
'"CELL",150,83.44\n'
>>> next(z)
'"MINT",200,51.23\n'
>>> next(z)
'"SOAP",95,40.37\n'
>>> next(z)
'"MINT",50,65.10\n'
>>> next(z)
'"PASTE",100,70.44\n'
>>> next(z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> FH = open("Data/inventory.csv")
>>> for line in FH:
...     print(line)
...
name,quant,price

"OIL",100,32.20

"PASTE",50,91.10

"CELL",150,83.44

"MINT",200,51.23

"SOAP",95,40.37

"MINT",50,65.10

"PASTE",100,70.44

>>> FH = open("Data/inventory.csv")
>>> next(FH)
'name,quant,price\n'
>>> next(FH)
'"OIL",100,32.20\n'
>>> next(FH)
'"PASTE",50,91.10\n'
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py
Total cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

>>> FH = open("Data/inventory.csv")
>>> headers = next(FH)
>>> headers
'name,quant,price\n'
>>> line = next(FH)
>>> line
'"OIL,PURE",100,32.20\n'
>>> line.split(',')[1]
'PURE"'
>>> import csv
>>>
>>> import csv
>>> FH = open("Data/inventory.csv")
>>> data = csv.reader(FH)
>>> data
<_csv.reader object at 0x102a1a490>
>>> headers2 = next(data)
>>> headers2
['name', 'quant', 'price']
>>> headers
'name,quant,price\n'
>>> line_data = next(data)
>>> line_data
['OIL,PURE', '100', '32.20']
>>> line_data[1]
'100'
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py
Total cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py
Total cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$ python -i invcost.py
Total cost: 44671.15
>>> inv_cost = inventory_cost('Data/inventory.csv')
>>> inv_cost
44671.15
>>> inv_cost = inventory_cost('Data/inventory2.csv')
>>> inv_cost
19908.75
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/inventory.csv
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/inventory.csv
Total cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/inventory2.csv
Total cost: 19908.75
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py                 Total
 cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ ls
Data       add.py     invcost.py
(py312_env) Monte-Aire:Food_Mart (main) surf$ python add.py 10 20
Total: 1020
(py312_env) Monte-Aire:Food_Mart (main) surf$ python add.py 10 20
Total: 30
(py312_env) Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> int("100")
100
>>> int('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> int('32.20')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '32.20'
>>> int("five")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'five'
>>> int("123")
123
>>> float("32.20")
32.2
>>> float("32.20 gms")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '32.20 gms'
>>> help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Built-in subclasses:
 |      bool
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |

 ............

 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rlshift__(self, value, /)

>>> float("32.20 gms")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '32.20 gms'
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
Traceback (most recent call last):
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/invcost.py", l
ine 28, in <module>
    cost = inventory_cost(filename)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/surf/work/github/priv/Advanced_Python_Jun2k24/Food_Mart/invcost.py", l
ine 17, in inventory_cost
    quant = int(row[1])
            ^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: ''
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
Bad row ['MINT', '', '51.23']
Bad row ['PASTE', '', '70.44']
Total cost: 27381.15
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py                 Total
 cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ ls
Data       add.py     invcost.py report.py
(py312_env) Monte-Aire:Food_Mart (main) surf$ python -i report.py
>>> inventory = read_inventory('Data/inventory.csv')
>>> inventory
[('OIL', 100, 32.2), ('PASTE', 50, 91.1), ('CELL', 150, 83.44), ('MINT', 200, 51.23),
 ('SOAP', 95, 40.37), ('MINT', 50, 65.1), ('PASTE', 100, 70.44)]
>>> from pprint import pprint
>>> # Pretty print
>>> pprint(inventory)
[('OIL', 100, 32.2),
 ('PASTE', 50, 91.1),
 ('CELL', 150, 83.44),
 ('MINT', 200, 51.23),
 ('SOAP', 95, 40.37),
 ('MINT', 50, 65.1),
 ('PASTE', 100, 70.44)]
>>> inventory[0]
('OIL', 100, 32.2)
>>> inventory[1]
('PASTE', 50, 91.1)
>>> inventory[1][1]
50
>>> inventory[1][2]
91.1
>>> p = inventory[1]
>>> p
('PASTE', 50, 91.1)
>>>
>>> pprint(inventory)
[('OIL', 100, 32.2),
 ('PASTE', 50, 91.1),
 ('CELL', 150, 83.44),
 ('MINT', 200, 51.23),
 ('SOAP', 95, 40.37),
 ('MINT', 50, 65.1),
 ('PASTE', 100, 70.44)]
>>> p = inventory[1]
>>> p
('PASTE', 50, 91.1)
>>> p[1] * p[2]
4555.0
>>> 50 * 91.1
4555.0
>>> total = 0.0
>>> for p in inventory:
...     total += p[1] * p[2]
...
>>> total
44671.15
>>>

>>> p
('PASTE', 100, 70.44)
>>>
>>> name, quant, price = p
>>> name
'PASTE'
>>> quant
100
>>> price
70.44
>>> name = "Sam"
>>> a, b, c = name
>>> a
'S'
>>> b
'a'
>>> c
'm'
>>> name = "Sample"
>>> a, b, c = name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 3)
>>> # Tuple unpacking
>>>
>>> inventory
[('OIL', 100, 32.2), ('PASTE', 50, 91.1), ('CELL', 150, 83.44), ('MINT', 200, 51.23),
 ('SOAP', 95, 40.37), ('MINT', 50, 65.1), ('PASTE', 100, 70.44)]
>>>
>>> total = 0.0
>>> for name,quant,price in inventory:
...     total += quant * price
...
>>> total
44671.15
>>> # Readability counts a lot
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ python -i report.py
>>>
>>> inventory = read_inventory('Data/inventory.csv')
>>> inventory
[{'name': 'OIL', 'quant': 100, 'price': 32.2}, {'name': 'PASTE', 'quant': 50, 'price'
: 91.1}, {'name': 'CELL', 'quant': 150, 'price': 83.44}, {'name': 'MINT', 'quant': 20
0, 'price': 51.23}, {'name': 'SOAP', 'quant': 95, 'price': 40.37}, {'name': 'MINT', '
quant': 50, 'price': 65.1}, {'name': 'PASTE', 'quant': 100, 'price': 70.44}]
>>> from pprint import pprint
>>> pprint(inventory)
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100}]
>>>
>>> p = inventory[0]
>>> p
{'name': 'OIL', 'quant': 100, 'price': 32.2}
>>> p['quant']
100
>>> p['price']
32.2
>>> p['quant'] * p['price']
3220.0000000000005
>>> total = 0.0
>>> for pr in inventory:
...     total += pr['quant'] * pr['price']
...
>>> total
44671.15
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python -i report.py
>>> prices = read_prices('Data/prices.csv')
>>> prices['TEA']
36.9
>>> prices['OIL']
9.22
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ python report.py
(py312_env) Monte-Aire:Food_Mart (main) surf$ python report.py
Total Gain/Loss: -15985.050000000003
(py312_env) Monte-Aire:Food_Mart (main) surf$ python data_stats.py
Average price 61.98285714285715
Std Dev: 21.829700497476452
(py312_env) Monte-Aire:Food_Mart (main) surf$ python data_stats.py
Average price 61.98285714285715
Std Dev: 21.829700497476452
(py312_env) Monte-Aire:Food_Mart (main) surf$ python quant_med.py
Median 100.0
(py312_env) Monte-Aire:Food_Mart (main) surf$ python quant_med.py
Median 87.5
(py312_env) Monte-Aire:Food_Mart (main) surf$ python quant_med.py ytho
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python -i report.py
>>> inv = read_inventory('Data/inventory.csv')
>>> prices = read_prices('Data/prices.csv')
>>> report = make_report(inv, prices)
>>> for r in report:
...     print(r)
...
('OIL', 100, 9.22, -22.980000000000004)
('PASTE', 50, 106.28, 15.180000000000007)
('CELL', 150, 35.46, -47.98)
('MINT', 200, 20.89, -30.339999999999996)
('SOAP', 95, 13.48, -26.889999999999997)
('MINT', 50, 20.89, -44.209999999999994)
('PASTE', 100, 106.28, 35.84)
>>>
>>> r
('PASTE', 100, 106.28, 35.84)
>>> print('%s %d %f %f' % r)
PASTE 100 106.280000 35.840000
>>> print('%s %d %f.2 %f.2' % r)
PASTE 100 106.280000.2 35.840000.2
>>> print('%s %d %f0.2 %f0.2' % r)
PASTE 100 106.2800000.2 35.8400000.2
>>> print('%s %d %.2f %.2f' % r)
PASTE 100 106.28 35.84
>>> print('%10s %10d %10.2f %10.2f' % r)
     PASTE        100     106.28      35.84
>>> r = ('OIL', 40, 123.4, -23.5)
>>> print('%10s %10d %10.2f %10.2f' % r)
       OIL         40     123.40     -23.50
>>> for r in report:
...     print('%10s %10d %10.2f %10.2f' % r)
...
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
>>> headers = ('Name', 'Quantity', 'Price', 'Change')
>>> print('%10s %10s %10s %10s' % headers)
      Name   Quantity      Price     Change
>>> #------ --------- ---------- ----------
>>> '-' * 10
'----------'
>>> ['-' * 10] * 4
['----------', '----------', '----------', '----------']
>>> dashes = tuple(['-' * 10] * 4)
>>> print('%10s %10s %10s %10s' % headers)
      Name   Quantity      Price     Change
>>> print('%10s %10s %10s %10s' % dashes)
---------- ---------- ---------- ----------
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ python report.py
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
(py312_env) Monte-Aire:Food_Mart (main) surf$ 
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> name = "Ajay"
>>> print(name)
Ajay
>>> print("My name is", name)
My name is Ajay
>>> print("My name is %s" % name)
My name is Ajay
>>> lname = "Tim"
>>> print("My name is %s : %s" % (name, lname))
My name is Ajay : Tim
>>> print("My name is {} : {}".format((name, lname))
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("My name is {} : {}".format(name, lname))
My name is Ajay : Tim
>>>
>>>
>>> print("My name is %s : %s" % (name))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not enough arguments for format string
>>> print("My name is %s : %s" % (name, name, name))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not all arguments converted during string formatting
>>> # Logging
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
Bad row ['MINT', '', '51.23']
Bad row ['PASTE', '', '70.44']
Total cost: 27381.15
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
Row 3 : Couldn't convert: ['MINT', '', '51.23']
Row 6 : Couldn't convert: ['PASTE', '', '70.44']
Total cost: 27381.15
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
Row 4 : Couldn't convert: ['MINT', '', '51.23']
Row 7 : Couldn't convert: ['PASTE', '', '70.44']
Total cost: 27381.15
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> headers1 = ['name', 'quant', 'price']
>>> row1 = ['OIL', 100, 490.1]
>>> cost1 = row1[1] * row1[2]
>>> cost1
49010.0
>>>
>>> headers2 = ['quant', 'price', 'name']
>>> row2 = [100, 490.1, 'OIL']
>>> cost2 = row2[1] * row2[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float''
>>> row2[1]
490.1
>>> row2[2]
'OIL'
>>>
>>> drow1 = dict(zip(headers1, row1))
>>> drow1
{'name': 'OIL', 'quant': 100, 'price': 490.1}
>>> drow1['quant'] * drow1['price']
49010.0
>>>
>>> drow2 = dict(zip(headers2, row2))
>>> drow2
{'quant': 100, 'price': 490.1, 'name': 'OIL'}
>>> drow2['quant'] * drow2['price']
49010.0
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/inventory.csv
Total cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/inventory.csv
Total cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/inventorydate.cs
v
Total cost: 44671.15
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python report.py
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python report.py
      Name   Quantity      Price     Change
---------- ---------- ---------- ----------
       OIL        100       9.22     -22.98
     PASTE         50     106.28      15.18
      CELL        150      35.46     -47.98
      MINT        200      20.89     -30.34
      SOAP         95      13.48     -26.89
      MINT         50      20.89     -44.21
     PASTE        100     106.28      35.84
(py312_env) Monte-Aire:Food_Mart (main) surf$
(py312_env) Monte-Aire:Food_Mart (main) surf$ python
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0
.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> friends = ['Manjunath', 'Sam', 'Vishal', 'Ajay', 'Mohan']
>>> friends
['Manjunath', 'Sam', 'Vishal', 'Ajay', 'Mohan']
>>> friends = ['Raghavendra', 'Sam', 'Vishal', 'Ajay', 'Mohan']
>>> friends
['Raghavendra', 'Sam', 'Vishal', 'Ajay', 'Mohan']
>>> sorted(friends)
['Ajay', 'Mohan', 'Raghavendra', 'Sam', 'Vishal']
>>> friends
['Raghavendra', 'Sam', 'Vishal', 'Ajay', 'Mohan']
>>> # a .. m .. l .. y .. n
>>> # a .. l .. m .. n .. y
>>> # Raghavendra, Vishal, Sam, Mohan, Ajay
>>> def get_last_char(name):
...     return name[-1]
...
>>> get_last_char('Sam')
'm'
>>> sorted(friends, key=get_last_char)
['Raghavendra', 'Vishal', 'Sam', 'Mohan', 'Ajay']
>>>


>>> friends
['Raghavendra', 'Sam', 'Vishal', 'Ajay', 'Mohan']
>>>
>>> # Sort based on number of chars in the name
>>> friends
['Raghavendra', 'Sam', 'Vishal', 'Ajay', 'Mohan']
>>> # 11 .. 3 .. 6 .. 4 .. 5
>>> # 3 .. 4 .. 5 .. 6 .. 11
>>> # Sam, Ajay, Mohan, Vishal, Raghavendra
>>>
>>> def get_nchars(name):
...     return len(name)
...
>>> get_nchars('Sam')
3
>>> sorted(friends, key=get_nchars)
['Sam', 'Ajay', 'Mohan', 'Vishal', 'Raghavendra']
>>> min(friends, key=get_nchars)
'Sam'
>>> max(friends, key=get_nchars)
'Raghavendra'
>>> max(friends, key=len)
'Raghavendra'
>>> max(friends, key=get_last_char)
'Ajay'
>>> def get_last_char(name):
...     return name[-1]
...
>>> max(friends, key=lambda name:name[-1])
'Ajay'
>>> sorted(friends, key=lambda name:name[-1])
['Raghavendra', 'Vishal', 'Sam', 'Mohan', 'Ajay']
>>> sorted(friends, key=lambda x:x[-1])
['Raghavendra', 'Vishal', 'Sam', 'Mohan', 'Ajay']
>>> sorted(friends, key=lambda x:x[-2])
['Sam', 'Vishal', 'Ajay', 'Mohan', 'Raghavendra']
>>> sorted(friends, key=lambda x:x[-3])
['Sam', 'Raghavendra', 'Vishal', 'Mohan', 'Ajay']
>>>
>>> # Lambda functions : nameless functions
>>> m = lambda x: x + 5
>>> m(10)
15
>>> def m(x):
...     return x + 5
...
>>> n = lambda x, y: x + y
>>> n(10, 20)
30
>>>
>>> p = lambda : "Hello World"
>>> p()
'Hello World'
>>> quit()
(py312_env) Monte-Aire:Food_Mart (main) surf$ 
(py312_env) Monte-Aire:Food_Mart (main) surf$ python -i report.py
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
>>> inv = read_inventory('Data/inventory.csv')
>>> from pprint import pprint
>>> pprint(inv)
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100}]
>>> def get_prod_name(pr):
...     return pr['name']
...
>>> pprint(sorted(inv, key=get_prod_name))
[{'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95}]
>>> pprint(sorted(inv, key=lambda pr: pr['name'] ))
[{'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95}]
>>>
>>> pprint(sorted(inv, key=lambda pr: pr['name'] ))
[{'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95}]
>>> pprint(sorted(inv, key=lambda pr: pr['quant'] ))
[{'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200}]
>>> pprint(sorted(inv, key=lambda pr: pr['price'] ))
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50}]
>>>
>>> pprint(sorted(inv, key=lambda pr: pr['price'] ))
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50}]
>>> # Sort based on cost of the product
>>> pprint(sorted(inv, key=lambda pr: pr['price'] * pr['quant'] ))
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'CELL', 'price': 83.44, 'quant': 150}]
>>>
>>>
>>>
>>> inv = read_inventory('Data/inventory.csv')
>>> from pprint import pprint
>>> pprint(inv)
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100}]
>>> pprint(sorted(inv, key=lambda pr:pr['quant']* pr['price']))
[{'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'MINT', 'price': 51.23, 'quant': 200},
 {'name': 'CELL', 'price': 83.44, 'quant': 150}]
>>> pprint(max(inv, key=lambda pr:pr['quant']* pr['price']))
{'name': 'CELL', 'price': 83.44, 'quant': 150}
>>>


>>> pprint(sorted(inv, key=lambda pr:pr['quant']))
[{'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200}]
>>> pprint(sorted(inv, key=lambda pr:(pr['quant'], pr['price']))
... )
[{'name': 'MINT', 'price': 65.1, 'quant': 50},
 {'name': 'PASTE', 'price': 91.1, 'quant': 50},
 {'name': 'SOAP', 'price': 40.37, 'quant': 95},
 {'name': 'OIL', 'price': 32.2, 'quant': 100},
 {'name': 'PASTE', 'price': 70.44, 'quant': 100},
 {'name': 'CELL', 'price': 83.44, 'quant': 150},
 {'name': 'MINT', 'price': 51.23, 'quant': 200}]
>>>
>>> quit()
(py312_env) Monte-Aire:day01 (main) surf$ pip install jupyter
Collecting jupyter
  Using cached jupyter-1.0.0-py2.py3-none-any.whl.metadata (995 bytes)
Collecting notebook (from jupyter)
  Using cached notebook-7.2.0-py3-none-any.whl.metadata (10 kB)
Collecting qtconsole (from jupyter)
  Using cached qtconsole-5.5.2-py3-none-any.whl.metadata (5.1 kB)
Collecting jupyter-console (from jupyter)
  Using cached jupyter_console-6.6.3-py3-none-any.whl.metadata (5.8 kB)
Collecting nbconvert (from jupyter)
  Using cached nbconvert-7.16.4-py3-none-any.whl.metadata (8.5 kB)
Collecting ipykernel (from jupyter)
  Using cached ipykernel-6.29.4-py3-none-any.whl.metadata (6.3 kB)
Collecting ipywidgets (from jupyter)
  Downloading ipywidgets-8.1.3-py3-none-any.whl.metadata (2.4 kB)
Collecting appnope (from ipykernel->jupyter)
  Using cached appnope-0.1.4-py2.py3-none-any.whl.metadata (908 bytes)
Collecting comm>=0.1.1 (from ipykernel->jupyter)
  Using cached comm-0.2.2-py3-none-any.whl.metadata (3.7 kB)
Collecting debugpy>=1.6.5 (from ipykernel->jupyter)
  Using cached debugpy-1.8.1-cp312-cp312-macosx_11_0_universal2.whl.metadata (1.1 kB)
Requirement already satisfied: ipython>=7.23.1 in /Users/surf/work/python/py312_env/l
ib/python3.12/site-packages (from ipykernel->jupyter) (8.22.2)
Collecting jupyter-client>=6.1.12 (from ipykernel->jupyter)
  Downloading jupyter_client-8.6.2-py3-none-any.whl.metadata (8.3 kB)
Collecting jupyter-core!=5.0.*,>=4.12 (from ipykernel->jupyter)
  Using cached jupyter_core-5.7.2-py3-none-any.whl.metadata (3.4 kB)
Requirement already satisfied: matplotlib-inline>=0.1 in /Users/surf/work/python/py31
2_env/lib/python3.12/site-packages (from ipykernel->jupyter) (0.1.6)
Collecting nest-asyncio (from ipykernel->jupyter)
  Using cached nest_asyncio-1.6.0-py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: packaging in /Users/surf/work/python/py312_env/lib/pyt
hon3.12/site-packages (from ipykernel->jupyter) (24.0)
Collecting psutil (from ipykernel->jupyter)
  Using cached psutil-5.9.8-cp38-abi3-macosx_11_0_arm64.whl.metadata (21 kB)
Collecting pyzmq>=24 (from ipykernel->jupyter)
  Using cached pyzmq-26.0.3-cp312-cp312-macosx_10_15_universal2.whl.metadata (6.1 kB)
Requirement already satisfied: tornado>=6.1 in /Users/surf/work/python/py312_env/lib/
python3.12/site-packages (from ipykernel->jupyter) (6.4)
Requirement already satisfied: traitlets>=5.4.0 in /Users/surf/work/python/py312_env/
lib/python3.12/site-packages (from ipykernel->jupyter) (5.14.1)
Collecting widgetsnbextension~=4.0.11 (from ipywidgets->jupyter)
  Downloading widgetsnbextension-4.0.11-py3-none-any.whl.metadata (1.6 kB)
Collecting jupyterlab-widgets~=3.0.11 (from ipywidgets->jupyter)
  Downloading jupyterlab_widgets-3.0.11-py3-none-any.whl.metadata (4.1 kB)
Requirement already satisfied: prompt-toolkit>=3.0.30 in /Users/surf/work/python/py31
2_env/lib/python3.12/site-packages (from jupyter-console->jupyter) (3.0.43)
Requirement already satisfied: pygments in /Users/surf/work/python/py312_env/lib/pyth
on3.12/site-packages (from jupyter-console->jupyter) (2.17.2)
Collecting beautifulsoup4 (from nbconvert->jupyter)
  Using cached beautifulsoup4-4.12.3-py3-none-any.whl.metadata (3.8 kB)
Collecting bleach!=5.0.0 (from nbconvert->jupyter)
  Using cached bleach-6.1.0-py3-none-any.whl.metadata (30 kB)
Collecting defusedxml (from nbconvert->jupyter)
  Using cached defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Requirement already satisfied: jinja2>=3.0 in /Users/surf/work/python/py312_env/lib/p
ython3.12/site-packages (from nbconvert->jupyter) (3.0.3)
Collecting jupyterlab-pygments (from nbconvert->jupyter)
  Using cached jupyterlab_pygments-0.3.0-py3-none-any.whl.metadata (4.4 kB)
Requirement already satisfied: markupsafe>=2.0 in /Users/surf/work/python/py312_env/l
ib/python3.12/site-packages (from nbconvert->jupyter) (2.1.1)
Collecting mistune<4,>=2.0.3 (from nbconvert->jupyter)
  Using cached mistune-3.0.2-py3-none-any.whl.metadata (1.7 kB)
Collecting nbclient>=0.5.0 (from nbconvert->jupyter)
  Using cached nbclient-0.10.0-py3-none-any.whl.metadata (7.8 kB)
Collecting nbformat>=5.7 (from nbconvert->jupyter)
  Using cached nbformat-5.10.4-py3-none-any.whl.metadata (3.6 kB)
Collecting pandocfilters>=1.4.1 (from nbconvert->jupyter)
  Using cached pandocfilters-1.5.1-py2.py3-none-any.whl.metadata (9.0 kB)
Collecting tinycss2 (from nbconvert->jupyter)
  Using cached tinycss2-1.3.0-py3-none-any.whl.metadata (3.0 kB)
Collecting jupyter-server<3,>=2.4.0 (from notebook->jupyter)
  Downloading jupyter_server-2.14.1-py3-none-any.whl.metadata (8.4 kB)
Collecting jupyterlab-server<3,>=2.27.1 (from notebook->jupyter)
  Downloading jupyterlab_server-2.27.2-py3-none-any.whl.metadata (5.9 kB)
Collecting jupyterlab<4.3,>=4.2.0 (from notebook->jupyter)
  Downloading jupyterlab-4.2.1-py3-none-any.whl.metadata (16 kB)
Collecting notebook-shim<0.3,>=0.2 (from notebook->jupyter)
  Using cached notebook_shim-0.2.4-py3-none-any.whl.metadata (4.0 kB)
Collecting qtpy>=2.4.0 (from qtconsole->jupyter)
  Using cached QtPy-2.4.1-py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: six>=1.9.0 in /Users/surf/work/python/py312_env/lib/py
thon3.12/site-packages (from bleach!=5.0.0->nbconvert->jupyter) (1.16.0)
Collecting webencodings (from bleach!=5.0.0->nbconvert->jupyter)
  Using cached webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)
Requirement already satisfied: decorator in /Users/surf/work/python/py312_env/lib/pyt
hon3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (5.1.1)
Requirement already satisfied: jedi>=0.16 in /Users/surf/work/python/py312_env/lib/py
thon3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.19.1)
Requirement already satisfied: stack-data in /Users/surf/work/python/py312_env/lib/py
thon3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.6.3)
Requirement already satisfied: pexpect>4.3 in /Users/surf/work/python/py312_env/lib/p
ython3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (4.9.0)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/surf/work/python/py31
2_env/lib/python3.12/site-packages (from jupyter-client>=6.1.12->ipykernel->jupyter)
(2.9.0.post0)
Requirement already satisfied: platformdirs>=2.5 in /Users/surf/work/python/py312_env
/lib/python3.12/site-packages (from jupyter-core!=5.0.*,>=4.12->ipykernel->jupyter) (
4.2.1)
Requirement already satisfied: anyio>=3.1.0 in /Users/surf/work/python/py312_env/lib/
python3.12/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (4.3.0)
Collecting argon2-cffi>=21.1 (from jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached argon2_cffi-23.1.0-py3-none-any.whl.metadata (5.2 kB)
Collecting jupyter-events>=0.9.0 (from jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached jupyter_events-0.10.0-py3-none-any.whl.metadata (5.9 kB)
Collecting jupyter-server-terminals>=0.4.4 (from jupyter-server<3,>=2.4.0->notebook->
jupyter)
  Using cached jupyter_server_terminals-0.5.3-py3-none-any.whl.metadata (5.6 kB)
Collecting overrides>=5.0 (from jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)
Collecting prometheus-client>=0.9 (from jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached prometheus_client-0.20.0-py3-none-any.whl.metadata (1.8 kB)
Collecting send2trash>=1.8.2 (from jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached Send2Trash-1.8.3-py3-none-any.whl.metadata (4.0 kB)
Collecting terminado>=0.8.3 (from jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached terminado-0.18.1-py3-none-any.whl.metadata (5.8 kB)
Collecting websocket-client>=1.7 (from jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached websocket_client-1.8.0-py3-none-any.whl.metadata (8.0 kB)
Collecting async-lru>=1.0.0 (from jupyterlab<4.3,>=4.2.0->notebook->jupyter)
  Using cached async_lru-2.0.4-py3-none-any.whl.metadata (4.5 kB)
Requirement already satisfied: httpx>=0.25.0 in /Users/surf/work/python/py312_env/lib
/python3.12/site-packages (from jupyterlab<4.3,>=4.2.0->notebook->jupyter) (0.27.0)
Collecting jupyter-lsp>=2.0.0 (from jupyterlab<4.3,>=4.2.0->notebook->jupyter)
  Using cached jupyter_lsp-2.2.5-py3-none-any.whl.metadata (1.8 kB)
Collecting babel>=2.10 (from jupyterlab-server<3,>=2.27.1->notebook->jupyter)
  Using cached Babel-2.15.0-py3-none-any.whl.metadata (1.5 kB)
Collecting json5>=0.9.0 (from jupyterlab-server<3,>=2.27.1->notebook->jupyter)
  Using cached json5-0.9.25-py3-none-any.whl.metadata (30 kB)
Collecting jsonschema>=4.18.0 (from jupyterlab-server<3,>=2.27.1->notebook->jupyter)
  Using cached jsonschema-4.22.0-py3-none-any.whl.metadata (8.2 kB)
Requirement already satisfied: requests>=2.31 in /Users/surf/work/python/py312_env/li
b/python3.12/site-packages (from jupyterlab-server<3,>=2.27.1->notebook->jupyter) (2.
31.0)
Requirement already satisfied: fastjsonschema>=2.15 in /Users/surf/work/python/py312_
env/lib/python3.12/site-packages (from nbformat>=5.7->nbconvert->jupyter) (2.19.1)
Requirement already satisfied: wcwidth in /Users/surf/work/python/py312_env/lib/pytho
n3.12/site-packages (from prompt-toolkit>=3.0.30->jupyter-console->jupyter) (0.2.13)
Collecting soupsieve>1.2 (from beautifulsoup4->nbconvert->jupyter)
  Using cached soupsieve-2.5-py3-none-any.whl.metadata (4.7 kB)
Requirement already satisfied: idna>=2.8 in /Users/surf/work/python/py312_env/lib/pyt
hon3.12/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->notebook->jupyter
) (3.7)
Requirement already satisfied: sniffio>=1.1 in /Users/surf/work/python/py312_env/lib/
python3.12/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->notebook->jupy
ter) (1.3.1)
Collecting argon2-cffi-bindings (from argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->no
tebook->jupyter)
  Using cached argon2_cffi_bindings-21.2.0-cp38-abi3-macosx_10_9_universal2.whl.metad
ata (6.7 kB)
Requirement already satisfied: certifi in /Users/surf/work/python/py312_env/lib/pytho
n3.12/site-packages (from httpx>=0.25.0->jupyterlab<4.3,>=4.2.0->notebook->jupyter) (
2024.2.2)
Requirement already satisfied: httpcore==1.* in /Users/surf/work/python/py312_env/lib
/python3.12/site-packages (from httpx>=0.25.0->jupyterlab<4.3,>=4.2.0->notebook->jupy
ter) (1.0.5)
Requirement already satisfied: h11<0.15,>=0.13 in /Users/surf/work/python/py312_env/l
ib/python3.12/site-packages (from httpcore==1.*->httpx>=0.25.0->jupyterlab<4.3,>=4.2.
0->notebook->jupyter) (0.14.0)
Requirement already satisfied: parso<0.9.0,>=0.8.3 in /Users/surf/work/python/py312_e
nv/lib/python3.12/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel->jupyter
) (0.8.3)
Requirement already satisfied: attrs>=22.2.0 in /Users/surf/work/python/py312_env/lib
/python3.12/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->not
ebook->jupyter) (23.2.0)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.18.0->jupyterlab-
server<3,>=2.27.1->notebook->jupyter)
  Using cached jsonschema_specifications-2023.12.1-py3-none-any.whl.metadata (3.0 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1
->notebook->jupyter)
  Using cached referencing-0.35.1-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.7.1 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->not
ebook->jupyter)
  Using cached rpds_py-0.18.1-cp312-cp312-macosx_11_0_arm64.whl.metadata (4.1 kB)
Collecting python-json-logger>=2.0.4 (from jupyter-events>=0.9.0->jupyter-server<3,>=
2.4.0->notebook->jupyter)
  Using cached python_json_logger-2.0.7-py3-none-any.whl.metadata (6.5 kB)
Requirement already satisfied: pyyaml>=5.3 in /Users/surf/work/python/py312_env/lib/p
ython3.12/site-packages (from jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebo
ok->jupyter) (6.0.1)
Collecting rfc3339-validator (from jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->n
otebook->jupyter)
  Using cached rfc3339_validator-0.1.4-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting rfc3986-validator>=0.1.1 (from jupyter-events>=0.9.0->jupyter-server<3,>=2
.4.0->notebook->jupyter)
  Using cached rfc3986_validator-0.1.1-py2.py3-none-any.whl.metadata (1.7 kB)
Requirement already satisfied: ptyprocess>=0.5 in /Users/surf/work/python/py312_env/l
ib/python3.12/site-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel->jupyter) (
0.7.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/surf/work/python/py
312_env/lib/python3.12/site-packages (from requests>=2.31->jupyterlab-server<3,>=2.27
.1->notebook->jupyter) (3.3.2)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/surf/work/python/py312_en
v/lib/python3.12/site-packages (from requests>=2.31->jupyterlab-server<3,>=2.27.1->no
tebook->jupyter) (2.2.1)
Requirement already satisfied: executing>=1.2.0 in /Users/surf/work/python/py312_env/
lib/python3.12/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (
2.0.1)
Requirement already satisfied: asttokens>=2.1.0 in /Users/surf/work/python/py312_env/
lib/python3.12/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (
2.4.1)
Requirement already satisfied: pure-eval in /Users/surf/work/python/py312_env/lib/pyt
hon3.12/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (0.2.2)
Collecting fqdn (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.0->jupyt
er-server<3,>=2.4.0->notebook->jupyter)
  Using cached fqdn-1.5.1-py3-none-any.whl.metadata (1.4 kB)
Collecting isoduration (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.0
->jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached isoduration-20.11.0-py3-none-any.whl.metadata (5.7 kB)
Collecting jsonpointer>1.13 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=
0.9.0->jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached jsonpointer-2.4-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting uri-template (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.
0->jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached uri_template-1.3.0-py3-none-any.whl.metadata (8.8 kB)
Collecting webcolors>=1.11 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0
.9.0->jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached webcolors-1.13-py3-none-any.whl.metadata (2.6 kB)
Requirement already satisfied: cffi>=1.0.1 in /Users/surf/work/python/py312_env/lib/p
ython3.12/site-packages (from argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server
<3,>=2.4.0->notebook->jupyter) (1.16.0)
Requirement already satisfied: pycparser in /Users/surf/work/python/py312_env/lib/pyt
hon3.12/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi>=21.1->jup
yter-server<3,>=2.4.0->notebook->jupyter) (2.22)
Collecting arrow>=0.15.0 (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyte
r-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook->jupyter)
  Using cached arrow-1.3.0-py3-none-any.whl.metadata (7.5 kB)
Collecting types-python-dateutil>=2.8.10 (from arrow>=0.15.0->isoduration->jsonschema
[format-nongpl]>=4.18.0->jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook->j
upyter)
  Using cached types_python_dateutil-2.9.0.20240316-py3-none-any.whl.metadata (1.8 kB
)
Using cached jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Using cached ipykernel-6.29.4-py3-none-any.whl (117 kB)
Downloading ipywidgets-8.1.3-py3-none-any.whl (139 kB)
    139.4/139.4 kB 3.8 MB/s eta 0:00:00
Using cached jupyter_console-6.6.3-py3-none-any.whl (24 kB)
Using cached nbconvert-7.16.4-py3-none-any.whl (257 kB)
Using cached notebook-7.2.0-py3-none-any.whl (5.0 MB)
Using cached qtconsole-5.5.2-py3-none-any.whl (123 kB)
Using cached bleach-6.1.0-py3-none-any.whl (162 kB)
Using cached comm-0.2.2-py3-none-any.whl (7.2 kB)
Using cached debugpy-1.8.1-cp312-cp312-macosx_11_0_universal2.whl (1.4 MB)
Downloading jupyter_client-8.6.2-py3-none-any.whl (105 kB)
    105.9/105.9 kB 10.4 MB/s eta 0:00:00
Using cached jupyter_core-5.7.2-py3-none-any.whl (28 kB)
Downloading jupyter_server-2.14.1-py3-none-any.whl (383 kB)
    383.4/383.4 kB 17.6 MB/s eta 0:00:00
Downloading jupyterlab-4.2.1-py3-none-any.whl (11.6 MB)
    11.6/11.6 MB 34.2 MB/s eta 0:00:00
Downloading jupyterlab_server-2.27.2-py3-none-any.whl (59 kB)
    59.4/59.4 kB 5.0 MB/s eta 0:00:00
Downloading jupyterlab_widgets-3.0.11-py3-none-any.whl (214 kB)
    214.4/214.4 kB 17.6 MB/s eta 0:00:00
Using cached mistune-3.0.2-py3-none-any.whl (47 kB)
Using cached nbclient-0.10.0-py3-none-any.whl (25 kB)
Using cached nbformat-5.10.4-py3-none-any.whl (78 kB)
Using cached notebook_shim-0.2.4-py3-none-any.whl (13 kB)
Using cached pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)
Using cached pyzmq-26.0.3-cp312-cp312-macosx_10_15_universal2.whl (1.4 MB)
Using cached QtPy-2.4.1-py3-none-any.whl (93 kB)
Downloading widgetsnbextension-4.0.11-py3-none-any.whl (2.3 MB)
    2.3/2.3 MB 29.5 MB/s eta 0:00:00
Using cached appnope-0.1.4-py2.py3-none-any.whl (4.3 kB)
Using cached beautifulsoup4-4.12.3-py3-none-any.whl (147 kB)
Using cached defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Using cached jupyterlab_pygments-0.3.0-py3-none-any.whl (15 kB)
Using cached nest_asyncio-1.6.0-py3-none-any.whl (5.2 kB)
Using cached psutil-5.9.8-cp38-abi3-macosx_11_0_arm64.whl (249 kB)
Using cached tinycss2-1.3.0-py3-none-any.whl (22 kB)
Using cached argon2_cffi-23.1.0-py3-none-any.whl (15 kB)
Using cached async_lru-2.0.4-py3-none-any.whl (6.1 kB)
Using cached Babel-2.15.0-py3-none-any.whl (9.6 MB)
Using cached json5-0.9.25-py3-none-any.whl (30 kB)
Using cached jsonschema-4.22.0-py3-none-any.whl (88 kB)
Using cached jupyter_events-0.10.0-py3-none-any.whl (18 kB)
Using cached jupyter_lsp-2.2.5-py3-none-any.whl (69 kB)
Using cached jupyter_server_terminals-0.5.3-py3-none-any.whl (13 kB)
Using cached overrides-7.7.0-py3-none-any.whl (17 kB)
Using cached prometheus_client-0.20.0-py3-none-any.whl (54 kB)
Using cached Send2Trash-1.8.3-py3-none-any.whl (18 kB)
Using cached soupsieve-2.5-py3-none-any.whl (36 kB)
Using cached terminado-0.18.1-py3-none-any.whl (14 kB)
Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Using cached websocket_client-1.8.0-py3-none-any.whl (58 kB)
Using cached jsonschema_specifications-2023.12.1-py3-none-any.whl (18 kB)
Using cached python_json_logger-2.0.7-py3-none-any.whl (8.1 kB)
Using cached referencing-0.35.1-py3-none-any.whl (26 kB)
Using cached rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)
Using cached rpds_py-0.18.1-cp312-cp312-macosx_11_0_arm64.whl (323 kB)
Using cached argon2_cffi_bindings-21.2.0-cp38-abi3-macosx_10_9_universal2.whl (53 kB)
Using cached rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)
Using cached jsonpointer-2.4-py2.py3-none-any.whl (7.8 kB)
Using cached webcolors-1.13-py3-none-any.whl (14 kB)
Using cached fqdn-1.5.1-py3-none-any.whl (9.1 kB)
Using cached isoduration-20.11.0-py3-none-any.whl (11 kB)
Using cached uri_template-1.3.0-py3-none-any.whl (11 kB)
Using cached arrow-1.3.0-py3-none-any.whl (66 kB)
Using cached types_python_dateutil-2.9.0.20240316-py3-none-any.whl (9.7 kB)
Installing collected packages: webencodings, widgetsnbextension, websocket-client, we
bcolors, uri-template, types-python-dateutil, tinycss2, terminado, soupsieve, send2tr
ash, rpds-py, rfc3986-validator, rfc3339-validator, qtpy, pyzmq, python-json-logger,
psutil, prometheus-client, pandocfilters, overrides, nest-asyncio, mistune, jupyterla
b-widgets, jupyterlab-pygments, jupyter-core, jsonpointer, json5, fqdn, defusedxml, d
ebugpy, comm, bleach, babel, async-lru, appnope, referencing, jupyter-server-terminal
s, jupyter-client, beautifulsoup4, arrow, argon2-cffi-bindings, jsonschema-specificat
ions, isoduration, argon2-cffi, jsonschema, ipywidgets, ipykernel, qtconsole, nbforma
t, jupyter-console, nbclient, jupyter-events, nbconvert, jupyter-server, notebook-shi
m, jupyterlab-server, jupyter-lsp, jupyterlab, notebook, jupyter
Successfully installed appnope-0.1.4 argon2-cffi-23.1.0 argon2-cffi-bindings-21.2.0 a
rrow-1.3.0 async-lru-2.0.4 babel-2.15.0 beautifulsoup4-4.12.3 bleach-6.1.0 comm-0.2.2
 debugpy-1.8.1 defusedxml-0.7.1 fqdn-1.5.1 ipykernel-6.29.4 ipywidgets-8.1.3 isodurat
ion-20.11.0 json5-0.9.25 jsonpointer-2.4 jsonschema-4.22.0 jsonschema-specifications-
2023.12.1 jupyter-1.0.0 jupyter-client-8.6.2 jupyter-console-6.6.3 jupyter-core-5.7.2
 jupyter-events-0.10.0 jupyter-lsp-2.2.5 jupyter-server-2.14.1 jupyter-server-termina
ls-0.5.3 jupyterlab-4.2.1 jupyterlab-pygments-0.3.0 jupyterlab-server-2.27.2 jupyterl
ab-widgets-3.0.11 mistune-3.0.2 nbclient-0.10.0 nbconvert-7.16.4 nbformat-5.10.4 nest
-asyncio-1.6.0 notebook-7.2.0 notebook-shim-0.2.4 overrides-7.7.0 pandocfilters-1.5.1
 prometheus-client-0.20.0 psutil-5.9.8 python-json-logger-2.0.7 pyzmq-26.0.3 qtconsol
e-5.5.2 qtpy-2.4.1 referencing-0.35.1 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1
 rpds-py-0.18.1 send2trash-1.8.3 soupsieve-2.5 terminado-0.18.1 tinycss2-1.3.0 types-
python-dateutil-2.9.0.20240316 uri-template-1.3.0 webcolors-1.13 webencodings-0.5.1 w
ebsocket-client-1.8.0 widgetsnbextension-4.0.11
(py312_env) Monte-Aire:day01 (main) surf$ jupyter notebook --no-browser
[I 2024-06-03 17:18:20.565 ServerApp] jupyter_lsp | extension was successfully linked
.
[I 2024-06-03 17:18:20.566 ServerApp] jupyter_server_terminals | extension was succes
sfully linked.
[I 2024-06-03 17:18:20.568 ServerApp] jupyterlab | extension was successfully linked.
[I 2024-06-03 17:18:20.570 ServerApp] notebook | extension was successfully linked.
[I 2024-06-03 17:18:21.100 ServerApp] notebook_shim | extension was successfully link
ed.
[I 2024-06-03 17:18:21.136 ServerApp] notebook_shim | extension was successfully load
ed.
[I 2024-06-03 17:18:21.138 ServerApp] jupyter_lsp | extension was successfully loaded
.
[I 2024-06-03 17:18:21.139 ServerApp] jupyter_server_terminals | extension was succes
sfully loaded.
[I 2024-06-03 17:18:21.140 LabApp] JupyterLab extension loaded from /Users/surf/work/
python/py312_env/lib/python3.12/site-packages/jupyterlab
[I 2024-06-03 17:18:21.140 LabApp] JupyterLab application directory is /Users/surf/wo
rk/python/py312_env/share/jupyter/lab
[I 2024-06-03 17:18:21.141 LabApp] Extension Manager is 'pypi'.
[I 2024-06-03 17:18:21.162 ServerApp] jupyterlab | extension was successfully loaded.
[I 2024-06-03 17:18:21.163 ServerApp] notebook | extension was successfully loaded.
[I 2024-06-03 17:18:21.164 ServerApp] Serving notebooks from local directory: /Users/
surf/work/github/priv/Advanced_Python_Jun2k24/day01
[I 2024-06-03 17:18:21.164 ServerApp] Jupyter Server 2.14.1 is running at:
[I 2024-06-03 17:18:21.164 ServerApp] http://localhost:8888/tree?token=5e0bebd49d476d
f0ae346f3e2e4873812b74f7c9fee33e78
[I 2024-06-03 17:18:21.164 ServerApp]     http://127.0.0.1:8888/tree?token=5e0bebd49d
476df0ae346f3e2e4873812b74f7c9fee33e78
[I 2024-06-03 17:18:21.164 ServerApp] Use Control-C to stop this server and shut down
 all kernels (twice to skip confirmation).
[C 2024-06-03 17:18:21.166 ServerApp]

    To access the server, open this file in a browser:
        file:///Users/surf/Library/Jupyter/runtime/jpserver-21053-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/tree?token=5e0bebd49d476df0ae346f3e2e4873812b74f7c9fee3
3e78
        http://127.0.0.1:8888/tree?token=5e0bebd49d476df0ae346f3e2e4873812b74f7c9fee3
3e78
77f22
[I 2024-06-03 17:20:32.906 ServerApp] Connecting to kernel 98d8ed85-e575-49dd-89fe-73
6a57e77f22.
[I 2024-06-03 17:20:32.917 ServerApp] Starting buffering for 98d8ed85-e575-49dd-89fe-
736a57e77f22:a29e0a78-8e69-45d0-92b9-2883bead755c
[I 2024-06-03 17:22:20.398 ServerApp] Saving file at /Numpy_Intro.ipynb
[I 2024-06-03 18:13:53.684 ServerApp] Saving file at /Numpy_Intro.ipynb
^C
(py312_env) Monte-Aire:day01 (main) surf$ 



# Copyright 2024 Sarfraaz Ahmed. All rights reserved.
