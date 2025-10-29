# list is a collection which is order and changeable and allow duplicate members.

list=[1,2,3,4,5]
print(list,"is:",type(list))
print()

# list[] => Allow duplicate values
list=[1,2,3,4,5,5]
print("Allow Duplicate values:",list)
print()


#           Any type of data we can stored

list=[1,"two",3,"four",5,"six"]
print("Any type of data can be stored:",list)
print()

#           We can modify  the list items .We can Add or Remove

list.append(10) # Add this element in last
print(list)
list.insert(1,"one") # (index,elements)Insert the element in first
print(list)
list.pop() #remove the element form last
print(list)
list.pop(5) #remove the element using index value
print(list)
list2=[7,8,9,19]
list.extend(list2)
print(list)