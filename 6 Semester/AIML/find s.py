import csv
a = []
with open('enjoysport.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
# print(a)
print("\nThe total number of training instances are: ", len(a))

num_attribute = len(a[0]) - 1

hypothesis = ['0'] * num_attribute
print("\nThe initial hypothesis is: ", hypothesis)

for i in range(len(a)):
    if a[i][num_attribute] == 'yes':
        print("\nInstance", i + 1, "is", a[i], "and is a Positive Instance")
        for j in range(num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print("The hypothesis for the training instance", i + 1, "is: ", hypothesis, "\n")
    else:
        print("\nInstance", i + 1, "is", a[i], "and is a Negative Instance Hence Ignored")
        print("The hypothesis for the training instance", i + 1, "is: ", hypothesis, "\n")

print("\nThe Maximally specific hypothesis for the training instance is: ", hypothesis)
