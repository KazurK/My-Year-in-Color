import os
import json
import datetime
import subprocess
date = datetime.datetime.now()

entry_file = "Entries.json"

def load_data():
    if os.path.exists(entry_file):
        with open(entry_file, "r") as f:
            return json.load(f)
        
        default_categories = [
            "purple = Happy", 
            "red = Stressed/Annoyed", 
            "grey = Average", 
            "green = Productive", 
            "blue = Content, at Peace", 
            "black = idc idc whatever"]
    return {"rating": default_categories, "entries": []}

def save_data(data):
    with open (entry_file, "w") as f:
        json.dump(data, f, indent=2)

def rating():
    Ratings = ["purple = Happy", "red = Stressed/Annoyed", "grey = Average", "green = Productive", "blue = Content, at Peace", "black = idc idc whatever"]
    for mood in Ratings:
        print(mood)
    print("Rating: ")
    x = input()
    subprocess.run(['clear'])
    return x

def add_entry(data):
    intro = f"Date:{date.strftime("%x")}, Entry: "
    print(intro)

    text = input()
    rating = rating()
    entry = {
        "id": len(data["entries"]) + 1, 
        "entry": text,
        "rating": rating,
        "date": date.strftime("%c")
    }

    data["entries"].append(entry)
    save_data(data)
    print("Entry saved!")
    
def view_calender(data):
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
            print(f"✓ Entry {entry_id} deleted.")
        else:
            print("No entry with that ID.")
    except ValueError:
        print("Please enter a valid number.")

