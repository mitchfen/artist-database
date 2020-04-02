import os
import sqlite3
import tkinter as tk
from tkinter import *
from sqlite3 import Error

# Import my own code
from commandLineInterface import cmdPromptLoop
from gui import buildGUI

# Connect to the SQL Shows.db file and create the only table
try :
    connector = sqlite3.connect('Shows.db')
except Error as e:
    print(e)

connector.execute('''CREATE TABLE IF NOT EXISTS showTable(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Artist  CHAR(30),
Date CHAR(30),
Venue CHAR(30));''')
connector.commit()

cursor = connector.cursor()

# Build the graphical user interface
buildGUI(connector, cursor)

# Commented out the command line interface now that the GUI is working
#cmdPromptLoop(connector, cursor)

connector.close()