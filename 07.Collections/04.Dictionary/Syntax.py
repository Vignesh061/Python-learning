# dictionary is a collection which is ordered , changeable and does NOT allow duplicate keys

dict_data = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(dict_data, "is:", type(dict_data))
print()

# dictionary => Does NOT allow duplicate keys
dict_data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "a": 10    # duplicate key, old value will be overwritten
}
print("Does NOT allow duplicate keys:", dict_data)
print()

#           Any type of data can be stored (keys & values)
dict_data = {
    1: "one",
    "two": 2,
    3: "three"
}
print("Any type of data can be stored:", dict_data)
print()

#           We can access dictionary items using keys
print("Access value using key:", dict_data[1])
print("Access value using get():", dict_data.get("two"))
print()

#           Dictionary length
print("Length of dictionary:", len(dict_data))
print()

#           Adding elements to dictionary
dict_data["four"] = 4
print("After adding element:", dict_data)
print()

#           Modifying elements in dictionary
dict_data["two"] = "TWO"
print("After modifying element:", dict_data)
print()

#           Removing elements from dictionary
dict_data.pop(3)
print("After removing element:", dict_data)
print()

#           Looping through dictionary
print("Looping through dictionary:")
for key, value in dict_data.items():
    print(key, ":", value)
print()

#           Dictionary methods
print("Keys:", dict_data.keys())
print("Values:", dict_data.values())
print("Items:", dict_data.items())
