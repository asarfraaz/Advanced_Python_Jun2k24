'''
    Find the total cost of inventory
'''
import csv
import sys

# Annotations
def inventory_cost(filename:str) -> float:
    total_cost = 0.0

    with open(filename) as FH:
        data = csv.reader(FH)
        # Skip the header line
        headers = next(data)

        # Starts iterating from second line onwards
        for rowno, row in enumerate(data, start=1):
            record = dict(zip(headers, row))
            try:
                quant = int(record['quant'])
                price = float(record['price'])
            except ValueError as e:
                print("Row", rowno, ": Couldn't convert:", row)
                continue

            total_cost += quant * price

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/inventory.csv'

cost = inventory_cost(filename)
print("Total cost:", cost)
