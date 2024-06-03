'''
    Find the total cost of inventory
'''
import csv

total_cost = 0.0

with open("Data/inventory.csv") as FH:
    data = csv.reader(FH)
    # Skip the header line
    headers = next(data)

    # Starts iterating from second line onwards
    for row in data:
        quant = int(row[1])
        price = float(row[2])
        total_cost += quant * price

print("Total cost:", total_cost)
