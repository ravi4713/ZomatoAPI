import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('f:/data/zomato.csv',skipinitialspace=True,encoding = "ISO-8859-1")
#as we know that country code of india is 1
df=data[data['Country Code']==1]
df=df[['Cuisines','ncr/rest_india']]
df.dropna(inplace=True)
Cuisines_rest=[]
Cuisines_ncr=[]
for i in df.values:
    if i[1]==0:
        for j in i[0].split(','):
            if j.strip() not in Cuisines_rest:
                Cuisines_rest.append(j.strip())
    else:
        for j in i[0].split(','):
            if j.strip() not in Cuisines_ncr:
                Cuisines_ncr.append(j.strip())
print("total number of Cuisines in Delhi NCR : ",len(Cuisines_ncr))
print("total number of Cuisines in Rest od India : ",len(Cuisines_rest))
print()
diff_Cuisines=[]
for i in Cuisines_rest:
    if i not in Cuisines_ncr:
        diff_Cuisines.append(i)
print("List of Cusines not served in Delhi NcR :")
for i in diff_Cuisines:
    print(i,end=',')
print()
print()
print("As we can see BBQ is present in these list of cuisine which are not served in delhi But Cuisine of BBQ is present in delhi,we can verify it through zomato apis")
print("Name of restaurant : ","Barbeque Nation")
print("Aderess : ","2nd Floor, Munshilal Building, Block N, Outer Circle, Connaught Place, New Delhi")
print("So we can say that BBQ cuisine is served in Delhi NCR but data Set was incomplete")