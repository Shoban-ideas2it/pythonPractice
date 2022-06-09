import sys

# intialize set
setVariable = set()
print(type(setVariable))

# Add a data to set
setVariable.add("1")
setVariable.add("str")
setVariable.add("[1,2]")
# setVariable.add([1,2])      List cannot be added to set bcoz list is non hashable

secondSet = {1,2,3,4}
print(secondSet)

setVariable.update(secondSet)

# print(setVariable.pop())

# setVariable.remove(1)

# setVariable.remove('1')

print(setVariable)


