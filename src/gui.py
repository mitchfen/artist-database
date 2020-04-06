import sqlite3
from sqlite3 import Error

import tkinter as tk
from tkinter import ttk
from tkinter import *


# Create all the GUI elements, and handle button clicks
def buildGUI(connector, cursor):

    # Main Tkinter window
    mainWindow = tk.Tk()
    mainWindow.configure(background = "#44475a")
    #mainWindow.geometry("400x200")
    mainWindow.resizable(0,0)
    mainWindow.title("Artist-DB Helper")

    # Labels and text entry boxes
    artistLabel = Label(mainWindow, bg="#44475a", fg="#f8f8f2", text="Artist:")
    artistEntry = Entry(mainWindow, width=40, borderwidth=0)
    
    dateLabel = Label(mainWindow, bg="#44475a", fg="#f8f8f2", text="Date (YYYY-MM-DD):", )
    dateEntry = Entry(mainWindow, width=40, borderwidth=0)
    
    venueLabel = Label(mainWindow, bg="#44475a", fg="#f8f8f2",  text="Venue:")
    venueEntry = Entry(mainWindow, width=40, borderwidth=0)

    spacer = Label(mainWindow, bg="#44475a", fg="#f8f8f2", text="")

    # Button objects
    addButton = Button(mainWindow, bg = "#50fa7b", width = 38, bd = "0", activebackground = "#f1fa8c", text="Add", cursor = "hand2", command=lambda: addEntryFromGUI(connector, artistEntry, dateEntry, venueEntry))
    
    viewButton = Button(mainWindow, bg = "#8be9fd", width = 38, bd = "0", activebackground = "#f1fa8c", text="View Table", cursor = "hand2", command=lambda: viewTable(mainWindow, cursor))
    
    clearButton = Button(mainWindow, bg = "#ff5555", width = 38, bd = "0", activebackground = "#f1fa8c", text="Clear the table", cursor = "hand2", command=lambda: clearTable(connector, mainWindow))

    closeButton = Button(mainWindow, width = 38, bd='0', activebackground = "#f1fa8c", text="Exit", cursor = "hand2", command=lambda: closeMainWindow(mainWindow))

    # Place all gui elements with grid method, Sticky is how I am justifying left
    artistLabel.grid(row=0, column=0)
    artistEntry.grid(row=1, column=0)
    dateLabel.grid(row=2, column=0)
    dateEntry.grid(row=3, column=0)
    venueLabel.grid(row=4, column=0)
    venueEntry.grid(row=5, column=0)
    spacer.grid(row=6, column = 0)
    addButton.grid(row=7, column=0)
    viewButton.grid(row=8, column=0)
    clearButton.grid(row=9, column=0)
    closeButton.grid(row=10, column = 0)

    mainWindow.mainloop()

# Add a new tuple to the table when add is clicked
def addEntryFromGUI(connector, artistEntry, dateEntry, venueEntry):

    # Get the values from GUI
    artist = artistEntry.get()
    date = dateEntry.get()
    venue = venueEntry.get()

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
def viewTable(mainWindow, cursor):
    
    # New popup to display the table
    popupWindow = tk.Toplevel(mainWindow)
    popupWindow.resizable(0,0)
    popupWindow.title("Table view")
    popupWindow.configure(background = "#44475a")

    # Grab the information from Sqlite, store in list
    cursor.execute("SELECT * FROM showTable")
    entries = []
    entries = cursor.fetchall()
    
    # TODO: Get a better understanding of how to style this treeview
    # Set ttk style need to color treeview
    style = ttk.Style(popupWindow)
    style.theme_use("clam")
    #style.configure("Treeview", background="#44475a", foreground="#f8f8f2")
    style.configure("Heading", background = "#44475a", foreground="#f8f8f2", relief="flat")
    
    # Declare treeview and insert information from list
    cols = ('Number', 'Artist', 'Date', 'Venue')
    listBox = ttk.Treeview(popupWindow, columns=cols, show='headings')
    
    for i, (Number, Artist, Date, Venue) in enumerate(entries, start=1):
        listBox.insert("", "end", values=(Number, Artist, Date, Venue))

    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=0, column=0, columnspan=2)


    # Function called by close button
    def closeViewTable():
        popupWindow.destroy()

    # Buttons at the bottom of the view page
    closeButton = tk.Button(popupWindow, bg = "#ff5555", bd = "0", activebackground = "#f1fa8c", text="Close", width=15, command=closeViewTable)
    closeButton.grid(sticky = W, row=4, column=0)
    printButton = tk.Button(popupWindow, bg = "#8be9fd", bd = "0", activebackground = "#f1fa8c", text="Print", width=15, command=closeViewTable)
    printButton.grid(sticky = E, row=4, column=1)

def closeMainWindow(mainWindow):
    mainWindow.destroy()