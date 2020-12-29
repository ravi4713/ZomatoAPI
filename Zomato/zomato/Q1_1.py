import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('f:/data/zomato.csv',skipinitialspace=True,encoding = "ISO-8859-1")
#as we know that country code of india is 1
df=data[data['Country Code']==1]
df.head()
df.City.unique()
NCR_cities=['New Delhi','Ghaziabad','Faridabad','Gurgaon',"Noida"]
def cities(city):
    y=0
    if city in NCR_cities:
        y=1
    else:
        y=0
    return y
df["ncr/rest_india"]=df['City'].apply(cities)
delhi_ncr=df["ncr/rest_india"].value_counts().iloc[0]
rest_india=df["ncr/rest_india"].value_counts().iloc[1]
print("restuarant in Delhi NCR :",delhi_ncr)
print("restuarant in rest of india :",rest_india)

plt.bar(["delhi_ncr",'rest_of_india'],[delhi_ncr,rest_india],width=0.1,align='center')
plt.show()