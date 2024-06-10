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

>>>
>>> # GYAN SESSION
>>> fruit = "Apples"
>>> cost = 250
>>> price = cost / 12
>>> print("The price of 1 apple is", price)
The price of 1 apple is 20.833333333333332
>>> print("The price of 1 apple is {}".format(price))
The price of 1 apple is 20.833333333333332
>>> fruit = "apples"
>>> print("The price of 1 {} is {}".format(fruit, price))
The price of 1 apples is 20.833333333333332
>>> print("The price of 1 {0} is {1}".format(fruit, price))
The price of 1 apples is 20.833333333333332
>>> print("The price of 1 {1} is {0}".format(fruit, price))
The price of 1 20.833333333333332 is apples
>>> print("The price of 1 {x} is {y}".format(x=fruit, y=price))
The price of 1 apples is 20.833333333333332
>>> print("The price of 1 {fruit} is {price}".format(fruit=fruit, price=price))
The price of 1 apples is 20.833333333333332
>>> # Python 3.6+
>>> print(f"The price of 1 {fruit} is {price}")
The price of 1 apples is 20.833333333333332
>>>
>>>
>>> fruit
'apples'
>>> print(f"The price of 1 {fruit} is {price}")
The price of 1 apples is 20.833333333333332
>>> fruit[:-1]
'apple'
>>> print(f"The price of 1 {fruit[:-1]} is {price}")
The price of 1 apple is 20.833333333333332
>>> print(f"The price of 1 {fruit[:-1]} is {price:.2f}")
The price of 1 apple is 20.83
>>> print(f"The price of 1 {fruit[:-1]:10} is {price:5.2f}")
The price of 1 apple      is 20.83
>>> print(f"The price of 1 {fruit[:-1]:>10} is {price:5.2f}")
The price of 1      apple is 20.83
>>> fruit
'apples'
>>> fav_fruit = f"Simla {fruit}"
>>> fav_fruit
'Simla apples'
>>> fav_fruit = f"Simla {fruit.title()}"
>>> fav_fruit
'Simla Apples'
>>>
>>>
>>> filename = "story.txt"
>>> folder = "/home/tim/Downloads"
>>>
>>> path = folder + "/" + filename
>>> path
'/home/tim/Downloads/story.txt'
>>>
>>> path = f"{folder}/{filename}"
>>> path
'/home/tim/Downloads/story.txt'
>>> quit()
Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
Row 4: Couldn't convert: ['MINT', '', '51.23']
Row 7: Couldn't convert: ['PASTE', '', '70.44']
Total cost: 27381.15
Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
Row rowno = 4: Couldn't convert: ['MINT', '', '51.23']
Row rowno = 7: Couldn't convert: ['PASTE', '', '70.44']
Total cost: 27381.15
Monte-Aire:Food_Mart (main) surf$ python invcost.py Data/missing.csv
Row rowno=4: Couldn't convert: ['MINT', '', '51.23']
Row rowno=7: Couldn't convert: ['PASTE', '', '70.44']
Total cost: 27381.15
Monte-Aire:Food_Mart (main) surf$

# Copyright 2024 Sarfraaz Ahmed. All rights reserved.
