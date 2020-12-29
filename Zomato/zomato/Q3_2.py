
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('f:/data/zomato.csv',skipinitialspace=True,encoding = "ISO-8859-1")


df=data["Aggregate rating"]
df.replace(0,np.nan,inplace=True)
df.dropna(inplace=True)
a=df.values
plt.title("Histogram of Aggregate Rating")
plt.xlabel("ratings")
plt.hist(a,edgecolor='black',bins=10)
plt.show()
