'''import math

# Import example module
import examples3_module as example

# Constants
print("Math constants")
print("==============")
print(math.pi)
print(math.e)
print("")

# Functions
print("Math functions")
print("==============")
print(math.sqrt(25))
print(math.trunc(14.83483))
print(math.sin(math.pi / 2.0))
print("")

# Dir
print("Dir")
print("===")
print(dir(math))
print(dir(example))
print("")

print(example.message)
print(math.__name__)
print(example.__name__)

def all(iterable):
    for element in iterable:
        if not element:
            return False
        return True
        '''

import datetime

# Create some dates
print("Creating Dates")
print("==============")

date1 = datetime.date(1999, 12, 31)
date2 = datetime.date(2000, 1, 1)
date3 = datetime.date(2016, 4, 15)
# date4 = datetime.date(2012, 8, 32)

# Today's date
today = datetime.date.today()
print(today)

print(date1)
print(date2)
print(date3)

print("")

# Compare dates
print("Comparing Dates")
print("===============")

print(date1 < date2)
print(date3 <= date1)
print(date2 == date3)

print("")

# Subtracting dates
print("Subtracting Dates")
print("=================")

diff = date2 - date1
print(diff)
print(diff.days)

diff2 = date3 - date2
print(diff2)
print(diff2.days)

print("")
