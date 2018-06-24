#if statement
print('only if')
firstname = 'Aditya'
if(firstname == 'Aditya') : print('firstname is matching')
lastname = 'kansal'
if(lastname == 'kansal') :  print('last name is matching')



#if-else
print('\n')
print('if-else statement')
a= 14
if(a== 12):
    print('if statement passed')
else :
    print('else statement is passed')



#if-elseif-else
print('\n')
print('if-elseif-else statement')
if(a== 12):
    print('if statement passed')
elif(a==13) :               # here else if is used as "elif"
    print('else if statement is passed')
else :
    print('else statement is passed')


#if inside if
print('\n')
print('if inside if statement')
b=2
if(a== 13):
    print('outer if statement passed')
    if(b == 1) :
        print('inner if is passed')
    else :
        print('inner else is passed')
else :               
    print('outer else statement is passed')
