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
