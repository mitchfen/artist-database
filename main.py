import os
import sqlite3
from addEntry import addEntry

def addEntry(conn):
    artist = input("Artist: ")
    date = input("Date: ")
    venue = input("Venue: ")

    sql = "INSERT INTO showTABLE (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "

    conn.execute(sql)
    conn.commit()

def connectToDatabase():
    conn = sqlite3.connect('Shows.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS showTable(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Artist  CHAR(30),
    Date CHAR(30),
    Venue CHAR(30));''')
    return conn

conn = connectToDatabase()
addEntry(conn)
conn.close()