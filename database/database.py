# from psycopg import connect
from dotenv import load_dotenv
import os
import importlib
from pathlib import Path
import requests

#Load environment file
load_dotenv(str(Path().cwd().parent.joinpath("environment", '.env')))

class Database:
    connection = None
    cursor = None
    db_module = "psycopg"
    db_helper_module = "postgres"
    def __init__(self,db_env_var, db_module):
        #Depending on the module passed, can use different db helper packages for different databases, abstracting implementation details from main
        #database class
        self.db_module = importlib.import_module(db_module)
        self.db_helper_module = importlib.import_module(f'{self.}')
        self.connection = self.db_module.connect(os.getenv(db_env_var))
        if(self.cursor == None):
            self.cursor = self.connection.cursor()


    def insert_stock(self,**kwargs):
        self.db_module.insert_stock(self.cursor,kwargs)  

    def insert_historical_stock_price(self, **kwargs):
        self.db_module.insert_historical_stock_price(self.cursor, kwargs)
    
    
    # def test(self):
    #     self.cursor.execute("select * from testtable")
    #     print(self.cursor.fetchall())
    def insert_multiple_stocks(self):
        res = requests.get("https://datahub.io/core/s-and-p-500-companies/r/0.csv")
        val = res.json()
        insert
a = Database(db_env_var="DB_URL", db_module="psycopg")
a.test()
