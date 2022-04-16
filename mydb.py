import sqlite3
class Database:
    #1. Properties
    con = ''
    cur = ''
    
    
    #2. Constructor
    def __init__(self,dbname):
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()
        pass
    
    
    #3. Method
    def insert(self):
        self.cur.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')

        # Insert a row of data
        self.cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        self.con.commit()
        self.con.close()
    
    
    #4 Nested Class
    
# lets create the class object

dbo = Database('my.db');

dbo.insert()