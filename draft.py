import os
import json
import datetime
import subprocess
from cursesHelper import show_message, get_input, select_from_list

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

    print(f"\n--- All Entries ({len(entries)} entries) ---")

    if not entries:
        print("No entries found.")
        return
    
    for entry in entries:
        print(f"\n {entry['date']}  |  {entry['category']}")
        print(entry["text"])
        print("-" * 30)

def delete_entry(data):
    view_calender(data)
    if not data["entries"]:
        return
    
    try:
        entry_id = int(input("\nEnter entry ID to delete (0 to cancel): "))
        if entry_id == 0:
            return
        original_len = len(data["entries"])
        data["entries"] = [e for e in data["entries"] if e["id"] !=entry_id]

        if len(data["entries"]) < original_len:
            save_data(data)
            print(f"Entry {entry_id} deleted.")
        else:
            print("No entry with that ID.")
    except ValueError:
        print("Please enter a valid number.")

