import sqlite3
import tkinter as tk
from tkinter import *
from sqlite3 import Error
from commandLineInterface import printTableToCMD

# Create all the GUI elements, and handle button clicks
def buildGUI(connector, cursor):

    mainWindow = tk.Tk()
    mainWindow.geometry("500x500")
    mainWindow.resizable(0,0)

    mainWindow.title("Artist-Database-helper")

    artistLabel = Label(mainWindow, text="Artist:")
    artistEntry = Entry(mainWindow, width=100, borderwidth=0)

    dateLabel = Label(mainWindow, text="Date:", )
    dateEntry = Entry(mainWindow, width=100, borderwidth=0)

    venueLabel = Label(mainWindow, text="Venue:")
    venueEntry = Entry(mainWindow, width=100, borderwidth=0)

    addButton = Button(mainWindow, text="Add", command=lambda: addEntryFromGUI(connector, artistEntry, dateEntry, venueEntry))
    editButton = Button(mainWindow, text="Edit", command=lambda: addEntryFromGUI())

    artistLabel.grid(sticky= W, row=0, column=0)
    artistEntry.grid(row=1, column=0)
    dateLabel.grid(sticky= W, row=2, column=0)
    dateEntry.grid(row=3, column=0)
    venueLabel.grid(sticky= W, row=4, column=0)
    venueEntry.grid(row=5, column=0)
    addButton.grid(sticky= W, row=6, column=0)
    editButton.grid(sticky = W, row=7, column=0)

    mainWindow.mainloop()
    printTableToCMD(cursor)

# Add a new tuple to the table when add is clicked
def addEntryFromGUI(connector, artistEntry, dateEntry, venueEntry):
    # Casting to string may not be needed here but I'm used to Java/C++, leave it for now
    print(artistEntry.get())
    artist = artistEntry.get()
    date = dateEntry.get()
    venue = venueEntry.get()

    sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "
    connector.execute(sql)
    connector.commit()

# TODO
def editEntryFromGUI():
    return

# TODO
def removeEntryFromGUI():
    return