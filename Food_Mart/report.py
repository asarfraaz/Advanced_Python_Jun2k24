'''
    Report any gains/losses in inventory
'''
import csv

def read_inventory(filename: str) -> list[tuple[str, int, float]]:
    inv = list()
    with open(filename) as FH:
        data = csv.reader(FH)
        headers = next(data)

        for row in data:
            name  = row[0]
            quant = int(row[1]) 
            price = float(row[2])
            info = (name, quant, price)
            inv.append(info)

    return inv
