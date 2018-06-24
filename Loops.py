# while loop
print('while loop')

count =10
while(count > 0):
    print(count)
    count -= 1

print('while loop ended')  #In Python, all the statements indented by the same number of character spaces after a programming construct are considered to be part of a single block of code.




#while loop with else
print('\n')
print('While loop along with else')
counter1 = 10
while(counter1 > 0):
    print(counter1)
    counter1 -= 1
else :
    print("loop ended")



#Range Fucntion in Python
print('\n')
print('Range function demo ')
print(range(5))         #0,1,2,3,4
print(range(10))        #0,1,2,3,4,5,6,7,8,9
print(range(1,10))      #1,2,3,4,5,6,7,8,9
print(range(3,10))      #3,4,5,6,7,8,9
print(range(1,10,2))    # 2,4,6,8
print(range(2,35,3))   # 3,6,9,12--- till 33




#for loop
print('\n')
print('For loop ')
for i in range(2,55,4):
    print(i)
for i in 'Aditya Kansal':
    print(i)


# for loop to find all the prime numbers within a range
print('\n')
print('Prime Numbers within a range using for loop ')
count = 0
for i in range(2,100):
    for j in range(2,i+1):
        if(i%j == 0):
            count +=1

    if(count < 2):
        print('%d is a prime number' % i)
    count =0
    

# break and continue is same as earlier.
# break will skip the loop
# continue will leave that iteration and go to the validaion part for next iteration
# pass
# pass is like a null in loops : like do nothing.

for i in range(3):
    if(i==1):
        pass
        print('pass is simply skipped')
    print(i)
    

 












