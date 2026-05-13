import curses
import subprocess
from draft import view_calender, add_entry, delete_entry, load_data
from cursesHelper import select_from_list


def main_menu(stdscr):
    data = load_data()

    options = ["View Calander", "Add Entry", "Edit Entry", "Delete Entry"]
    chosen_option = select_from_list(stdscr, "Select an option:", options)

    if chosen_option == "View Calander":
        view_calender(stdscr, data)
    
    elif chosen_option == "Add Entry":
        curses.curs_set(1)
        add_entry(stdscr, data)
        curses.curs_set(0)
    
    elif chosen_option == "Delete Entry":
        delete_entry(stdscr, data)



if __name__ == "__main__":
    curses.wrapper(main_menu)

