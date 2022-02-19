
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

# to format time in Hours:Minutes:Seconds
time = now.strftime("%H:%M:%S")
print("current Time is:", time)

# format date and year
date_time = now.strftime("%d/%m/%Y")
print("To day is:",date_time)

# format time
this_time = now.strftime("%H:%M:%S")
print("The time is know:",this_time)