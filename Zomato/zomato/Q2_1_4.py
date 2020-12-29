df=data[["Cuisines","Aggregate rating"]]
df.dropna(inplace=True)
d={}
d1={}
x_axis=[]
y_axis=[]
for i in df.values:
    for j in i[0].split(","):
        d[j.strip()]=d.get(j.strip(),0)+1
        d1[j.strip()]=d1.get(j.strip(),0)+i[1]

l=sorted(d.values())
l.reverse()
for i in l[:10]:
    for j in d:
        if d[j]==i:
            x_axis.append(j)
            y_axis.append(float(format(d1[j]/d[j],".2f")))
plt.bar(x_axis,y_axis,edgecolor="black")
plt.xticks(rotation=90)
plt.show()
print("from the bar grahp we can see that Italian ,Continental food are liked most")