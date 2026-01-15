# set is a collection which is unordered, unchangeable* and does NOT allow duplicate members
# (*unchangeable means items cannot be changed, but we can add/remove items)

set_data = {1, 2, 3, 4, 5}
print(set_data, "is:", type(set_data))
print()

# set => Does NOT allow duplicate values
set_data = {1, 2, 3, 4, 5, 5}
print("Does NOT allow duplicate values:", set_data)
print()

#           Any type of data can be stored
set_data = {1, "two", 3, "four", 5}
print("Any type of data can be stored:", set_data)
print()

#           We cannot access items using index (unordered)
# print(set_data[0])  ❌ Error

#           But we can loop through set elements
print("Accessing elements using loop:")
for item in set_data:
    print(item)
print()

#           Set length
print("Length of set:", len(set_data))
print()

#           Adding elements to set
set_data.add(6)
print("After adding element:", set_data)
print()

#           Removing elements from set
set_data.remove(3)
print("After removing element:", set_data)
print()

#           Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
