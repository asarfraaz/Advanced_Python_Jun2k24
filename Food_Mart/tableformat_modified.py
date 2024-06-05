'''
    Classes to help format report table
'''

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

