# Find the largest and smallest  number without using max

num = [5,12,3,20] 

largest=num[0]
smallest=num[0]
for i in num:
    if i > largest:
        largest=i
    if i < smallest:
        smallest=i
        
print("Largest Number:",largest)
print("Smallest Number:",smallest)
    
    
