import os
import json
import subprocess
import curses
from datetime import datetime
from cursesHelper import show_message, get_input, select_from_list, draw_border, center_text

entry_file = "Entries.json"

# JSON data functions
def load_data():

    default_categories = [
        "purple = Happy", 
        "red = Stressed/Annoyed", 
        "grey = Average", 
        "green = Productive", 
        "blue = Content, at Peace", 
        "black = idc idc whatever"]
        
    if os.path.exists(entry_file):
        with open(entry_file, "r") as f:
            return json.load(f)
        
    return {"rating": default_categories, "entries": []}

def save_data(data):
    with open (entry_file, "w") as f:
        json.dump(data, f, indent=2)

#add entry and save to json file
def add_entry(stdscr, data):
    Ratings = ["purple = Happy", "red = Stressed/Annoyed", "grey = Average", "green = Productive", "blue = Content, at Peace", "black = idc idc whatever"]

    intro = f"Date:{datetime.now().strftime("%x")}, Entry: "
    text = get_input(stdscr, intro, multiline=True)
    rating = select_from_list(stdscr, "Rating:", Ratings)
    entry = {
        "id": len(data["entries"]) + 1, 
        "entry": text,
        "rating": rating,
        "date": datetime.now().strftime("%c")
    }

    data["entries"].append(entry)
    save_data(data)
    show_message(stdscr, "Entry saved!")
    
#load entries from json and display in terminal
def view_calender(stdscr, data):
    entries = data["entries"]

    if not entries:
        print("No entries found.")
        return
    
    idx = 0
    while True:
        stdscr.clear()
        draw_border(stdscr)
        h, w =stdscr.getmaxyx()

        #draws and formats entries
        entry = entries[idx]
        stdscr.addstr(3, 3, f"Date: {entry['date']}")
        stdscr.addstr(4, 3, f"Rating: {entry['rating']}")
        stdscr.addstr(5, 3, "-" * (w - 6))

        #word wrapping in case terminal is too small
        words = entry["entry"].split()
        lines, line = [], ""
        for word in words:
            if len(line) + len(word) + 1 <= w - 6:
                line = f"{line} {word}".strip()
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)

        for i, ln in enumerate(lines):
            row = 6 + i
            if row >= h - 3:
                break
            stdscr.addstr(row, 3, ln)

        center_text(stdscr, h - 2, "← prev   → next   q back")
        stdscr.refresh()

        #wrapper for selecting entries
        key = stdscr.getch()
        if key == curses.KEY_LEFT and idx > 0:
            idx -= 1
        elif key == curses.KEY_RIGHT and idx < len(entries) - 1:
            idx += 1
        elif key == ord("q"):
            return


def delete_entry(stdscr, data):
    if not data["entries"]:
        show_message(stdscr, "No entries to delete.")
        return
 
    # Build a list of labels to pick from
    labels = [f"{e['date']}  |  {e['rating'][:20]}" for e in data["entries"]]
    labels.append("Cancel")
 
    chosen = select_from_list(stdscr, "Delete which entry?", labels)
    if chosen is None or chosen == "Cancel":
        return
 
    idx = labels.index(chosen)
    data["entries"].pop(idx)
    save_data(data)
    show_message(stdscr, "✓ Entry deleted.")


