
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('f:/data/zomato.csv',skipinitialspace=True,encoding = "ISO-8859-1")

df=data[data['Country Code']==216]
d={}
df.dropna(inplace=True)
for i in df.values:
    for j in i[9].split(','):
        d[j.strip()]=d.get(j.strip(),0)+1
l=sorted(d.values())
l.reverse()
l1=[]
l2=[]
for i in range(10):
    for j in d:
        if d[j]==l[i]:
            print(j," : ",l[i])
            d[j]=-1
            l2.append(j)
            l1.append(l[i])
plt.pie(l1,labels=l2,autopct="%.2f%%")
plt.show()
