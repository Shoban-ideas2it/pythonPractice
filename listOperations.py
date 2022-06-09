# list of strings -- 50 strings
# count of dupicate strings
# second highest duplicate string
# No Built-in functions only List

data = input("Enter a sentence/para to find the duplicate strings :")
duplicate_data = data.split( )
duplicate_count = []

# Removes the Duplicate string from the List or set(List)
unique_data = []
for i in duplicate_data:
    if i not in unique_data:
        unique_data.append(i)

# Get the count of the duplicate strings
for i in unique_data:   
    count = 0
    for j in duplicate_data:
        if i == j:
            count = count + 1
    duplicate_count.append(count)

# Find the second highest count
second_high_count = 0
max = duplicate_count[0]
for i in duplicate_count:
    if i > max:
        second_high_count = max
        max = i
    elif i > second_high_count and i != max:
        second_high_count = i
 
if second_high_count == 0:
    print("There is no second highest count in the given string")
else:
    # Find the indexes and get the string
    for i in duplicate_count:
        
    second_high_countindx = duplicate_count.index(second_high_count)
    Second_high_str = unique_data[second_high_countindx]

    print("Second Highest duplicate count: ", second_high_count)
    print("Second Highest duplicate string: ", Second_high_str)


