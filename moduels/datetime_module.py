"""
Python has a module named datetime to work with dates and times.

datetime format symbols
----------------------
%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - minute [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 59]
"""

#date: day - month - year : 10/03/2021: 2021/10/03
#time: hours: min: sec: mSec

# How are you deal with date and times in python?
# python has built in lib that datetime

# import
from datetime import date
from datetime import time
from datetime import datetime
# deltas
from datetime import timedelta


# date: year, month, day
my_birth_day = date(year=1992, month=4, day=11)
print(type(my_birth_day))
# lets print out attributes of date
print("Year:", my_birth_day.year)
print("Month:", my_birth_day.month)
print("day:", my_birth_day.day)

my_friend_birth = date(year=1990, month=6, day=30)
print(my_friend_birth)

# who is older?
if my_birth_day > my_friend_birth:
    print("my friend is older than me")

# getting delta between two dates
out = my_birth_day - my_friend_birth  # days
print(type(out))
print(out)

# -------------

# use case:  10000
# given_date: 2021/03/12

# rec_date = 2021/08/25

# How find duration

given_date = date(year=2021, month=3, day=12)
rec_date = date(year=2022, month=8, day=25)

per_day = 20
# days
total_days = rec_date - given_date
print(total_days.days)
print("Intrest:", total_days.days * per_day)

#  ------------------------
# Adding date + timedelta
today = date(year=2021, month=8, day=25)
future_date = date(year=2022, month=8, day=25)
# adding 90
# after 90 days what will year , month and day
out = today + timedelta(days=90)
print(out)

# ---------
# time: Hours, minutes, seconds, m sec
# Start time and end time
class_time = time(hour=6, minute=15, second=0)
print(class_time)
class_end_time = time(hour=7, minute=15, second=30)
print(class_end_time)

# Find the class duration in time
hour = class_end_time.hour - class_time.hour
minutes = class_end_time.minute - class_time.minute
sec  = class_end_time.second - class_time.second
time_diff = f"{hour}:{minutes}:{sec}"
print(time_diff)
# print(class_time + class_end_time) invalid on time object


# datetime
# use cases: last_login_datetime
# date + time
my_last_login = datetime(year=2021, month=8, day=24, hour=7, minute=30, second=45)
print(type(my_last_login))
print(my_last_login)
print(my_last_login.date())
print(my_last_login.time())

# today login
# after how many days i log in back
my_today_login = datetime(year=2021, month=8, day=25, hour=8, minute=40, second=45)

out = my_today_login - my_last_login
print(out)
# Adding delta

out = my_last_login + timedelta(weeks=1, hours=0, minutes=30)
print(out)



# Date formate
# dealing time zone


print("------------------------")
# How to get the current date and time in python?
today_date_time = datetime.now() # 24 hours # OS time zone
print(type(today_date_time))
print(today_date_time)

# print
print(f"Year: {today_date_time.year}")
print(f"Month: {today_date_time.month}")
print(f"Day: {today_date_time.day}")
print(f"Hour: {today_date_time.hour}")
print(f"Minute: {today_date_time.minute}")


# I want to get the landon today date and time
# Time zone
#from datetime import timezone
#----- pass

# how do we find the time zone
from datetime import timezone

print("-----------")
print("Date:", datetime.now().date())


# Month name march 10,

# date formats
"""

datetime format symbols
----------------------
%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - minute [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 59]
"""

print(today_date_time)
# format

# we formated the python datetime
# formating and converting python datetime to string
my_formated_date = today_date_time.strftime("%b-%Y-%d %H:%M:%S")
print(my_formated_date)


# parsing string datetime into python datetime
data_str = '2021-August-27 19:09'
# need to compare with other date?
other_date_str = "2021-08-26 19:09"
# which is older date?
date_1 = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
print(type(date_1))

date_2 = datetime.strptime(other_date_str, "%Y-%m-%d %H:%M")
print(type(date_2))


if date_1 > date_2:
    print("Date 1")
else:
    print('Date 2')



# Date related completed except timezone












































