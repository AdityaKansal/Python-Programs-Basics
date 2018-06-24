import random

# to get a list with even numbers only
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#first way using loop
b= []
for i in a:
    if i%2==0 :
        b.append(i)

print(b)



#using Lambda function
b.clear()
c = lambda x :True if x%2== 0 else False
 
for i in a :
     if c(i):
         b.append(i)
print(b)



#using list commprehension
b.clear()
b=[i for i in a if i%2==0 ]
print(b)


#numbers less than 50
b.clear()
b= [i for i in a if i<50]
print(b)


#list of divisors
inputnumber = 1135
i= inputnumber
while i >1:
    #print(i)
    if inputnumber%i ==0:
        print(i)


    i-=1


#list overlap
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 89, 13]

# a list that contains common values among these
c=[]

#for loop
for i in a:
    for j in b:
        if i == j :
            c.append(i)

c= list(set(c))
print(c)
  
d = []
e = []
counter = 10
while counter >0:
    d.append(random.randint(0,100))
    counter -=1
print(d)




#String to check whether it is palinrome or not
str1 = 'ATA'
str1 = str1.lower()
str2 = str1[::-1]
if str1 == str2 :
    print('palindrome')
else:
    print('Non -palindrome')



#Guess Game

counter = 0
def gamelogic():
    userinput = input('Enter your number between 1-9 - ')
    
    randomnumber =  random.randint(1,9)
    print(randomnumber)
    difference = abs(int(userinput) - randomnumber)
    #print(difference)
    if difference == 0 :
        print('Exact match')
    elif 0< difference < 4:
        print('Guess too high')    
    elif  3 < difference < 10:
        print('Guess too low')
    
    restartgame = input('To restart game , press yes otherwise no')
    return restartgame
counter = 0
#startgame = input('Input yes to start the game otherwise no')    
startgame = 'no'
while startgame == 'yes':
    counter += 1
    startgame = gamelogic()
else:
    print('You have guessed %d times. Thanks for playing' % counter)
                              


# list comprehensive to find common parameters between two lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d = random.sample(range(1,30),12)     # creating list with random sample function
c = [i for i in set(a) if i in set(c)]
print(d)
print(c)





#prime numbers
def primenumber(a):
    #prime number logic
    i = a-1
    while i >1:
        if a%i == 0:
            return True
        i-=1
    else:
        return False

number = input('enter number to prime number check')
check = primenumber(int(number))
if check == True:
    print('Not prime number')
else:
    print('Prime')





































        
