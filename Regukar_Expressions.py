import re

#search operation
if re.search('Aditya Kansal','Aditya Kansal lives in Modinagar') :
    print('String found')

else:
    print('string not found')



#Find all strings

allstring = re.findall('Aditya','Aditya lives in Modinagar and Aditya works in UHG')

for i in allstring:
    print(i)



# finditer - returns start and end point of the string
str1 = 'Aditya lives in Modinagar and Aditya works in UHG'

list1 = re.finditer('Aditya',str1)
for i in list1:
    print(i)
    print(i.span())


#finding string
str2 ='Sat,mat,pat,zat'
result = re.findall('[mspz]at',str2)        #exact match
for i in result:
    print(i)

result1 = re.findall('[c-q]at',str2)        # range match
for i in result1:
    print(i)


result3 = re.findall('[^c-q]at',str2)       # outide range match
for i in result3:
    print(i)


# Replace string
str3 = 'rat cat mat pat'
#will replace rat with mouse
replaceword = re.compile('rat')
str3 = replaceword.sub('mouse',str3)

print(str3)


#matching a single character

str4='12345678'
print(len(re.findall('\d',str4)))
print(len(re.findall('\d{5}',str4)))






