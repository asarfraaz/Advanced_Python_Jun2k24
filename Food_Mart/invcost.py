'''
    Find the total cost of inventory
'''
import csv

def inventory_cost(filename):
    total_cost = 0.0

    with open(filename) as FH:
        data = csv.reader(FH)
        # Skip the header line
        headers = next(data)

        # Starts iterating from second line onwards
        for row in data:
            quant = int(row[1])
            price = float(row[2])
            total_cost += quant * price

    return total_cost


cost = inventory_cost('Data/inventory.csv')
print("Total cost:", cost)
