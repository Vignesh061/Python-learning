# tuple is a collection which is ordered and unchangeable and allows duplicate members.

tuple_data = (1, 2, 3, 4, 5)
print(tuple_data, "is:", type(tuple_data))
print()

# tuple() => Allow duplicate values
tuple_data = (1, 2, 3, 4, 5, 5)
print("Allow Duplicate values:", tuple_data)
print()

#           Any type of data can be stored
tuple_data = (1, "two", 3, "four", 5, "six")
print("Any type of data can be stored:", tuple_data)
print()

#           We cannot modify the tuple items (Immutable)
# tuple_data[0] = 10   ❌ Error: tuple does not support item assignment

#           But we can access tuple elements
print("First element:", tuple_data[0])
print("Last element:", tuple_data[-1])
print()

#           Tuple length
print("Length of tuple:", len(tuple_data))
print()

#           Tuple slicing
numbers = (10, 20, 30, 40, 50)
print("Sliced tuple:", numbers[1:4])
print()

#           Tuple unpacking
a, b, c = (1, 2, 3)
print("Unpacked values:", a, b, c)
