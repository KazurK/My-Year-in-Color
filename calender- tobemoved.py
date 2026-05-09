import tkinter as tk
import calendar
from datetime import datetime

# Get current month and year
now = datetime.now()
year = now.year
month = now.month

# Create main window
root = tk.Tk()
root.title("My Year In Colour")

# Month label
month_name = calendar.month_name[month]
label = tk.Label(root, text=f"{month_name} {year}", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=7)

# Weekday headers
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, day in enumerate(days):
    tk.Label(root, text=day).grid(row=1, column=i)

# Get month calendar layout
month_days = calendar.monthcalendar(year, month)

# Create buttons for each day
for row_index, week in enumerate(month_days):
    for col_index, day in enumerate(week):
        if day == 0:
            tk.Label(root, text=" ").grid(row=row_index+2, column=col_index)
        else:
            btn = tk.Button(root, text=str(day), width=5, height=2)
            btn.grid(row=row_index+2, column=col_index)

root.mainloop()