import scipy.integrate
import numpy as np

# integration method
print('integration of x2')
ans, err = scipy.integrate.quad(lambda x : x**2,0,4)
print(ans)

#numpy interaction
print('')
print('numpy commands ')
#a = np.concatenate(([3],[0]*5,np.arange(-1, 1.002, 2/9.0)))
#shortcut to do this
#a = np.r_[3,[0]*5,np.arange(-1, 1.002, 2/9.0)]
a = np.r_[3,[0]*5,-1:1:10j]
print(a)


# np.mgrid
print('')
print('mgrid function ')
a = np.mgrid[0:10:2]     #little different from Linspace. It creates an aray between 0 an 10 with an space of 2 withe qual spacing
print(a)
print('')
print(np.mgrid[0:2,0:3])  #doubtful


#test code
print('')
print('test code')

#a = np.array(input().strip().split(' '))
#length = np.size(a)
#i = a[0]
#while i < length:
        
#print(np.zeros((1,2),int))
#print(np.ones((1,2),int))





# Learn Python Numpy
print('')
print ('Demo  ')
#a = np.array([1,2,3,4,5])
#a = np.arange(9).reshape(3,3)
#b = np.arange(9).reshape(3,3)
#a = np.array(([1,2,3],[4,5,6]))
#print(type(a))
#a = np.zeros((2,3))
#a = np.ones((3,3),str))
#a = np.array(([1,2,3],[4,5,6]))
#b = np.array(([7,8,9],[10,11,12]))
#print(np.vstack((a,b)))
#print(np.hstack((a,b)))

a = np.array(([1,2,3],[4,5,6]))
b = np.array(([1,2,3],[4,5,6]))

print(a.ravel())














