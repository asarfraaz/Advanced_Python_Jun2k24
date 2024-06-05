'''
    Parse a csv file into a list of entries
'''

import csv

def parse_csv(filename:str, 
              select:list[str]=None, 
              types=None,
              has_headers:bool=True,
              delimiter:str=',',
              silence_errors:bool=False
              ) -> list[dict[str, str|int|float]] | list[tuple[str, int, float]]:
    '''
        Parse a CSV file into a list of records
        based on a given select list of columns
        and convert them to the given datatypes
        Also supports reading CSV files without headers
        Supports supressing of errors messages
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as FH:
        data = csv.reader(FH, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(data)
        
        if select:
            indices = [ headers.index(col) for col in select ]
            headers = select
        else:
            indices = []

        records = list()
        for rowno, row in enumerate(data, start=1):
            if not row:     # Skip rows with no data
                continue

            if indices:
                row = [ row[idx] for idx in indices ]

            if types:
                try:
                    row = [ func(val) for func, val in zip(types, row) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records
