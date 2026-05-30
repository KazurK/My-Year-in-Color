#pylint:disable=E0606
import json
import os
from datetime import datetime
from helper import clear_console


diary = os.path.join(os.path.dirname(__file__), "diary.json")

def save_json(data):
    with open (diary, "w") as f:
        json.dump(data, f, indent=2)
        
def load_json():
        if os.path.exists(diary):
            with open(diary, "r") as f:
                return json.load(f)
    
    
    
def add_entry(data):
    intro = input(f"Day: {datetime.now().strftime("%x")}, Entry: ")
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
       
       
    entry = {"id": len(data['diary']) + 1, 'entry': intro, 'emotion': mood, 'date': datetime.now().strftime("%c")
    }
    
    data['diary'].append(entry)
    save_json(data)
    clear_console()
    print("Entry saved")
    
def delete_entry(data):
    if not data['diary']:
        print("No entries to delete")
        return 
    
    for line in data['diary']:
        print(f"ID: {line['id']}  |  {line['date']} |  {line['emotion'][:25]}  |  {line['entry'][:50]}")
        
    Delete = int(input("Delete entry: ")) - 1
    data['diary'].pop(Delete)
    save_json(data)
    clear_console()
    print("Entry deleted")
     
        
        
def edit_entry(data):

    if not data['diary']:
        print("No entries to edit")
        return 
    
    for line in data['diary']:
        print(f"ID: {line['id']}  |  {line['date']} |  {line['emotion'][:25]}  |  {line['entry'][:50]}")
    
    editNum = int(input("Edit entry: ")) - 1
    clear_console()
    editText = input("Edit Text: ")
    
    editEntry = {"id": data['diary'][editNum]['id'], "entry": editText, "emotion": data['diary'][editNum]['emotion'], "date": data['diary'][editNum]['date'] }
    
    data['diary'].pop(editNum)
    data['diary'].insert(editNum, editEntry)
    save_json(data)
    clear_console()
    print(f"Entry No.{editNum + 1} edited")
    
        
    
def view_calander(data):
    
    if not data['diary']:
        print("No entries to view")
        return 
        
    for line in data['diary']:
        print(f"ID: {line['id']} |  {line['date']} |  {line['emotion'][:25]}  |  {line['entry'][:50]}")
    
    viewNum = int(input("View entry:")) -1
    clear_console()
    
    print(f"id: {data['diary'][viewNum]['id']}\n date: {data['diary'][viewNum]['date']}\n emotion: {data['diary'][viewNum]['emotion']}\n entry: {data['diary'][viewNum]['entry']}")
    
    
    
def main():
    data = load_json()
    
    print("1 -- View calander \n2 -- Add entry \n3 -- Edit entry \n4 -- Delete entry\n")
    select = int(input("Please enter number: "))
    
    if select == 1:
        view_calander(data)
    elif select == 2:
        add_entry(data)
    elif select == 3:
        edit_entry(data)
    elif select == 4:
        delete_entry(data)
    else:
        print("Please select a valid option")
        
        
    
if __name__ == "__main__":
    main()
