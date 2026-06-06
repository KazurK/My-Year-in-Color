#pylint:disable=E0606
import json
import os
from datetime import datetime
from helper import clear_console


diary = os.path.join(os.path.dirname(__file__), "diary.json")
#Json save
def save_json(data):
    with open (diary, "w") as f:
        json.dump(data, f, indent=2)

#Json load, called in main
def load_json():
        if os.path.exists(diary):
            with open(diary, "r") as f:
                return json.load(f)
    
    
#add entry  
def add_entry(data):
    clear_console()
    intro = input(f"Day: {datetime.now().strftime("%x")}, Entry: ")
    clear_console()
    
    for x in data['emotions']:
        print(x)
        
    color = input("enter color for emotion ")

    mood = None

    #searches to see if the color mathes with an emotion in dairy.json
    for x in data['emotions']:
        split = x.split(" = ")       
        if color.strip().lower() == split[0].lower():
            mood = x
            break

    if mood is None:
        print("Color not recognised, please try again.")
        return 
       
    #formating entries for json save
    entry = {"id": len(data['diary']) + 1,
              'entry': intro, 
              'emotion': mood, 
              'date': datetime.now().strftime("%c")
    }
    
    #save json
    data['diary'].append(entry)
    save_json(data)
    clear_console()
    print("Entry saved")
    
#delete entry
def delete_entry(data):
    if not data['diary']:
        print("No entries to delete")
        return 
    
    for line in data['diary']:
        print(f"ID: {line['id']}  |  {line['date']} |  {line['emotion'][:25]}  |  {line['entry'][:50]}")
        
    #remove entry from diary and save json
    Delete = int(input("Delete entry: ")) - 1 #account for zero index
    data['diary'].pop(Delete)
    save_json(data)
    clear_console()
    print("Entry deleted")
     
        

#edit entry
def edit_entry(data):

    if not data['diary']:
        print("No entries to edit")
        return 
    
    for line in data['diary']:
        print(f"ID: {line['id']}  |  {line['date']} |  {line['emotion'][:25]}  |  {line['entry'][:50]}")
    
    editNum = int(input("Edit entry: ")) - 1 #grabs the index of the entry we want to edit, account for zero index
    clear_console()
    editText = input("Edit Text: ") #gets the new text from user
    
    #new entry formatted with new text while saving other info like id, date, emotion, etc
    editEntry = {"id": data['diary'][editNum]['id'], "entry": editText, "emotion": data['diary'][editNum]['emotion'], "date": data['diary'][editNum]['date'] }
    
    data['diary'].pop(editNum) #removes old entry 
    data['diary'].insert(editNum, editEntry) #adds new entry
    save_json(data) #save json
    clear_console()
    print(f"Entry No.{editNum + 1} edited")
    
        
#view calander
def view_calander(data):
    
    if not data['diary']:
        print("No entries to view")
        return 
    
    #were high lol but had an idea to add a visual calander 
    #but idk how i would use colours 
        
    for line in data['diary']:
        print(f"ID: {line['id']} |  {line['date']} |  {line['emotion'][:25]}  |  {line['entry'][:50]}")
    
    viewNum = int(input("View entry:")) -1 #account for zero index
    clear_console()
    #display selected entry
    print(f"id: {data['diary'][viewNum]['id']}\n date: {data['diary'][viewNum]['date']} / emotion: {data['diary'][viewNum]['emotion']}\n entry: {data['diary'][viewNum]['entry']}")

#add emotion
def add_emotion(data):
    addColor = input("Type color: ") 
    addEmotion = input("Type emotion: ") 

    save = f"{addColor} = {addEmotion}" #format new emotion
    data['emotions'].append(save) #save json
    save_json(data)
    clear_console()
    print(f"Added + {save}")
    
    
def main():
    data = load_json()
    
    menu = ["1 -- View calander", "2 -- Add entry", "3 -- Edit entry", "4 -- Delete entry", "5 -- Add emotion"]
    for x in menu:
        print(x)
    select = int(input("Please enter number: "))
    
    if select == 1:
        view_calander(data)
    elif select == 2:
        add_entry(data)
    elif select == 3:
        edit_entry(data)
    elif select == 4:
        delete_entry(data)
    elif select == 5:
        add_emotion(data)
    else:
        print("Please select a valid option")
        
        
    
if __name__ == "__main__":
    main()
