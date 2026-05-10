import datetime
import subprocess
date = datetime.datetime.now()

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

Day1 = Day(Entry(), Rating())

print(f"Day: " + Day1.day)
print(f"Mood: " + Day1.rating)
print(f"Entry: " + Day1.entry)
