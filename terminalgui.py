import curses
import subprocess
from draft import view_calender, add_entry, delete_entry, load_data
from cursesHelper import select_from_list


def main_menu(stdscr):
    data = load_data()

    options = ["View Calander", "Add Entry", "Edit Entry", "Delete Entry"]
    chosen_option = select_from_list(stdscr, "Select an option:", options)

    if chosen_option == "View Calander":
        view_calender(data)
    
    elif chosen_option == "Add Entry":
        subprocess.run(['clear'])
        curses.endwin()       
        add_entry(data)
        stdscr = curses.initscr()
    
    elif chosen_option == "Delete Entry":
        delete_entry(data)


curses.wrapper(main_menu)

