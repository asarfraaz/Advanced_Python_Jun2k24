'''
    Classes to help format report table
'''

def create_formatter(fmt):
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CsvTableFormatter()
    else:
        raise RuntimeError(f'Unknown format: {fmt}')

class TableFormatter:
    '''
        Interface for depicting a table
    '''
    def headings(self, headers):
        '''
            Emit table headings
        '''
        raise NotImplementedError

    def row(self, rowdata):
        '''
            Emit a single row of table data
        '''
        raise NotImplementedError


class TextTableFormatter(TableFormatter):        
    ''' 
        Emit a table in plain-text format
    '''
    def headings(self, headers):
        ''' 
            Emit heading with a dashed line
        '''
        for hdr in headers:
            print(f'{hdr:>10s}', end=' ') 
        else:
            print()

        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        '''
            Emit a single row for plain-text format
        '''
        for field in rowdata:
            print(f'{field:>10s}', end=' ')
        else:
            print()

class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
