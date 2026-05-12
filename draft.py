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
    text = input()
    rating = Rating()
    entry = {
        "entry": text,
        "rating": rating,
        "date": date.strftime("%c")
    }
    data["entries"].append(entry)
    save_data(data)
    print("Entry saved!")
    


