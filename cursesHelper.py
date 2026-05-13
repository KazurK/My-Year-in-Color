import curses
from curses.textpad import Textbox

#draws border for display on terminal
def draw_border(stdscr):
    stdscr.border()

#centers text when displayed on terminal
def center_text(stdscr, y, text, attr=0):
    h, w = stdscr.getmaxyx()
    x = max(0, (w - len(text)) // 2)
    stdscr.addstr(y, x, text, attr)

#print function
def show_message(stdscr, msg):
    stdscr.clear()
    draw_border(stdscr)
    h, w = stdscr.getmaxyx()
    center_text(stdscr, h // 2, msg)
    center_text(stdscr, h // 2 + 2, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()    

#input function 
def get_input(stdscr, title, multiline=False):

    #draws boarder and displays title
    stdscr.clear()
    draw_border(stdscr)
    h, w = stdscr.getmaxyx()
    center_text(stdscr, 2, title, curses.A_BOLD)

    #decides the size of the input box, uses multiline for entries and uses single line for mood ratings
    if multiline:
        hint = "Ctrl-G to save      Ctrl-C to cancel"
        box_h, box_w = h - 10, w - 6
        box_y, box_x = 5, 3
    else:
        hint = "Enter to Confirm    Ctrl-C to cancel"
        box_h, box_w = 1, w - 6
        box_y, box_x = 5, 3   
    
    center_text(stdscr, h - 2, hint)

    #draws visible border for input box
    for row in range(box_y - 1, box_y + box_h + 1):
        for col in range(box_x - 1, box_x + box_w + 1):
            if row == box_y - 1 or row == box_y + box_h:
                try:
                    stdscr.addch(row, col, "-")
                except curses.error:
                    pass
            elif col == box_x - 1 or col == box_x + box_w:
                try:
                    stdscr.addch(row, col, "|")
                except curses.error:
                    pass

    stdscr.refresh()

    #creates the actual input box
    edit_win = curses.newwin(box_h, box_w, box_y, box_x)
    box = Textbox(edit_win)

    #gets text
    try:
        box.edit()
    except KeyboardInterrupt:
        return None
    
    text = box.gather().strip()
    return text if text else None

# Function for creating GUI based on List Options
def select_from_list(stdscr, title, options):
    current = 0

    while True:
        stdscr.clear()
        draw_border(stdscr)
        h, w = stdscr.getmaxyx()
        center_text(stdscr, 2, title, curses.A_BOLD)

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
        elif key in (curses.KEY_ENTER, 10, 13):
             return options[current]
        elif key == ord('q'):
            return None