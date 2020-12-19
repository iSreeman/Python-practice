#we already tried for loop for sets, tuples, dict, lists

#loop through a string
str = "sreeman"
for i in str:
    print(i)

#break statement
fruits = ["apple","kiwi","banana","watermelon"]
for i in fruits:
    print(i)
    if i == "kiwi":
        break

#continue statement
for j in fruits:
    if j == "banana":
        continue
    print(j)

#range function >> to loop through a set of code a specified no of times we use range function (def:0 end:5-1 in below example)

for i in range(5):
    print(i)

print()

for i in range(2,5):
    print(i)

print()

for i in range(0,10,2):
    print(i)

print()

#Nested loops
colors = ["red","green","white"]

for i in colors:
    for j in fruits:
        print(i,j)

#pass statement
for i in range(0,4,1):
    pass