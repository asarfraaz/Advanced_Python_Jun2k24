'''
    Report any gains/losses in inventory
'''
import csv

def read_inventory(filename: str) -> list[dict[str, str|int|float]]:
    inv = list()
    with open(filename) as FH:
        data = csv.reader(FH)
        headers = next(data)

        for row in data:
            info = {
                    'name' : row[0],
                    'quant': int(row[1]),
                    'price': float(row[2]),
                   }
            inv.append(info)

    return inv

def read_prices(filename:str) -> dict[str, float]:
    prices = dict()
    with open(filename) as FH:
        data = csv.reader(FH)
        for row in data:
            try:
                prices[ row[0] ] = float(row[1])
            except IndexError as e:
                continue

    return prices

# Main starts from here
inventory = read_inventory('Data/inventory.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for pr in inventory:
    total_cost += pr['quant'] * pr['price']

latest_cost = 0.0
for pr in inventory:
    latest_cost += pr['quant'] * prices[ pr['name'] ]

gain_or_loss = latest_cost - total_cost
print("Total Gain/Loss:", gain_or_loss)
