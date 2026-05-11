import curses

# Function for creating GUI based on List Options
def select_from_list(stdscr, title, options):
    current = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, title)
        stdscr.addstr(1, 0, "─" * 30)

        for i, option in enumerate(options):
            if i == current:
                stdscr.addstr(i + 2, 0, f" > {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 0, f"  {option}")
        
        stdscr.addstr(len(options) + 3, 0, "↑↓ to move, Enter to select, Q to go back")

        key = stdscr.getch()

        if key == curses.KEY_UP and current > 0:
            current -= 1
        elif key == curses.KEY_DOWN and current <len(options) - 1:
            current += 1
        elif key == ord('\n'):
            return options[current]
        elif key == ord('q'):
            return None

def main_menu(stdscr):
    options = ["View Calander", "Add Entry", "Edit Entry", "Delete Entry"]
    chosen_option = select_from_list(stdscr, "Select an option:", options)

    if chosen_option == "View Calander":
        print("1:Working")
    
    elif chosen_option == "Add Entry":
        print("2:Working")
    
    elif chosen_option == "Edit Entry":
        print("3:Working")

    else:
        print("4:Working")


curses.wrapper(main)

