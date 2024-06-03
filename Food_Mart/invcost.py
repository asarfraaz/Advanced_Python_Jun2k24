'''
    Find the total cost of inventory
'''

# Initialise total = 0
total_cost = 0.0

# Open the file
with open("Data/inventory.csv") as FH:
    # Iterate through the lines
    first_line = True
    for line in FH:
        if first_line:
            first_line = False
            continue
        # Extract from each line, quant and price
        parts = line.split(',')
        quant = int(parts[1])
        price = float(parts[2])
        # Add quant * price to total
        total_cost += quant * price

# Print the total
print("Total cost:", total_cost)
