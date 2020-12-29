df=data[["Average Cost for two","Aggregate rating","Rating color"]]
df.dropna(inplace=True)
x=[1,2,3,4,5]
color=['Red', 'Orange', 'Yellow', 'Green', 'Dark Green']
x_axis=[]
y_axis=[]
for i in df.values:
    if i[2] !="White":
        x_axis.append(x[color.index(i[2])])
        y_axis.append(i[0])
plt.scatter(x_axis,y_axis)
plt.xlabel("Ratings number")
plt.ylabel("No.of Avg. Cost")
plt.title("No. of Avg Cost  vs rating")
plt.show()