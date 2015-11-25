import cx_Oracle, logging


def fetchdict(cursor):
    if cursor.description is None: return None
    desc = [d[0] for d in cursor.description]
    row = [dict(zip(desc,line)) for line in cursor]
    return row


class DBConnection:
    '''
    Abstract class for connect to PostgreSQL or Oracle.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.connection = None
        self.cursor = None
        self.bulk_size = 1000
       

    def connect(self):
        raise 'Not implemented connect()!' 
    
    
    def execute(self, sSQL):
        logging.debug("SQL: %s" %sSQL)
        if self.connection is None:
            self.connect()
           
        self.cursor = self.get_cursor()
        self.cursor.execute(sSQL)
        
        return self.cursor
    
    
    def commit(self):
        self.connection.commit() 
    
    
    def rollback(self):
        self.connection.rollback()
    
    
    def fetch_all(self, fetch_dict = False):
        if fetch_dict:
            rows = fetchdict(self.cursor) 
        else:
            rows = self.cursor.fetchall()
                       
        return rows
    
    def fetch_first(self, fetch_dict = False):
        if fetch_dict:
            rows = fetchdict(self.cursor)
        else:
            rows = [self.cursor.fetchone()]
               
        if len(rows) > 0:
            return rows[0]        
        return []
    
    
    def fetch_many(self):
        return self.cursor.fetchmany()        
    
    
    def get_cursor(self):
        if self.connection == None:
            self.connect()
        if self.cursor == None:
            self.cursor = self.connection.cursor()  
        self.cursor.arraysize = self.bulk_size 
        return self.cursor 
    
    
    def close(self):
        if not self.connection is None:
            self.connection.close()
            self.connection = None




class OracleConnection(DBConnection):
        
    def __init__(self):
        DBConnection.__init__(self)

        
    def connect(self, uri):       
        logging.debug("Connect to oracle...")
        
        dsn_tns = cx_Oracle.makedsn(host, port, database)
        
        logging.debug('Oracle DSN: %s  user=%s' %(dsn_tns, user_name))
        
        self.connection = cx_Oracle.connect(user     = user_name, 
                                            password = user_password, 
                                            dsn      = dsn_tns)

        logging.debug("Connect to oracle [DONE]")
        
        return self.connection
