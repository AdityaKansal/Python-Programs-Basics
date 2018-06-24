import pandas as pd
import matplotlib.pyplot as plt 

#basic pandas program
print('')
print('Basic Pandas Program')
XYZ_Web = {'Days': [1,2,3,4,5,6,7], 'Visitors' : [100,200,300,400,500,600,700],'Bounces' : [10,10,30,40,50,60,70]}
df = pd.DataFrame(XYZ_Web)
print(df)
print(df.size)


#slicing data frame
print('')
print('Slicing a data frame')
print(df.head(2))    # will print first two rows
print('\n')
print(df.tail(2))    # will print last two rows
print('\n')
print(df[0:5:3])     # slicing rows in between     - Similar to list
print('\n')
print(df[df['Days'] == 1]   )      #slicing based on comparsion   
print(df[df['Visitors']== 200])
print('\n')
print(df['Days'])      # getting columns
print(df['Bounces'])
print('\n')
print(df['Days'][df['Bounces'] == 10][df['Visitors'] == 100])      # And condition in Pandas
print('\n')
sd = df[['Visitors']]     #slicing columns with the use of headers
print(sd)



#merging
print('\n')
print('Merging ')
df1 = pd.DataFrame({'Name': ['Aditya','Robin','Priyanshu'],'ID':[1,2,3],'Job': ['Eng','Doc','IAS'],'Salary':[10,15,20]},index= [2001,2002,2003])
df2 = pd.DataFrame({'Name': ['Kansal','Robin','Priyanshu'],'ID':[4,2,3],'Job': ['Eng','Doc','IAS']},index= [2004,2005,2006])
print(df1)
print('\n')
print(df2)
print('\n')
print(pd.merge(df1,df2))   #data loss -- merge operation basically finds out common things and then gives the common output
print('\n')
print(pd.merge(df1,df2, on = 'Job'))    #this on function will do merge based onnly on this header. rest all columns will be repated mentioning Xtable data and Y table data and so on.



#joining tqo data frames
print('\n')
print('Joining two data frames')
df1 = pd.DataFrame({'Name': ['Aditya','Robin','Priyanshu'],'ID':[1,2,3],'Job': ['Eng','Doc','IAS'],'Salary':[10,15,20]},index= [2001,2002,2003])
df2 = pd.DataFrame({'Name2': ['Kansal','Robin','Priyanshu'],'ID2':[4,2,3],'Job2': ['Eng','Doc','IAS']},index= [2003,2005,2006])
print(df1)
print('\n')
print(df2)
print('\n')
print(df1.join(df2))    # this join function will join two frames based on index.and it only adds columns to the right.It wont increase the number of rows
                        #so, if i join df1.join(df2), all the indexes of Df1 will be output with extra columns of df2. Df2 extra indexes will not come in output



#change index of data frame
print('\n')
print('changing index')
df = pd.DataFrame({'Day': [1,2,3,4,5],'Visitors' : [100,20,40,120,60], 'Bounces': [13,20,7,40,3]})
print(df)   # when we print this , the default index is 0,1,2,3,4,5
print('\n')
#lets change the index
df.set_index('Day',inplace = True)   # this statement has made Day as index
print(df)


#plot the graph of this data drame
print('\n')
df.plot()
plt.show()

#chanfing the name of column/header
print('\n')
df = df.rename(columns = {'Visitors' : 'Users'})    #This will change the header name
print(df)


#concatenation
print('\n')
print('Concatenation  ')
df1 = pd.DataFrame({'Name': ['A','B','C','D'], 'EMPID':[1,2,3,4]},index = [0,1,2,3])
df2 = pd.DataFrame({'email': ['A','B','C','D']},index = [0,1,2,4])

#df2 = pd.DataFrame({'Email': ['email1','email2','email3','email4'],'EMPID':[1,2,3,4]},index = [0,1,2,,3])
print('Using Join')
print(df1.join(df2))
print('')
print('using concat')
print(pd.concat([df1,df2]))  # concatenate is starightforward.. All left, right centre. and give NaN when data is not available



#data Munging
print('\n')
print('Data Munging')
#reading from csv file
Read1 = pd.read_csv('C:\\Users\\akansal2\\Desktop\\Test.csv',index_col=0)
Read1.to_html('test.html')


#reading excel and doing basic operations
print('\n')
print('Reading excel and doing basic operations ')
Excel_WB = pd.ExcelFile('C:\\Users\\akansal2\\Desktop\\test1.xlsx')
print(Excel_WB.sheet_names)  # reading sheet names
print('Total number of sheets in excel is %d'%len(Excel_WB.sheet_names))   #total number of sheets
sheet_1 = pd.read_excel('C:\\Users\\akansal2\\Desktop\\test1.xlsx',sheet_name = 0)
print(sheet_1)
sheet_1.to_html('Deli_DashBoard.html')
df = pd.DataFrame(sheet_1)
#plt.bar(df['Department'],df['Number of defects'])
#plt.show()



# Plotting a graph for population change for differnet countries
print('\n')
print('Population change Graph')
df = pd.read_excel('C:\\Users\\akansal2\\Desktop\\test1.xlsx',sheet_name = 1,index_col = 0)     #here 'DataSheet' data type is panda data frame
print(df)
df.plot()
plt.show()
print('\n')
print(df)
df = df.set_index(['Country Code'])
#print(df)
#df.plot()
#sd = df.reindex(columns = ['2012','2013'])

db = df.diff(axis = 1)

print(db)
db.plot()
plt.show()
















