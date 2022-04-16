import sqlite3


class Database:
    con = cur = ''
    def __init__(self,dbname):
        print('Hello from constructor'+dbname);
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()
        self.insertSomeOption();
    
    def insertSomeOption(self):
        print('Hello from insertSomeOption');
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS option_tbl (option_name text) ''') 
        pass
    
    def insert(self,lists):
        for list in lists:
            self.cur.execute(f"INSERT INTO option_tbl VALUES ('{list}')") 
            # Save (commit) the changes
            self.con.commit()
        pass
    
    def select(self,table_name):
        lists = []
        rows = self.cur.execute(f"SELECT * FROM {table_name}")
        i = 0
        for row in rows:
            #print(type(row))
            lists.insert(i,row[0])
            pass
        #print(lists)
        
        return lists
        
