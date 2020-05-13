# Import my own modules
import gui
import cli
import mitchDAO

def main():
    
    # Instantiate the Data Access Object from DAO class in mitchDAO.py
    DAO = mitchDAO.DAO('Shows.db')
    
    # Build the graphical user interface
    gui.buildGUI(DAO)
    # Commented out the command line interface now that the GUI is working
    #cli.cmdPromptLoop(DAO)

    # Close SQLite connector before exit
    DAO.close()

if __name__ == '__main__':
    main()
