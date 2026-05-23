#pylint:disable=E0606
import json
import os
from datetime import datetime
from helper import clear_console

dairy = os.path.join(os.path.dirname(__file__), "diary.json")

def save_json(data):
    with open (dairy, "w") as f:
        json.dump(data, f, indent=2)
        
def load_json():
        default_categories = [
        "purple = Happy", 
        "red = Stressed/Annoyed", 
        "grey = Average", 
        "green = Productive", 
        "blue = Content, at Peace", 
        "black = idc idc whatever"]
        
        if os.path.exists(dairy):
            with open(dairy, "r") as f:
                return json.load(f)

        return {"rating": default_categories,         "entries": []}
    
    
    
def add_entry(data):
    intro = input(f"Day: {datetime.now.strftime("%x")}, Entry: ")
    clear_console()
    
    emotions =[
        "purple = Happy", 
        "red = Stressed/Annoyed", 
        "grey = Average", 
        "green = Productive", 
        "blue = Content/At peace", 
        "black = idc idc whatever"]
    
    for x in emotions:
        print(x)
        
    color = input("enter color for emotion ")
    if color == "purple":
       mood = "purple = Happy"
    elif color == "red" :
       mood = "red = Stressed/Annoyed"
    elif color == "grey":
       mood = "grey = Average"
    elif color == "green":
       mood = "green = Productive"
    elif color == "blue":
       mood = "blue = Content/At peace"
    elif color == "black":
       mood = "black = idc idc whatever"
       
       
    entry = {"id": len(data["dairy"]) + 1, "entry": intro, "emotion": mood, "date": datetime.now().strftime("%c")
    }
    
    data["dairy"].append(entry)
    save_json(data)
    clear_console()
    print("Entry saved")
    
def delete_entry(data):
    
def edit_entry(data):
def view_calander(data):
    
def main():
    data = load_json()
    
    