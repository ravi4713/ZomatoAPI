
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('f:/data/zomato.csv',skipinitialspace=True,encoding = "ISO-8859-1")



df=data[["Restaurant Name"]]
l=[]
l1=[]
for i in df["Restaurant Name"].value_counts().head(15).index:
    l.append(i)
for i in df["Restaurant Name"].value_counts().head(15).values:
    l1.append(i)
plt.bar(l,l1,edgecolor="black")
plt.xticks(rotation=90)
plt.title("Restaurants with maximum outlets")
plt.xlabel("Restaurants name")
plt.ylabel("No. of Outlets")
plt.show()