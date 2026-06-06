import os
from helper import print_calander
from datetime import datetime

month = int(datetime.now().strftime("%m"))
year = int(datetime.now().strftime("%Y"))
print_calander(month, year)