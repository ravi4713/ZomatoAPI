df=data
df=df[["Locality",'Aggregate rating','Votes']]
df.dropna(inplace=True)
df1=df.groupby('Locality')
localities={}
for i ,j in df1:
    t_votes=j['Votes'].sum()
    a=0
    if t_votes>0:
        for k in j.values:
            a+=int(int(k[2]))*float(k[1])
        localities[i]=format((a)/t_votes,".5f")
l=sorted(localities.values())
l.reverse()
for i in range(10):
    for j in localities:
        if localities[j]==l[i]:
            print(j," : ",l[i])
            localities[j]=-1
            break
print()
print("Only for INDIA")
print()
df=data[data["Country Code"]==1]
df=df[["Locality",'Aggregate rating','Votes']]
df.dropna(inplace=True)
df1=df.groupby('Locality')
localities={}
for i ,j in df1:
    t_votes=j['Votes'].sum()
    a=0
    if t_votes>0:
        for k in j.values:
            a+=int(int(k[2]))*float(k[1])
        localities[i]=format((a)/t_votes,".5f")
l=sorted(localities.values())
l.reverse()
for i in range(10):
    for j in localities:
        if localities[j]==l[i]:
            print(j," : ",l[i])
            localities[j]=-1
            break
            
