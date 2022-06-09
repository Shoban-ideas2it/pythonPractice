# Tuple Operations
testTuple = ()
print(testTuple.__sizeof__())

testTuple1 = (1,2)
print(testTuple1.__sizeof__())

# Join
testTuple4 = testTuple + testTuple1
print(testTuple4.__sizeof__())

# Duplicate Values
testTuple2 = (1,1,2,3,4,4)
print(testTuple2)

print(testTuple2.__sizeof__())

# Different Datatypes
testTuple5 = (1,"arr",2.5,True,[1,2])
print(testTuple5)

print(testTuple5.__sizeof__())
print(len(testTuple5))

# Max
print(max(testTuple2))

# Min
print(min(testTuple2))
