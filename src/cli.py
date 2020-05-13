from tabulate import tabulate


# Main program loop, where user input is accepted
def cmdPromptLoop(DAO):

    keepGoing = True
    while(keepGoing):

        print("\n")
        print("1) Print the table")
        print("2) Add a new entry")
        print("3) Remove an entry")
        print("4) Edit an entry")
        print("5) Clear the table")
        print("6) Exit")

        i = int(input("Command: "))
        if i == 1:  printTableToCMD(DAO)
        elif i == 2: addEntryFromCMD(DAO)
        elif i == 3: removeEntryFromCMD(DAO)
        elif i == 4: editEntryFromCMD(DAO)
        elif i == 5: clearTable(DAO)
        elif i == 6: keepGoing = False

# Print the table using tabulate
def printTableToCMD(DAO):

    print("\n")
    entries = DAO.collectAllEntries()
    print(tabulate(entries))

# Get user input from CMD, store in database
def addEntryFromCMD(DAO):

    print("\n")
    artist = input("Artist: ")
    date = input("Date: ")
    venue = input("Venue: ")

    DAO.addEntry(artist, date, venue)

# Drop and recreate the table to clear it
def clearTable(DAO):

    print("\n")
    checkIfSure = input("Are you sure? (yes or no): ")
    keepGoing = True
    while(keepGoing):
        if checkIfSure == "yes": 
            DAO.clearTable()
            print("TABLE HAS BEEN CLEARED.")
            keepGoing = False
        elif checkIfSure == "no":
            keepGoing = False
            return
        else:
            checkIfSure = input("invalid input, please enter \"yes\" or \"no\": ")
            

# TODO Complete this function
def removeEntryFromCMD(DAO):
   return 

# TODO Complete this function
def editEntryFromCMD(DAO):
    return
