
# current date and time manipulation
from datetime import datetime

now = datetime.now()

# to get year from datetime
year = now.strftime("%Y")
print("current Year is:", year)

# to get month from datetime
month = now.strftime("%m")
print("current Month is:", month)

# to get day from datetime
day = now.strftime("%d")
print("current Day is:", day)

# to format time
time = now.strftime("%H:%M:%S")
print("current Time is:", time)
timeIs = now.strftime("%H-%M-%S")
print("current Time is:", timeIs)
# format date and year
date_time = now.strftime("%d-%m-%Y")
print("To day is:",date_time,"And the time is", timeIs)

# format time
date = now.strftime("%d/%m/%Y")
this_time = now.strftime("%H:%M:%S")
print("To day is:",date,"And the time is",this_time)
