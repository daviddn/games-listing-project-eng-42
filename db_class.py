import pyodbc
import requests

# Define a class to access db

class Connectdb():
    # have the characteristics to access the db
    def __init__(self, server = 'localhost, 1433', database = 'SpartaGames', username = 'SA', password = 'Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_db.cursor()

    # Define methods
    def filter_query(self, query):
        return self.cursor.execute(query)