#Tutorial point exercise

#1 We dont need to specifically declare the type of variable here.
print('1 -')
a = 100             # Integer type 
b= 100.01           # Floating type
c = 'Aditya'        # String type
print(a)
print(b)
print(c)



#2 There are 5 datatypes iin Pyhton - Number, string, list, tuple and dictionary

#2a- Numbers
#number contains four kind of data - Integer, Floating(decimal), Long(Long integer, octadecimal, hexa decimal), and Complex numbers.print('/
print('\n')
print('Numbers - 2 a -')
a = 100
b = 100.12
c = 162517257112189738998798789789102381038131839109823091830918309181231892371893189L
d = 3.13j
print(type(a))        #integer
print(type(b))        #float    
print(type(c))        #long(hexadecimal)       Issue -2
print(type(d))        #complex number




#2b Strings functions
print('\n')
print('string operators 2 b - ')
name = 'Modinagar'
print(name)
print(name[1])
print(name[1:3])
print(name[1:])
print(name*3)
print(name + ' Birth city of Aditya')


#2c Lists
print('\n')
print(' Lists in python  2 c -')
biglist = ['abcd', 123,100.01,12+10j]
print(biglist)
print(biglist[0])
print(biglist[-2])
print(biglist[1:2])
print(biglist[2:])
print(biglist * 3)
print(biglist + biglist)



#2d Tuples - tuples are exact similar to lists. the only differnce is they can not be modified later. Consider them as only readonly list
print('\n')
print('Tuples 2 d - ')
tuple1 = 'abcd',2,10.5,56j    #one way to define tuple
tuple2 = ('a1',3,4,5,6)       # another way to define tuple
print(tuple1)
print(tuple2)
print(tuple1[2])
print(tuple1[2:4])
print(tuple1[2:])
print(tuple1 * 4)
print(tuple1 + tuple2)
#tuple1[1] = 37j            #update not allowed in tuple
biglist[1] =37j             #update allowed in lists
print(biglist)



#2e Dictionary - Key value pair concept : Defined by {}
print('\n')
print('Dictionary 2 e - ')
dict1 = {1:'Aditya', 2:'kansal','BirthCity':'Modinagar','Workingcity':'Bangalore'}
print(dict1)
print(dict1[1])
print(dict1[2])
print(dict1['BirthCity'])
print(dict1['Workingcity'])
dict1['Workingcity'] = 'Noida'    #updates in dictionary
print(dict1)




#3 Arthimetic functions
print('\n')
print('Arithmetic function 3 - ')
a = 5
b= 2
print(a+ b)     #addition
print(b-a)     #substraction
print(a*b)     #Multiplication
print(a/b)     #division
print(a**b)     #Exponent
print(a%b)     #Modulo


c= a/b
print(type(c))    #Datatypes are defined based on assignment. In this case division, it always store value in float datatype irrespective of input values



#4 concatenation of string and numbers with casting
print('\n')
print('concatenation of string and numbers with casting 4 - ')
l= 15
b=20
area = l*b
print(area)
print('the area is %d' % area)       # works for integers
print('the area is %8d' % area)       # right justfied
print('the area is %08d' % area)        # right jutified with zeroes in left side
print('the area is %f' % area)      #works for Float types
print('the area is %.2f' % area)    #limit the number of places after decimal. By default, it comes till 6 places.



#5 Assignment operator
# c = c+a
# c +=a --> c = c + a 
# c -=a --> c = c - a
# c *=a --> c = c * a
# c /=a --> c = c / a 
# c **=a --> c = c ** a
# c %=a --> c = c % a 
# c //=a --> c = c // a 






















