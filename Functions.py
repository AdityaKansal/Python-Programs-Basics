from functools import reduce
import random
import turtle

#sum function
def sum(a,b):
    print(a+b)
    return


# Sum function with returning vlues
def ReturnSum(a,b):
    return a+b

#calling functions
sum(10,20)
print(ReturnSum(20,30))



#Lambda function--  one line function
print('\n')
print('lambda function')
square = lambda x: x**2
print(square(12))



#map function-- It is used to apply chnages to all elements in the list
print('\n')
print('map function')
list1 = [1,2,3,4,5]
list2 = list(map(square,list1))
print(list2)


#filter function- to select data from a list based on condition
print('\n')
print('filter function')
list3 = list(filter(lambda x: x<22,list1))
print(list3)




#reduce function- it will only give one output instead of a list
print('\n')
print('reduce function')
#multiplication of all the list members
result = 0
result = reduce(lambda x,y:x*y,list3)
print('the multiplcation of all the list members is %d' %result)




#dir() function- to list all the functions in sorted way under a module
print('\n')
print('dir function')
content = dir(random)
print('random functions ')
print(content)
print('turtle functions ')
print(dir(turtle))
