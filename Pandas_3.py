import pandas as pd
import numpy as np

#defining data frame for operation
print('Sample Data frame')
data = np.arange(9).reshape(3,3)
df = pd.DataFrame(data,columns= ('a','b','c'))
print(df)
print('\n')


#table wise operation - pipe()     --  This pipe function is used to perform a common operation on all the elements of data frame
print('table wise operation')

#defining two sample function
def adder(arg1,arg2):              # arg1 would be the each element in data frame while arg2 is coming from pipe function
    return arg1 + arg2

def sub(arg1,arg2):
    return  arg1 -arg2

print('calling sum functon ')
print('')
print(df.pipe(adder,2))

print('\n')
print('calling dif functon ')
print('')
print(df.pipe(sub,2))


print('\n')
#row wise or column wise operation - apply()  -- This function will consider each row or column as an array and perfomr the operation
print('row wise or column wise operation - apply()')
print('default operation will be column wise')
print(df.apply(np.average)) 
print('')
print('changing the operation row wise ')
print(df.apply(np.average,axis = 1))

print('\n')
#element wise operation - applymap function -- this will perfomr the operation on individual element
print('apply map function')
print(df.applymap(lambda x: x**2))   #this apply map function will take only one input and gives one output only


# performing same square function using pipe function
print('')
print('printing squares using pipe function')
def square(arg1):
    return arg1*arg1
print(df.pipe(square))

print('\n')
# re-indexing of data frames
print('reindexing of data frame')
print(df)
print(df.reindex(index = [2,0,1]))
print(df.reindex(columns =['b','a','c']))
print(df.reindex(index = [2,1,0],columns =['c','a','b']))
print('')
print('rename function ')
print(df.rename(columns = {'a':'a1'},index = {1:4}))          #rename function


print('\n')
print('numpy random function ')
print(np.random.rand(3,3))    #random function to generate arrays- firsr arguement is number of rows , second arguement is number of columns

print('\n')
print('sorting a data frame')   #sort of data frame
print('original data frame')
df = df.reindex(index = [1,0,2],columns = ['b','a','c'])
print(df)

print('')
print('sorted using index')
print(df.sort_index())  #index sort

print('')
print('sorted using index in descending order')
print(df.sort_index(ascending = False))  #sorted using index in descending order

print('')
print('sorting the columns using axis')    
print(df.sort_index(axis = 1))      #sorting the columns using axis


print('')
print('Sorting particular columns or by values')
print(df.sort_values(by = 'c', ascending = False))    # all other values will be adjusted accordingly

print('')
print('Sorting particular rows or by index')
print(df.sort_index(1))    # all other values will be adjusted accordingly


print('\n')
#slicing of data frames
print('slicing of data frame using loc,iloc and ix')
#.loc() 	Label based
#.iloc() 	Integer based
#.ix() 	Both Label and Integer based  --- Ix is DEPRECATED
print('orginal data frame')
print(df)
print('')
print("df.loc[1:1,'a']--  Output ")
print(df.loc[1:1,'a'])
print('')
print("df.iloc[:1,:1]  --  Output ")
print(df.iloc[:1,:1])


print('\n')
print('Missing values ')
print('')
data = np.arange(16).reshape(4,4)
df = pd.DataFrame(data,index = [0,1,4,5],columns =['a','b','e','f'])
df = df.reindex(index = [0,1,2,3,4,5,6],columns = ['a','b','c','d','e','f'])
print(df)

print('')
print('is null')
print(df.isnull())

print('')
print('not null')
print(df.notnull())

print('')
print('performng arthmetic operation with NAN values')
print(df['b'].sum())
print(df.loc[4].sum())

print('')
print('orginal dataframe')
print(df)

print('')
print('Filling values in place of NaN')
print('Filling zeroes')
df1 = df.fillna(0)
print(df1)

print('')
print('Forward fill')
df1 = df.fillna(method = 'pad')   #values will be filled in place of Nan via column. value will move from up to down and fill downwards
print(df1)

print('')
print('Backward fill')
df1 = df.fillna(method = 'backfill')  #values will be filled in place of Nan via column. value will move from down to up and fill upwards
print(df1)


print('')
print('Backward fill with limit')
df1 = df.fillna(method = 'backfill', limit = 1)  #only one row upwards will be filled.
print(df1)

print('')
print('Deleting nulls')
df1 = df.fillna(method = 'backfill', limit = 1) 
df1.pop('c')
df1.pop('d')
print('orginal data frame')
print(df1)
print('')
print('After NaN deletion -- Row wise')
print(df1.dropna(axis =0))
print('')
print('After NaN deletion -- Column wise')
print(df1.dropna(axis =1))








































