import gui
import mitchDAO

def main():
    DAO = mitchDAO.DAO('Shows.db')
    gui.buildGUI(DAO)
    DAO.close()

if __name__ == '__main__':
    main()
