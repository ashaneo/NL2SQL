import sqlite3
from datetime import datetime

class NL2SQLDatabase:
    def __init__(self, db_path):  # Initialize the database connection and create the table if it does not exist.
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self): #Create the nl2sql_history table if it does not EXist
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS nl2sql_history (
                id INTEGER PRIMARY KEY,
                natural_language_question TEXT NOT NULL,
                generated_query TEXT NOT NULL,
                time_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def add_record(self, question, query): #Add a record to the nl2sql_history table.
        self.cursor.execute('''
            INSERT INTO nl2sql_history (natural_language_question, generated_query)
            VALUES (?, ?)
        ''', (question, query))
        self.conn.commit()
        print("Record added successfully")
    
    def fetch_all(self): #Fetch all records from the nl2sql_history table.
        self.cursor.execute('SELECT * FROM nl2sql_history')
        return self.cursor.fetchall()
    
    def __del__(self): #Close the database connection when the object is deleted.
        self.conn.close()

if __name__ == '__main__': #This is just for TEsting
    db = NL2SQLDatabase('LocalDB/history.db')
    # db.add_record("What is the total revenue for 2020?", "SELECT SUM(revenue) FROM sales WHERE year = 2020")
    print(db.fetch_all())
