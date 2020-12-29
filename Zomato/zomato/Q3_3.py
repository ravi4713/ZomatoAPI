import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('f:/data/zomato.csv',skipinitialspace=True,encoding = "ISO-8859-1")



df=data[["Restaurant Name",'Votes']]
df.sort_values("Votes",inplace=True,ascending=False)
l=[]
l1=[]
for i in df.head(10).values:
    l.append(i[0])
    l1.append(i[1])
    print(i[0]," : ",i[1])
plt.title("Bar Graph of Restaurants With maximum Votes")
plt.xlabel("Name of Restaurants")
plt.ylabel("No. of votes")
plt.bar(l,l1,edgecolor='black')
plt.xticks(rotation=90)
plt.show()