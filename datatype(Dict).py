#Dictionary is unordered, changable and indexed. It won't allow duplicates

#Init
Dict = {
         "brand" : "Ford",
        "model" : "Mustang",
        "Year" : 1998
        }
print(Dict)

#Access items
print(Dict["Year"])

print(Dict.get("brand"))

#change values
Dict["Year"] = 1964
print(Dict)

#Loop
for i in Dict:
        print(i)
        print(Dict[i])#to print values

for i in Dict.values():
        print(i)

for i,j in Dict.items():
        print(i,j)

#Check if key exists
if "brand" in Dict:
        print("Yes")

#length
print(len(Dict))

#Add items
Dict["color"] = "white"
print(Dict)

#Remove items
Dict.pop("model")
print(Dict)

Dict.popitem()#removes las indexed item (randomly in 3.7 version)
print(Dict)

del Dict["Year"]
print(Dict)

#clear() method will empties the dictionary

#Copy a dictionary
Dict1 = Dict.copy()
print(Dict1)

Dict2 = dict(Dict1)
print(Dict2)

#Nested Dictionaries >> in this a dictionary can contain many dictionaries

#Dict constructor
Dict3 = dict(brand = "Ford",model = "Mustang")
print(Dict3)