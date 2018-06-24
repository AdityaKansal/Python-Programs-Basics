import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series in pandas-------------------------------------
# series are 1 D array in pandas. We use it in pd.Series format.
print('\n')
print('Series in Pandas')
print('\n')
s = pd.Series([1,2,3,4])
print(s)
print('')
s = pd.Series(np.arange(10))  
print(s)
s = pd.Series(np.arange(5),index = [100,101,102,103,104])    # changing index
print(s)
s = pd.Series({'a': 123,'b':456,'c': 345})    #when u pass on Dictionary, there is no index avaialble, until we pass it explicitly
print(s)
s = pd.Series({'a': 123,'b':456,'c': 345})    #when u pass on Dictionary, there is no index avaialble, until we pass it explicitly
print(s)
#s = pd.Series({'a': 123,'b':456,'c': 345},index =[101,102,103]) ---- indexing wont happen here, but we can change index and change the mapping.
data = {'a': 123,'b':456,'c': 345}
s = pd.Series(data,index= ['b','c','a'])
print(s)
#from scalar
s = pd.Series(5,index = [1,2,3,4,5])
print(s)
#retrieving data from series:
s1= pd.Series(np.arange(5),index = ['a','b','c','d','e'])
s2 = pd.Series(np.arange(5),index=[100,102,103,104,105])
print(s1[0])
print(s1[2])
print(s1['b'])
print(s1[['a','b','c']])
print('\n')
#print(s2[0])  --- this wont work if we change index to other numbers .
print(s2[[102,103]]) 

    
#data frame:
print('\n')
print('Data Frames')
print('\n')
#from a list input
print(' from a list input')
data = [1,2,3,4,'abc']
df = pd.DataFrame(data)
print(df)

#from a list of lists input
print('\n')
print('using list of lists')
data = [['aditya',10,'kansal'],['Robin',20,'Singh'],['Priyanshu',30,'Gupta']]
df = pd.DataFrame(data)
print(df)   # note the header of columns and rows. These are by default indexing

#giving the headers at columns
print('\n')
print('giving the headers at columns')
data = [['aditya',10,'kansal'],['Robin',20,'Singh'],['Priyanshu',30,'Gupta']]
df = pd.DataFrame(data,columns=['FirstName','Seq','Lastname'])
print(df) 

 
#giving the headers at rows-- USe index
print('\n')
print('giving the headers at columns')
data = [['aditya',10,'kansal'],['Robin',20,'Singh'],['Priyanshu',30,'Gupta']]
df = pd.DataFrame(data,index=[1001,1002,1003])
print(df) 
   
#changing/assigning datatype     
print('\n')
print('changing/assigning datatype ')
data = [['aditya',10,'kansal'],['Robin',20,'Singh'],['Priyanshu',30,'Gupta']]
df = pd.DataFrame(data,index=[1001,1002,1003],dtype=float)
print(df) 

#using Dicts-- we already did in Pandas 
#using list of dicts
print('\n')
print('using list of dicts ')
print('\n')
print('data1')
data1 = [{1:'a',2:'b', 3:'c'},{4:'d',5:'e',6:'f'},{7:'g',8:'h',9:'i'}]  # first kind of data
df = pd.DataFrame(data1)
print(df)
print('\n')
print('data2')
data2 = [{1:'a',2:'b', 3:'c'},{1:'d',2:'e',3:'f'},{1:'g',2:'h',3:'i'}]    # second kind of data
df = pd.DataFrame(data2)
print(df)
print('\n')
print('data3')
data3 = {1:['a','d','g'],2:['b','e','h'], 3:['c','f','i']}    # third kind of data
df = pd.DataFrame(data3)
print('\n')
print(df) 
print('\n')
print('data4')
data4 = {1:['a'],2:['b'], 3:['c']}     # fourth kind of data
df = pd.DataFrame(data4)
print('\n')
print(df) 
print('\n')
print('data4=5')
data4 = [{1:'a',2:'b', 3:'c'},{1:'d'},{1:'g',2:'h'}]     # fifth kind of data
df = pd.DataFrame(data4)
print('\n')
print(df) 

#giving indexes and columns
print('\n')
data1 = [{1:'a',2:'b', 3:'c'},{1:'d',2:'e',3:'f'},{1:'g',2:'h',3:'i'}]    
df = pd.DataFrame(data,index = [100,102,104],columns = ['header1','Header 2','header 3'])
print('\n')
print(df) 

#data is in form of dict of series
print('\n')
print('data is in form of dict of series')
data = {'a':pd.Series([101,102,103],index = [0,1,2]),'b':pd.Series([101,102,103],index = [0,1,2]),'c':pd.Series([101,102,103],index = [0,1,2])}
df = pd.DataFrame(data)
print(df)

#printting specific row or column
print('\n')
print('printting specific row or column')
print(df)
print('first row')
print(df[0:1])  #fiirst row
print('')
print('a column')
print(df['a'])   # header 'a' column


#column addition
print('\n')
print('Column addition')
print('')
data = {'a':[1,2,3],'b':[4,5,6]}
df = pd.DataFrame(data)
print(df)
df['c'] = pd.Series([1,2,3])
df['d'] = pd.Series(['abc','def',451])
print(df)
df1 = df['a'] + df['b']
print(df1)


#column deletion
print('\n')
print('column deletion')
print('')
data = {'a':[1,2,3,4,5],'b':[2,4,5,6,7],'c': [12,23,12,33,12] }
df= pd.DataFrame(data)
print(df)
del df['c']    #first method to delete any column
print(df)
df.pop('b')    #second method to delete any column
print(df)




#row addition and access to rows
print('\n')
print('row addition and access to rows')
print('')
data = [[1,2,3,4,5],[4,5,6,7,8],[1,3,4,5,6]]
df= pd.DataFrame(data,index=[100,101,102],columns = ['h1','h2','h3','h4','h5'])
print(df)
print('\n')
print(df.loc[101])    #this will call row using the new index name
print('\n')
print(df.iloc[1])   #eventhough index is changed -iloc will still call rows with an index number
 
#deleting  a row
#use drop
df = df.drop(102)
print(df)




#introduction to Panel- 3D
print('\n')
print('Panel 3D')
print('\n')
data = {'a': pd.DataFrame([1,2,3]),'b':pd.DataFrame([1,2,3])}
pn = pd.Panel(data)
#printing complete panel
print('printing complete panel')
print(pn)
print('\n')
#printing item
print('printing item')
print(pn['a'])
print('\n')
#printing major axis
print('printing major axis')
print(pn.major_xs(1))
print('\n')
#printing minor axis
print('printing minor axis')
print(pn.minor_xs(0))
print('\n')


#statitics using data frames
print('\n')
print('statitics using data frames')
print('')
data = {'Name': pd.Series(['a1','a2','a3','a4','a5','a6','a7','a8']), 'age':pd.Series([10,11,12,13,14,15,16,17]),'Marks':pd.Series([99,98,67,68,89,87,90,65])}
df = pd.DataFrame(data)
print(df)
print('\n')
print('sum------------')
print('sum is %s'%df.sum())
print('sum of marks is  %d' %df['Marks'].sum() )
print( df.sum(0) )  # axis = 0  column sum 
print(df.sum(1))   #axis = 1   row sum


#other functions
print('Mean of marks is %s' %df['Marks'].mean())
print('standard deviation of marks is %s' %df['Marks'].std())
#median,mode and other functions are also available.


#describe function
print(df.describe())


































































































































 































     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

