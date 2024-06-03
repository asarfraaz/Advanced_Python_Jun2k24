'''
    Find the total cost of inventory
'''
import csv
import sys

def inventory_cost(filename):
    total_cost = 0.0

    with open(filename) as FH:
        data = csv.reader(FH)
        # Skip the header line
        headers = next(data)

        # Starts iterating from second line onwards
        for row in data:
            try:
                quant = int(row[1])
                price = float(row[2])
            except ValueError as e:
                print("Bad row", row)
                continue

            total_cost += quant * price

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/inventory.csv'

cost = inventory_cost(filename)
print("Total cost:", cost)
