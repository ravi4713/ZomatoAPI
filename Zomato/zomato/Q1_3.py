import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('f:/data/zomato.csv',skipinitialspace=True,encoding = "ISO-8859-1")
#as we know that country code of india is 1
df=data[data['Country Code']==1]

d_ncr={}
d_rest={}
all_={}
for i in df.values:
    if i[1]==0:
        for j in i[0].split(','):
            d_rest[j.strip()]=d_rest.get(j.strip(),0)+1
            all_[j.strip()]=all_.get(j.strip(),0)+1
    else:
        for j in i[0].split(','):
            d_ncr[j.strip()]=d_ncr.get(j.strip(),0)+1
            all_[j.strip()]=all_.get(j.strip(),0)+1

l=sorted(d_ncr.values())
l.reverse()
values=[]
cuisine=[]
for i in range(10):
    values.append(l[i])
    for j in d_ncr:
        if d_ncr[j]==l[i]:
            cuisine.append(j)
print("IN DELHI NCR")
for i in range(10):
    print(cuisine[i],values[i])
plt.bar(cuisine,values,edgecolor="black")
plt.title("Top 10 Cuisines served my maximun restaurant in delhi")
plt.xlabel("Top-Cuisines")
plt.ylabel("No. of restaurant served ")
plt.xticks(rotation=30)
plt.show()


l=sorted(d_rest.values())
l.reverse()
values=[]
cuisine=[]
for i in range(10):
    values.append(l[i])
    for j in d_rest:
        if d_rest[j]==l[i]:
            cuisine.append(j)
print("IN REST OF INDIA")
for i in range(10):    
    print(cuisine[i],values[i])

plt.bar(cuisine,values,edgecolor="black")
plt.title("Top 10 Cuisines served my maximun restaurant in Rest of India")
plt.xlabel("Top-Cuisines")
plt.ylabel("No. of restaurant served ")
plt.xticks(rotation=30)
plt.show()

l=sorted(all_.values())
l.reverse()
values=[]
cuisine=[]
for i in range(10):
    values.append(l[i])
    for j in all_:
        if all_[j]==l[i]:
            cuisine.append(j)
print("IN INDIA")
for i in range(10):
    print(cuisine[i],values[i])

plt.bar(cuisine,values,edgecolor="black")
plt.title("Top 10 Cuisines served my maximun restaurant in India")
plt.xlabel("Top-Cuisines")
plt.ylabel("No. of restaurant served ")
plt.xticks(rotation=30)
plt.show()