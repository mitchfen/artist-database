import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from sqlite3 import Error
import re
from commandLineInterface import printTableToCMD

# Create all the GUI elements, and handle button clicks
def buildGUI(connector, cursor):

    # Main Tkinter window
    mainWindow = tk.Tk()
    mainWindow.configure(background = "#44475a")
    mainWindow.geometry("400x200")
    mainWindow.resizable(0,0)
    mainWindow.title("Artist-Database-helper")

    # Labels and text entry boxes
    artistLabel = Label(mainWindow, bg="#44475a", fg="#f8f8f2", text="Artist:")
    artistEntry = Entry(mainWindow, width=100, borderwidth=0)
    
    dateLabel = Label(mainWindow, bg="#44475a", fg="#f8f8f2", text="Date (YYYY-MM-DD):", )
    dateEntry = Entry(mainWindow, width=100, borderwidth=0)
    
    venueLabel = Label(mainWindow, bg="#44475a", fg="#f8f8f2",  text="Venue:")
    venueEntry = Entry(mainWindow, width=100, borderwidth=0)

    # Button objects
    addButton = Button(mainWindow, bg = "#50fa7b", bd = "0", activebackground = "#f1fa8c", text="Add", command=lambda: 
    addEntryFromGUI(connector, artistEntry, dateEntry, venueEntry))
    
    viewButton = Button(mainWindow, bg = "#8be9fd", bd = "0", activebackground = "#f1fa8c", text="View Table", command=lambda: viewTable(mainWindow))
    
    clearButton = Button(mainWindow, bg = "#ff5555", bd = "0", activebackground = "#f1fa8c", text="Clear the table", command=lambda: clearTable(connector, mainWindow))

    # Pace all gui elements with grid method, Sticky is how I am justifying left
    artistLabel.grid(sticky= W, row=0, column=0)
    artistEntry.grid(row=1, column=0)
    venueLabel.grid(sticky= W, row=2, column=0)
    venueEntry.grid(row=3, column=0)
    dateLabel.grid(sticky= W, row=4, column=0)
    dateEntry.grid(row=5, column=0)

    addButton.grid(sticky= W, row=6, column=0)
    viewButton.grid(sticky = W, row=7, column=0)
    clearButton.grid(sticky = W, row=8, column=0)

    mainWindow.mainloop()
    printTableToCMD(cursor)

# Add a new tuple to the table when add is clicked
def addEntryFromGUI(connector, artistEntry, dateEntry, venueEntry):

    # Get the values from GUI
    artist = artistEntry.get()
    date = dateEntry.get()
    venue = venueEntry.get()

    # TODO: Use regex or some method to validate date format

    # Enter into table
    sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "
    connector.execute(sql)
    connector.commit()

    # Clear the GUI entry fields
    artistEntry.delete(0, END)
    dateEntry.delete(0, END)
    venueEntry.delete(0,END)

# Clear the table by dropping and rebuilding it
def clearTable(connector, mainWindow):

    # Bring up a new window to confirm clearing the table
    popupWindow = tk.Toplevel(mainWindow)
    popupWindow.resizable(0,0)
    #popupWindow.geometry("100x20")
    popupWindow.title("Confirm")
    popupWindow.configure(background = "#44475a")

    confirmClear = Button(popupWindow, bg = "#ff5555", bd = "0", activebackground = "#f1fa8c", text="Confirm clear", command=lambda: clearConfirmed(connector, popupWindow))
    
    confirmClear.grid(sticky = W, row = 0, column = 0)

    # Actually send SQL command to clear table if confirmation pressed
    def clearConfirmed(connector, popupWindow):
        sql = "DROP TABLE showTable;"
        connector.execute(sql)
        connector.commit()
        connector.execute('''CREATE TABLE IF NOT EXISTS showTable(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Artist  CHAR(30),
        Date CHAR(30),
        Venue CHAR(30));''')
        connector.commit()
        popupWindow.destroy()
    
# TODO
def viewTable(mainWindow):
    
    # New popup to display the table
    popupWindow = tk.Toplevel(mainWindow)
    popupWindow.resizable(0,0)
    #popupWindow.geometry("500x500")
    popupWindow.title("Confirm")
    popupWindow.configure(background = "#44475a")

    tempList = [['Test', 'Test'], ['Test2', 'Test2'], ['Test3', 'Test3'], ['Test4', 'Test4']]

    cols = ('Artist', 'Venue', 'Date')
    listBox = ttk.Treeview(popupWindow, columns=cols, show='headings')
    
    for i, (Artist, Venue) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, Artist, Venue))

    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=0, column=0, columnspan=2)

    def close():
        popupWindow.destroy()

    closeButton = tk.Button(popupWindow, text="Close", width=15, command=close)
    closeButton.grid(sticky = W, row=4, column=0)
    printButton = tk.Button(popupWindow, text="Print", width=15, command=close)
    printButton.grid(sticky = E, row=4, column=1)