import re
from collections import MutableSequence

class DataSet(list):
    
    def __init__(self, data=None):
        super(DataSet, self).__init__()

        self._connection = None
        self._query      = None
        self._rows       = []
        self._isvalidate = False
        self._rownum     = 0
        self._count      = 0
        
    
    def parse(self, query):
        #Build sql
        found = re.compile("(@@[aA-zZ]*)").findall(query)
        if found:
            for token in found:
                name = token[2:]
                value = globals().get(name)
                if not value:
                    raise Exception('Unknown param: %s' %token)
                query = query.replace(token, str(value))

        #Build value
        found = re.compile("(@[aA-zZ]*)").findall(query)
        if found:
            for token in found:
                name = token[1:]
                value = globals().get(name)
                if not value:
                    raise Exception('Unknown param: %s' %token)
                if isinstance(value, str):
                    value = "'%s'" %value
                query = query.replace(token, str(value))
        return query


    def refresh(self):
        if not self._isvalidate:
            query = self.parse(self._query)
            self._connection.execute(query)
            self._rows = self._connection.fetch_all(fetch_dict = True)
            self._count = len(self._rows)
            self._isvalidate = True


    def invalidate(self):
        self._isvalidate = False
    
        
    @property
    def rows(self):
        self.refresh()
        return self._rows
        

    @property
    def query(self):
        return self._query


    @query.setter
    def query(self, value):
        # Remove ';' from sql
        value = value[:-1]
        self._query = value
        
        
    @property
    def connection(self):
        return self._connection
        
        
    @connection.setter
    def connection(self, value):
        self._connection = value
        
        
    def insert(self, pos, val):
        self._rows.insert(pos, val)
        
        
    def append(self, val):
        self._rows.append(val)
        
        
    def __str__(self):
        return self.__repr__()
    
    
    def __repr__(self):
        return """<DataSet %s>""" % self._rows
    
        
    def __iter__(self):
        self._rownum = 0
        self.refresh()
        return self


    def __next__(self):
        if self._rownum > self._count - 1:
            raise StopIteration
        else:
            self._rownum += 1
            return self._rows[self._rownum - 1]
        
        
    def __len__(self):
        self.refresh()
        return self._count


    def __getitem__(self, sliced):
        self.refresh()
        return self._rows[sliced]
    
    
    def __delitem__(self, pos):
        del self._rows[pos]


    def __setitem__(self, pos, val):
        self._rows[pos] = val
        return self._rows[pos]




        