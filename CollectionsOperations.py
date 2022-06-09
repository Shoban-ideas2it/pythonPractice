import time

st = time.process_time()
# List

# Tuple

# Set

# Dictionary
testDict = {"pat":1}

# Add
testDict['tap'] = 2
testDict['atp'] = 2
testDict['tpa'] = 2
testDict['model'] = 2

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

testDict.update(thisdict)
print(testDict)
print(len(testDict))

print(testDict.get("pat"))

elapsed_time = time.time() - st
print('Execution time:', elapsed_time)

mylist = ["a","b","c"]
mydict = {}

for i in mylist:
    for j in mylist:
        for k in mylist:
            print(hash("".join([i,j,k])))
            mydict["".join([i,j,k])] = 1 
            

print(mydict)


list1 = [ 1, 2, 3, 4, 5, 6 ]
 
# Pops and removes the last
# element from the list
print(list1.pop(), list1)
 
# Pops and removes the 0th index
# element from the list
print(list1.pop(4), list1)



