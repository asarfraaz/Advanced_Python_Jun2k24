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
            record = dict(zip(headers, row))
            info = {
                    'name' : record['name'],
                    'quant': int(record['quant']),
                    'price': float(record['price']),
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

def print_report(report):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    print("%10s %10s %10s %10s" % headers)

    dashes = tuple(['-' * 10] * 4)
    print("%10s %10s %10s %10s" % dashes)

    for row in report:
        print("%10s %10d %10.2f %10.2f" % row)

def inventory_report(inventory_filename, prices_filename):
    inventory = read_inventory(inventory_filename)
    prices = read_prices(prices_filename)
    report = make_report(inventory, prices)
    print_report(report)

# Main starts from here
