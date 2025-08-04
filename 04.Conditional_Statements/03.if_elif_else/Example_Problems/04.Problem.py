# Take  salary as input and apply tax slabs:

salary=float(input("Enter a salary:"))

if salary>=1000000:
    tax=30 * salary / 100
    print(f" Your salary was {salary} so You have {tax} tax")

elif salary>=5000000:
    tax=20*salary/100
    print(f"Your salary was {salary} , so yoy have {tax}")

elif salary>=250000 :
    tax=5*salary/100
    print(f"Your salary was {salary} , so you have {tax}")
else:
    print(f"Your salary is{salary} , so you have no tax")
