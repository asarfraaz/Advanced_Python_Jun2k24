'''
    Report any gains/losses in inventory
'''
import csv
from fileparse import parse_csv
from product import Product

def read_inventory(filename: str) -> list[dict[str, str|int|float]]:
    with open(filename) as FH:
        invdicts = parse_csv(FH,
                        select=['name', 'quant', 'price'],
                        types=[str, int, float]
                       )
        inv = [ Product(pr['name'], pr['quant'], pr['price'])
                for pr in invdicts
              ]
    return inv

def read_prices(filename:str) -> dict[str, float]:
    with open(filename) as FH:
        list_prices = parse_csv(FH, types=[str, float], has_headers=False)
        prices = dict(list_prices)
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


def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} invfile pricefile')

    invfile = args[1]
    pricefile = args[2]
    inventory_report(invfile, pricefile)


# Main starts from here
if __name__ == "__main__":
    import sys
    main(sys.argv)
