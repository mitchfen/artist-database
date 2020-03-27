import os
import sys
import sqlite3
import tkinter as tk
from tkinter import *
from sqlite3 import Error
from tabulate import tabulate

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

###################################################
#   GUI Code
###################################################

# Add a new tuple to the table
def addEntryFromGUI():
    # Casting to string may not be needed here but I'm used to Java/C++, leave it for now
    print(artistEntry.get())
    artist = artistEntry.get()
    date = str(dateEntry.get())
    venue = str(venueEntry.get())

    sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "
    conn.execute(sql)
    conn.commit()

def gridAllTheThings():
    artistLabel.grid(sticky= W, row=0, column=0)
    artistEntry.grid(row=1, column=0)
    dateLabel.grid(sticky= W, row=2, column=0)
    dateEntry.grid(row=3, column=0)
    venueLabel.grid(sticky= W, row=4, column=0)
    venueEntry.grid(row=5, column=0)
    addArtistButton.grid(sticky= W, row=6, column=0)

###################################################
#   End of GUI code
###################################################


###################################################
#   Command line code
#   This code was written for the command line functionality.
#   No longer needed now that the GUI is functional
###################################################

# Main program loop, where user input is accepted
def cmdPromptLoop():

    keepGoing = True
    while(keepGoing):

        print("1) Print the table")
        print("2) Add a new entry")
        print("3) Remove an entry")
        print("4) Edit an entry")
        print("5) Exit")

        i = int(input("Command: "))
        if i == 1:  printTableToCMD()
        elif i == 2: addEntryFromCMD()
        elif i == 3: removeEntryFromCMD()
        elif i == 4: editEntryFromCMD()
        elif i == 5: keepGoing = False

# Print the table using tabulate
def printTableToCMD():
        cur.execute("SELECT * FROM showTable")
        entries = cur.fetchall()
        print(tabulate(entries))

def addEntryFromCMD(x):
    print(x)
    artist = input("Artist: ")
    date = input("Date: ")
    venue = input("Venue: ")

    sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "

    conn.execute(sql)
    conn.commit()


# TODO
def removeEntryFromCMD():
   return 

# TODO
def editEntryFromCMD():
    return

###################################################
#   End of command line code
###################################################

# MAIN PROGRAM
entries = []
conn = connectToDatabase()
cur = conn.cursor()

root = tk.Tk()
root.geometry("300x200")
root.resizable(0,0)

root.title("Artist-Database-helper")

artistLabel = Label(root, text="Artist:", anchor="w")
artistEntry = Entry(root, width=100, borderwidth=0)

dateLabel = Label(root, text="Date:", anchor="w")
dateEntry = Entry(root, width=100, borderwidth=0)

venueLabel = Label(root, text="Venue:", anchor="w")
venueEntry = Entry(root, width=100, borderwidth=0)

addArtistButton = Button(root, text="Add", command=lambda: addEntryFromGUI())

gridAllTheThings()
root.mainloop()
printTableToCMD()

conn.close()