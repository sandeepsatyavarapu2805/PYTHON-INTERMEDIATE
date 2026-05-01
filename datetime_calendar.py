import datetime, calendar
#import antigravity

today = datetime.date.today() # date
present  = datetime.datetime.today() # date and time

print( f"{today:%B %d, %Y}") # prints the date formatted
print( present) # prints the date formatted
print(present.weekday()) # prints the day number in the week starting with 0 as monday
print(present.isoweekday()) # prints the day number in the week starting with 1 as monday

print(calendar.isleap(today.year)) # prints if the year is leap or not : boolean type
print('\n')
print(calendar.month(today.year, today.month)) # prints a formatted calendar of that month
print(calendar.weekday(today.year, today.month, today.day)) # prints the INDEX of day mentioned, in the week