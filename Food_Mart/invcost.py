'''
    Find the total cost of inventory
'''
import csv
import sys
from report import read_inventory

# Annotations
def inventory_cost(filename:str) -> float:
    total_cost = 0.0
    inv = read_inventory(filename)
    for pr in inv:
        total_cost += pr.cost()

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/inventory.csv'

cost = inventory_cost(filename)
print("Total cost:", cost)
