import numpy as np

# array function
a = np.array([(1,2,3),(4,5,6)])
print(a)


#defining Numpy range  
b= np.array([(1,2,3)])
print(b)



#rank method ---  Give rank of array-- n dimension
print(a.ndim)
print(b.ndim)


#shape of array --like (2,3) or (2,1)
print(a.shape)
print(b.shape)


# size of array -- calculates the total number of elements
print(a.size)
print(b.size)

#reshape -- interchange rows and columrs
a = a.reshape(3,2)
print(a)


#slicing in numpy
print('')
print('slicing  ')
c = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(c[0])   # first row
print(c[0,1])  # first row and second column
print(c[2,0])   #third row and 1st element
print(c[0:,2])  # all the rows and third element
print(c[0:2,1])  #all the rows from 0 till 2(not 2 index row) and the first index element



#linspace
print('')
print('linspace')
print(np.linspace(1,5,10))  # print 10 numbers between 1 and 5(including both) with equal spacing
print(np.linspace(33,35,80))



#min max and sum
print('')
print('min max and sum')
a = np.array([(1,2,3),(4,5,6)])
print(a.max())
print(a.min())
print(a.sum())
print(a.mean())
print(a.prod())
print('original')
print(a)
print('after transpose')
print(a.transpose())
print(a.sum(axis = 0))  # calculate sum of all the columns
print(a.sum(axis = 1))  # calculate sum of all the rows



# square root and standard deviation
print('')
print('square root and standard deviation')
print(np.sqrt(a))
print(np.std(a))


# arithmetic operations on matrices
print('')
print('Artithmetic operations on matrices  - ')
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])

print(a+b)   
print(a-b)
print(a*b)
print(a/b)


#concatenation of two arrays
print('')
print('concatenation of two arrays')
print(np.vstack((a,b)))     # vertical stack
print(np.hstack((a,b)))     # horizontal stack


#ravel function
print('')
print('ravel function ')
print(np.ravel(a))



#exponential and logarithmic functions
print('')
print('exponential and logarithmic functions   ')
print(np.exp(a))
print(np.log(a))
print(np.log10(a))
print(np.log2(a))


#zeroes and ones
print('')
print('zeroes and ones')
print(np.zeros((2,3)))
print(np.ones((3,2)))


#arange function  -- similar to range function in lists
print('')
print('arange function  ')
print(np.arange(5))
print(np.arange(1,5))
print(np.arange(1,10,2))


# loops with numpy arrays
print('')
print('loops in array')
a = np.array([(1,2,3),(4,5,6)])
for i in a:        # here i is row not each element
    print(i)

for i in a.flat:
    print(i)

c= list()
print(np.ravel(a))
for i in np.ravel(a):
    c.append(i)
print(c)


# reshaping a linear array
print('')
print('reshaping a linear array ')
print(np.arange(6).reshape(3,2))
print(np.arange(9).reshape(3,3))


#horizontal and vertical split
print('')
print('vertical and horizontal split ')
a = np.arange(9).reshape(3,3)
print(a)
print('vertical split')
print(np.vsplit(a,3))    # this doesnt mean vertical always.. it is the first dimension found and then split
print('horizontal split')
print(np.hsplit(a,3))



#indexing with boolean
print('')
print('indexing with boolean ')
a = np.arange(16).reshape(4,4)
print(a)
b = a >9
print(b)
print(a[b])  # this statement will return the values where index is true


#power of numpy arrays when indexed with boolean values
print('')
print('power of numpy arrays when indexed with boolean values')
a = np.arange(16).reshape(4,4)
print(a)

print('in the 2D array, replace values with zero if thety are greater than 9')
b = a > 9
a[b] = 0
print(a)


print('make squares of values if they are even')
a = np.arange(16).reshape(4,4)
b = a % 2 == 0
print(b)
a[b] = a[b]**2
print(a)


# hackerrank problems
print('')
print('hackerrank')
a = np.array([(1,2,3,4,5)])
b = np.flip(a,1)        # flip function-- reorder the elements along a given axis
print(b)



#print('')
#print('next challenge')
#def convert(a):
#
#    b =np.array(a,int)
#    return b.reshape(3,3)
#
#
#
#
#a = input().strip().split(' ')
#result = convert(a)
#print(result)
#
#
#
#
#import numpy
#
#def convert(a):
#
#    b =numpy.array(a,int)
#    return b.reshape(3,3)
#
#
#a = input('Enter').strip().split(' ')
#result = convert(a)
#print(result)



#additional functions
print('\n')
print('additional function')
print(np.identity(4))    #creates a identity matirx function
print(np.eye(3,4,k =0))    # similar to identity but rows and columns can be of different value. also we can move '1' diagonal row up or down with value of K
print(np.eye(3,4,k= 1))    # postive k will move the 1 diagonal row upside
print(np.eye(3,4,k =-2))   # negative k will move the 1 diagonal row down
print('to convert datatype of eye to an int')
print(np.eye(3,4,k=2,dtype = int))         #dtype is used to assign the datatype here .


#rounding off functions
print(np.floor(1.1))   # The floor of x is the largest integer where .i <= x    Run towards Floor-- down side
print(np.ceil(1.1))    # The ceiling of x  is the smallest integer where i>= x.  Run towards ceil-upside
print(np.rint(1.1))   # The rint tool rounds to the nearest integer of input element-wise   -- round off
print(np.rint(1.5))













