#List is a collection which is ordered and changeable. It Allows duplicate members

#List initialization
List = ["apple","Bike","Car","banana","Pulsar","Jaguar"]
print(List)

#Accessing List items
print(List[2])

#Negative Index
print(List[-3:-1])

#Range
print(List[3:6])
print(List[5:])
print(List[:4])

#Change value
List[5] = "Benz"
print(List)

#loop
for i in List:
    print(i)

#Check item if exists
if "Benz" in List:
    print("Yes")

#length
print(len(List))

#Add items
List.append("Orange")
print(List)

List.insert(5,"FZ")
print(List)

#Remove Items

List.remove("Orange")
print(List)

#Removes last index item if index is not specified
List.pop()
print(List)

del List[5]
print(List)

#del keyword can completely delete the list and clear() method will empties the list

#Copy a list
List1 = List.copy()
print(List1)

#Another way to copy list
List2 = list(List)
print(List2)

#Join two lists

List3 = List1 + List2
print(List3)

List1.extend(List2)
print(List1)

#List constructor
List4 = list(("test","test1"))
print(List4)