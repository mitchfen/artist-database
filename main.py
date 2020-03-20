import os
import sys
import sqlite3
from sqlite3 import Error
from tabulate import tabulate

# Add a new tuple to the table
def addEntry():

    artist = input("Artist: ")
    date = input("Date: ")
    venue = input("Venue: ")

    sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "

    conn.execute(sql)
    conn.commit()

# Connect to the SQL Shows.db file and create the only table
def connectToDatabase():

    try :
        conn = sqlite3.connect('Shows.db')
    except Error as e:
        print(e)

    conn.execute('''CREATE TABLE IF NOT EXISTS showTable(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Artist  CHAR(30),
    Date CHAR(30),
    Venue CHAR(30));''')
    return conn

# Main program loop, where user input is accepted
def mainLoop():

    keepGoing = True
    while(keepGoing):

        print("1) Print the table")
        print("2) Add a new entry")
        print("3) Remove an entry")
        print("4) Edit an entry")
        print("5) Exit")

        i = int(input("Command: "))
        if i == 1:  printTable()
        elif i == 2: addEntry()
        elif i == 3: removeEntry()
        elif i == 4: editEntry()
        elif i == 5: keepGoing = False

# Print the table using tabulate
def printTable():
        cur.execute("SELECT * FROM showTable")
        entries = cur.fetchall()
        print(tabulate(entries))

# TODO
def removeEntry():
   return 

# TODO
def editEntry():
    return

entries = []
conn = connectToDatabase()
cur = conn.cursor()
mainLoop() #Executes until user enters 3, then close connection and exit
os.system("cp Shows.db backup.db") #copy the database just in case
conn.close()