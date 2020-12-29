df=data[["Votes","Aggregate rating","Rating color"]]

#let white Represent 1 and rating below 1.5
#let Red represent 2 and rating between 1.5 to 2.5
#let Orange represent 3 and rating between 2.5 to 3.5
#let Yellow represent 4 and rating between 3.5 to 4.0
#let Green represent 5 and rating between 4.0 to 4.5
#let Dark Green represent 6 and rating between above 4.5

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
plt.ylabel("No.of votes")
plt.title("No. of votes vs rating")
plt.show()

print("After seeing these graph we can see that as no. of votes increases ratings also increases")
print("For Rating Color equal to red i.e 1 we can see that maximum votes are less than 2000")
print("For Rating Color equal to Orange i.e 2 we can see that maximum votes are near about 2000")
print("For Rating Color equal to Yellow i.e 3 we can see that maximum votes are near about 4000")
print("And so on")