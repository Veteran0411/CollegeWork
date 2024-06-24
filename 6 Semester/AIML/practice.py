import csv
a=[]
with open("enjoysport.csv","r") as file:
    for row in csv.reader(file):
        a.append(row)
        
print("total number of training instances",len(a))

num_attribute=len(a[0])-1

hypothesis=["0"]*num_attribute

for i in range(len(a)):
    if a[i][num_attribute]=="yes":
        print("\nInstance", i + 1, "is", a[i], "and is a Positive Instance")
        for j in range(num_attribute):
            if hypothesis[j]=="0" or hypothesis[j]==a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print("updated hypothesis",hypothesis)
    else:
        print("\nInstance", i + 1, "is", a[i], "and is a Negative Instance Hence Ignored")
        
print("\nThe Maximally specific hypothesis for the training instance is: ", hypothesis)
