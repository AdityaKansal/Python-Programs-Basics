import datetime   # importing datetime class to use date functions

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

# converting dates to other formats
print('\n')
print('coverting date format ')
print(today.strftime('%d %b %y'))
print(today.strftime('today date is %d %b %y'))   #putting extra string under strftime function



# taking input date from user
print('\n')
print('date as input ')
userinput = input('enter your birthdate in mm/dd/yyyy format')
# now converting this date string to date format
birthdate = datetime.datetime.strptime(userinput,'%m/%d/%Y').date()    #strptime (converts string to date) and strftime(date to other date in otherformat)
print(birthdate)
age = today - birthdate
print(age)   #indays




#time
print('\n')
print('time ')
currenttime = datetime.datetime.now()
print(currenttime)
print(currenttime.hour)
print(currenttime.minute)
print(currenttime.second)
print(currenttime.strftime('%H:%m'))
