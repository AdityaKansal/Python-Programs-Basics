import pandas as pd

#basic pandas application
web_xyz = {'Day':[1,2,3,4,5,6,7],'Visitors':[100,200,300,400,500,600,700], 'Bounce_rate': [10,20,30,40,50,60,70]}
df = pd.dataframe(web_xyz)

print(df)
