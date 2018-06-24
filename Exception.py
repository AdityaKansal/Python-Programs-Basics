import datetime
currentdate = datetime.date.today()
birthdate = input('enter yout birth date')
try:
    birthdate = datetime.datetime.strftime(birthdate,'%Y-%m-%d').date()
    print(currentdate)

    age= currentdate- birthdate
    print(age)
except Exception as e:
    print('invalid date format')
