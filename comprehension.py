# List

# mylist = [1,2,3,4]

# sqList = [x*x for x in mylist if x>1]

# print(sqList)

# # dictionary

# myDict = {2,3,4,5}
# sqDict = { y*y for y in myDict if y>2}
# print(sqDict)

# # Set

# mList = [1,2,4,4,4,5,5,5,5]
# mySet = set()

# mySet = { y for y in mList}
# print(mySet)

# # Generator

# # triple the data
# mylist = [1,2,4,56,7,8,9]

# myGen = sum(i for i in range(100))

# # for i in myGen:
# print(myGen)

# def square(number):
#     return number * number

# myMap = map(square,mList)
# myMap = list(myMap)
# print(myMap)



name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print(set(mapped))
    