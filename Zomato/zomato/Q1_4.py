print('from the given data set we can see that maximum no. of restaurant are present at delhi ncr i.e 7947 retaurants and rest are from differents parts.we can plot pie chat between them to show percentage of restaurant presents in different parts')
plt.pie([7947,705],labels=["DELHI NCR",'REST OF INDIA'],autopct="%.2f%%")
plt.title("Pie chart for total number of restaurants")
plt.show()

print("In Indian different variety of cuisines are made In delhi ncr we have 86 different variety of cuisines")
print("we can say that we can find all type of cuisines in delhi ncr which are present in india ,but due to incomplete data set we get 4 cuisines which are not present in delhi")
print("famaous cuisines in india are : ")
for i in cuisine:
    print(i,end=',')