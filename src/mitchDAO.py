import sqlite3
from sqlite3 import Error


class DAO:

    connector = None
    cursor = None
    entries = []
    databaseName = None
    tableName = "showTable"
    createTableString = '''CREATE TABLE IF NOT EXISTS showTable(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Artist  CHAR(30),
        Date CHAR(30),
        Venue CHAR(30));'''


    # Parameterized constructor
    def __init__(self, databaseName):
        
        # Connect to the SQL Shows.db file and create the only table
        try :
            self.connector = sqlite3.connect(databaseName)
        except Error as e:
            print(e)

        self.connector.execute(self.createTableString)
        self.connector.commit()
        self.cursor = self.connector.cursor()
        self.databaseName = databaseName

    # Method to close SQLite connection
    def close(self):

        self.connector.close()

    # Method to add a a table entry
    def addEntry(self, artist, date, venue):
        
        sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "
        self.connector.execute(sql)
        self.connector.commit()
    
    # Method to clear table by dropping then recreating it
    def clearTable(self):
        sql = "DROP TABLE " + self.tableName + ";"
        self.connector.execute(sql)
        self.connector.commit()
        self.connector.execute(self.createTableString)
        self.connector.commit()

    # Grab the information from Sqlite, store in a list, return that list
    def collectAllEntries(self):
                
        self.cursor.execute("SELECT * FROM showTable")
        self.entries =self.cursor.fetchall()
        return self.entries