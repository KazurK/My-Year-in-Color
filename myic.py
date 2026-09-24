from myicDatabaseQuery import *
import os
from datetime import datetime

#create database
createDatabase()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


#add entry  
def add_entry():
    
    intro = input(f"Day: {datetime.now().strftime("%x")}, Entry: ")
    clear_console()

    emotions = myicGetMoods()
    for emotion in emotions:
        print(tuple(emotion))
        
    color = input("enter color for emotion ")

    mood = None
    #searches to see if the color mathes with an emotion in emotions
    #there's probably a better way to do this using key value pairs
    for emotion in emotions:    
        if color.strip().lower() == emotion["color"].lower():
            mood = emotion["emotion"]
            break
    if mood is None:
        print("Color not recognised, please try again.")
        return 
      
    #formating entries for database save
    queryVariables = ({"date": datetime.now().strftime("%c"),
                "emotion": mood,
                "notes": intro,
                "time": "Time"})
    myicAddDay(queryVariables) #saves to database
    clear_console()
    print("Entry saved")
    
#delete entry
def delete_entry():

    #Display all entries
    myicGetAllEntries()
    deleteID = (input("Delete entry: "))
    myicDeleteEntry(deleteID) #remove from database
    clear_console()
    print("Entry deleted")
     
        

#edit entry
def edit_entry():

    myicGetAllEntries() 
    editID = int(input("Edit entry: ")) #grabs the index of the entry we want to edit
    clear_console()

    editText = input("Edit Text: ") #gets the new text from user
    myicEditEntry(editText,editID)
    clear_console()

    print(f"Entry No.{editID + 1} edited")
    
        
#view calander
def view_calander():
    clear_console()
    
    myicGetAllEntries()
    #were high lol but had an idea to add a visual calander 
    #but idk how i would use colours 

    viewID = (input("View entry:"))
    clear_console()
    #display selected entry
    myicGetSpecificEntry(viewID)

#add emotion
def add_emotion():
    addColor = input("Type color: ") 
    addEmotion = input("Type emotion: ") 

    mood = ({"color": addColor, "emotion": addEmotion})
    myicAddMood(mood)
    clear_console()

    print(f"Added + {addColor} = {addEmotion}")
    
    
def main():
    
    menu = ["1 -- View calander", "2 -- Add entry", "3 -- Edit entry", "4 -- Delete entry", "5 -- Add emotion"]
    for x in menu:
        print(x)
    select = int(input("Please enter number: "))
    
    if select == 1:
        view_calander()
    elif select == 2:
        add_entry()
    elif select == 3:
        edit_entry()
    elif select == 4:
        delete_entry()
    elif select == 5:
        add_emotion()
    else:
        print("Please select a valid option")
        
        
    
if __name__ == "__main__":
    main()
