num=[]
n=int(input("Enter the size of the list :"))

for i in range(n):
    value=int(input(f"Enter the number {i+1} :"))
    num.append(value)
    
for i in  num:
    if (i%2==0):
        print("Even num in list:",i)
    else:
        print("Odd num in list:", i)
