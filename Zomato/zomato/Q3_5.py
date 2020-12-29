import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('f:/data/zomato.csv',skipinitialspace=True,encoding = "ISO-8859-1")
india=data[data["Country Code"]==1]

count=india["City"].value_counts()
city_rating_votes=india.loc[:,("City","Aggregate rating","Votes")]

city_rating_votes["Aggregate rating"]=city_rating_votes["Aggregate rating"]*city_rating_votes["Votes"]



city_votes=city_rating_votes.groupby("City")["Votes"].agg("sum")#
city_rating=city_rating_votes.groupby("City")["Aggregate rating"].agg("sum")
city_rating_votes=pd.DataFrame(city_rating)
city_rating_votes["Votes"]=city_votes

city_rating_votes["Weighted Rating"]=city_rating_votes["Aggregate rating"]/city_rating_votes["Votes"]
city_weighted=city_rating_votes[["Weighted Rating"]]#.sort_values(ascending=False)

a=pd.DataFrame(city_weighted)
a["counts"]=count
print(a)
a
plt.figure(figsize=(15, 10), dpi=70)
plt.scatter(a.index,a.counts,s=a['Weighted Rating'] ,c='b',edgecolor='r')
plt.xlabel("City")

plt.ylabel("Number of Restaurant")
plt.xticks(rotation=60)
plt.show()