#Set is unordered and unindexed. It won't allow duplicate members

#initialization
Set = {"Benz","Ferrari","Jaguar","Ford"}
print(Set)

#Access items. Cannot access items because tuples are unordered. To access we use loop and in keyword
for i in Set:
    print(i)

#return True or False
print("Jaguar" in Set)

#Add items
Set.add("Bentley")
print(Set)

Set.update(["Ford","Lambo","Fortuner"])
print(Set)

#length
print(len(Set))

#Remove Item
Set.remove("Lambo")
Set.discard("Fortuner")

print(Set)

#can use pop to remove last index but not be sure which element will be deleted as it is unorderd. Clear() will empties the Set and del keyword will delete the Set

#Join two sets
Set1 = {"a","b","c"}
Set2 = {"p","q","r"}

Set3 = Set1.union(Set)
print(Set3)

Set2.update(Set)
print(Set2)

#Set constructor
Set4 = set(("test","test1"))
print(Set4)

#there are many other methods which can be used based on requirement