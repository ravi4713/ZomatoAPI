df=data[["Cuisines","Aggregate rating","Rating color"]]
df.dropna(inplace=True)
x=[1,2,3,4,5]
color=['Red', 'Orange', 'Yellow', 'Green', 'Dark Green']
x_axis=[]
y_axis=[]
d={}
d1={}
for i in df.values:
    if i[2] !="White":
        d[len(i[0].split(","))]=d.get(len(i[0].split(",")),0)+1
        d1[len(i[0].split(","))]=d1.get(len(i[0].split(",")),0)+i[1]
l1=np.array(list(d.values()))
l2=np.array(list(d1.values()))
a=l2/l1
y_axis=[float(format(i,".2f")) for i in a]
x_axis=list(d.keys())
plt.bar(x_axis,y_axis,edgecolor="Black")
plt.xlabel("no. of cusines served")
plt.ylabel("avg rating")
plt.title("no. of cusines served vs rating")

print("After seeing graph we can say that as no. of cuisines increases than rating also increases")