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

def make_report(inventory:list[dict[str, str|int|float]],
                prices: dict[str, float]
               ) -> list[tuple[str, int, float, float]]:
    report = list()
    for pr in inventory:
        name   = pr['name']
        quant  = pr['quant']
        latest = prices[name]
        change = latest - pr['price']
        one_row = (name, quant, latest, change)
        report.append(one_row)

    return report

