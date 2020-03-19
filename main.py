import os
import sys
import sqlite3

# Add a new tuple to the table
def addEntry(conn):
    artist = input("Artist: ")
    date = input("Date: ")
    venue = input("Venue: ")

    sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "

    conn.execute(sql)
    conn.commit()

# Connect to the SQL Shows.db file
def connectToDatabase():
    conn = sqlite3.connect('Shows.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS showTable(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Artist  CHAR(30),
    Date CHAR(30),
    Venue CHAR(30));''')
    return conn

# I miss switch loops
def mainLoop():
    keepGoing = True
    while(keepGoing):
        print("_____________________")
        print("1) Print the table")
        print("2) Add a new entry")
        print("3) Exit")
        i = int(input("Command: "))
        if i == 1: printTable()
        elif i == 2:addEntry(conn)
        elif i == 3:keepGoing = False

def printTable():
    print("table goes here")

    i = input

conn = connectToDatabase()
mainLoop() #Executes until user enters 3, then close connection and exit
conn.close()