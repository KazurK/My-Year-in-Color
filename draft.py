import datetime
import subprocess
import curses
date = datetime.datetime.now()

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


class Day:
    def __init__(self, entry, rating):
        self.entry = entry
        self.rating = rating
    day = date.strftime("%a")
    date = date.strftime("%c")



def Rating():
    Ratings = ["purple = Happy", "red = Stressed/Annoyed", "grey = Average", "green = Productive", "blue = Content, at Peace", "black = idc idc whatever"]
    for mood in Ratings:
        print(mood)
    print("Rating: ")
    x = input()
    subprocess.run(['clear'])
    return x

def Entry():
    intro = f"Date:{date.strftime("%x")}, Entry: "
    print(intro)
    return input()

day1 = Day(Entry(), Rating())

day2 = Day(Entry(), Rating())

print(f"Day: " + day1.day)
print(f"Mood: " + day1.rating)
print(f"Entry: " + day1.entry)
