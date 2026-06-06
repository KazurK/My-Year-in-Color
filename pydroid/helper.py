import os

#clear console
def clear_console():
    
    os.system('cls' if os.name == 'nt' else 'clear')

#calander functions
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_months(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    return 0 

def get_first_day_in_month(month, year):
    #essecially this algoritm gets the first day in the month/ zeller's congurence
    if month < 3:
        month += 12
        year -= 1

    q = 1
    k = year % 100
    j = year // 100
    h = (q + (13 * (month + 1) // 5) + k + (k // 4) + (j // 4) -(2 * j)) % 7
    return (h + 5) % 7

def print_calander(month, year):
    daysInMonth = get_days_in_months(month, year)
    firstDay = get_first_day_in_month(month, year)

    print(f"\n {month:02d}/{year}")
    print("Mon Tue Wed Fri Sat Sun")

    for x in range(firstDay):
        print("    ", end="")
    
    for day in range(1, daysInMonth + 1):
        print(f"{day:3d} ", end="")
        if (firstDay + day) % 7 == 0:
            print()
    print()


    

    
  
