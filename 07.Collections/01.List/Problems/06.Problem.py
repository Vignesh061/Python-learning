# find the num in the list

num = [5, 12, 3, 20]
search = 12
found = False

for i in num:
    if i == search:
       print(i)
       

if search in num:
    print(search)
    
for i in range(len(num)):
    if search==num[i]:
        print(num[i])
    
    