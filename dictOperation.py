import sys

# intialize
tempDict = {}
print("Size of empty dictionary: ",sys.getsizeof(tempDict))

for i in range(1,100):
    tempDict[i] = i
    print(i , "Size of dictionary: ",sys.getsizeof(tempDict))
    # print(tempDict)

# Copy of the same 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
tempDict = thisdict.copy()
print(tempDict)

print(id(tempDict))
print(id(thisdict))

# Dict
dictName = {}
print(type(dictName))
print(sys.getsizeof(dictName))

dictName['furit'] = 'Orange'
dictName['Veg'] = 'Tomatto'

dictSize = {"hi":"7889", "ui":"24242","io":"o909", "rtretret":"etrtretet","hi1":"7889", "ui1":"24242" }
print(dictSize.pop("hi"))
print(dictSize.popitem())
dictSize.clear()

print(dictSize)

# print(dictSize[0])
print(hash(1))
print(sys.getsizeof(dictSize))
