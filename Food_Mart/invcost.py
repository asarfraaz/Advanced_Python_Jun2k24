'''
    Find the total cost of inventory
'''

total_cost = 0.0

with open("Data/inventory.csv") as FH:
    # Skip the header line
    headers = next(FH)

    # Starts iterating from second line onwards
    for line in FH:
        parts = line.split(',')
        quant = int(parts[1])
        price = float(parts[2])
        total_cost += quant * price

print("Total cost:", total_cost)
