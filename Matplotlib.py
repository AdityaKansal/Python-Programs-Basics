from matplotlib import pyplot as plt
import numpy as np



#basic pyplot
print('')
print('basic pyplot')
plt.plot([1,2,3],[4,5,1])
plt.show()

#a simple plot with labels and variables as input
print('')
print('simple plot with labels and variables as input')
x = [1,2,3]
y = [4,50,10]
plt.plot(x,y)
plt.title('ABC')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()


#plotting two graphs with little formatting
print('')
print('plotting two graphs with little formatting')
x1= [1,2,3]
y1= [4,5,1]
x2=[2,3,4]
y2 =[6,7,2]

plt.plot(x1,y1,'g',label = 'line1', linewidth =5)
plt.plot(x2,y2,'c', label = 'line2', linewidth = 5)

plt.title('Compare')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.legend()
plt.grid(True,color= 'y')
plt.show()


#plotting a bar graph
print('')
print('plotting a bar graph')

x1 = [1,2,3,4,5]
y1 = [10,20,30,40,50]
x2 = [1.5,2.5,3.5,4.5,6.6]
y2 = [23,12,1,34,56]

plt.bar(x1,y1,label = 'Data1',color = 'g')
plt.bar(x2,y2,label ='Data2',color = 'b')
plt.legend()

plt.title('Bar Graph')
plt.xlabel('Day')
plt.ylabel('Quantity')
plt.show()


#Designing a histogram
print('')
print('Desgnging a histogram')
population = [1,2,3,4,5,6,10,12,13,20,45,30,40,50,60]   #random date
bins = [5,10,15,20,25,30,35,40,50,55,60,65]    #equal intervals
plt.hist(population,bins,histtype= 'bar',rwidth = 0.8)
plt.title('Hisogram')
plt.ylabel('population')
plt.xlabel('bins')
plt.show()



#scatter plot
print('')
print('Scatter plot')
x1 =[1,2,3,1,5,6,1]
y1 = [1,2,13,4,7,6,10]
plt.scatter(x1,y1,label = 'Scatter',color= 'g',marker = 'x')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Scatter plot')
plt.legend()
plt.show()




#area graph
print('')
print('Area graph')
Days = [1,2,3,4,]
Sleeping = [1,2,3,4]
Bathing=[5,6,7,8]
Eating = [1,3,8,4]
Exercising = [4,5,9,3]

plt.plot([],[],color ='g', label = 'Sleeping',linewidth = 5)  #this line is just to create legend for the map
plt.plot([],[],color = 'm',label = 'Bathing',linewidth =5 )  #this line is just to create legend for the map
plt.plot([],[],color = 'b',label = 'Eating',linewidth = 5)   #this line is just to create legend for the map
plt.plot([],[],color ='y',label ='Excercising',linewidth = 5)    #this line is just to create legend for the map

plt.stackplot(Days,Sleeping,Bathing,Eating, Exercising,colors =['g','m','b','y'])     #this line of code is mainly to plot the area graph
#plt.stackplot(Days,Bathing,color = 'm')    #if we give it individually for all activities, it will shadow the other data and will not be able to distinguish between them

plt.title('Area Graph')
plt.xlabel('Activities')
plt.ylabel('Data')
plt.legend()
plt.show()





#Pie Chart
print('')
print('Pie Chart ')
slices = [7,2,2,13]
activities = ['Sleeping','Bathing','Eating','Exercising']
cols = ['c','m','y','b']
#plt.pie([1,2,3,4],labels =['Sleeping','Bathing','Eating','Exercising'],colors = ['c','m','y','b'],startangle=90,shadow = True,autopct= '%1.1f'
plt.pie(slices,labels = activities,colors = cols,explode = (0,0.2,0,0),autopct='%1.1f',startangle = 90,shadow=True)
plt.title('Daily Routine',fontweight = 'bold',fontsize = 20,fontname = 'Segoe Print')
plt.show()




#multiple plots
print('')
print('Multiple Plots ')
f = lambda x : x**2    # defining lambda function to plot graph of x2 vs x
g = lambda x : x**3
x1 = np.arange(-10,10,1)

plt.subplot(2,1,1)      # the three arguements inside subplots are for: Number of subplots, number of plots horixontally, Seq number of plot
plt.plot(x1,f(x1),color = 'g',linewidth = 3)
plt.title('Square',fontweight = 'bold')

plt.subplots_adjust(hspace = 1,wspace =1)

plt.subplot(2,1,2)
plt.plot(x1,g(x1),color = 'b',linewidth = 3)
plt.title('Cubicle',fontweight = 'bold')
plt.show()







