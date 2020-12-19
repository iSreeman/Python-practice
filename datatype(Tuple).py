#Tuples are ordered and unchangeable. Allows duplicate members

#Tuple Initialization
Tuple = ("Bike","car","Fruits","vegetables","Bike")
print(Tuple)

#Access tuple items
print(Tuple[3])

#Negative Indexing
print(Tuple[-2])

#Range
print(Tuple[0:3])

#Range of Negative Indexes
print(Tuple[-3:-1])

#Change Tuple Values. As tuples are unchangeable to change tuple values we can convert tuple into a list >> change values >> convert to tuple again
Convert = list(Tuple)
Convert[1] = "Cars"
Tuple = tuple(Convert)
print(Tuple)

#loop
for i in Tuple:
    print(i)

#check item
if "Fruits" in Tuple:
    print("Yes")

#length
print(len(Tuple))

#Cannot Add items

#tuple class
print(type(Tuple))

#Remove items
Tuple1 = ("Test","Test1")
del Tuple1
#print(Tuple1) #error because tuple has deleted successfully

#Join two tuples
Tuple2 = ("a","b","c")
Tuple3 = Tuple + Tuple2
print(Tuple3)

#Tuple constructor
Tuple4 = tuple(("p","q","r"))
print(Tuple4)

#other methods
print(Tuple.count("Bike")) #return the count of value
print(Tuple.index("Cars"))