import sqlite3
from sqlite3 import Error
from tabulate import tabulate

###################################################
#   Command line code
#   This code was written for the command line functionality.
#   No longer needed now that the GUI is functional
###################################################

# Main program loop, where user input is accepted
def cmdPromptLoop(connector, cursor):

    keepGoing = True
    while(keepGoing):

        print("1) Print the table")
        print("2) Add a new entry")
        print("3) Remove an entry")
        print("4) Edit an entry")
        print("5) Clear the table")
        print("6) Exit")

        i = int(input("Command: "))
        if i == 1:  printTableToCMD(cursor)
        elif i == 2: addEntryFromCMD(connector)
        elif i == 3: removeEntryFromCMD(connector)
        elif i == 4: editEntryFromCMD(connector)
        elif i == 5: clearTable(connector)
        elif i == 6: keepGoing = False

# Print the table using tabulate
def printTableToCMD(cursor):

        cursor.execute("SELECT * FROM showTable")
        entries = []
        entries = cursor.fetchall()
        print(tabulate(entries))

# Get user input from CMD, store in database
def addEntryFromCMD(connector):

    artist = input("Artist: ")
    date = input("Date: ")
    venue = input("Venue: ")

    # TODO: Use regex or some method to validate date format

    sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "

    connector.execute(sql)
    connector.commit()

# Drop and recreate the table to clear it
def clearTable(connector):

    checkIfSure = input("Are you sure? (yes or no)")
    keepGoing = True
    while(keepGoing):
        if checkIfSure == "yes": 
            sql = "DROP TABLE showTable;"
            connector.execute(sql)
            connector.commit()
            connector.execute('''CREATE TABLE IF NOT EXISTS showTable(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Artist  CHAR(30),
            Date CHAR(30),
            Venue CHAR(30));''')
            connector.commit()
            keepGoing = False
        elif checkIfSure == "no":
            keepGoing = False
            return
        else:
            checkIfSure = input("invalid input, please enter \"yes\" or \"no\"")
            

# TODO
def removeEntryFromCMD(connector):
   return 

# TODO
def editEntryFromCMD(connector):
    return