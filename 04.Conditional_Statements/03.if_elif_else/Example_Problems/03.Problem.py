#  BMI(Body Mass Index) Calculator - print Underweight , Normal , Overwitht, 

height=float(input("Entere you Height in Meteres:"))
weight=float(input("Enter you Weight in Kg:"))

bmi=weight/(height*height)

print("Your BMI is:",round(bmi,2))

if bmi<18.5:
    print("Category: Underweight")
elif bmi<25:
    print("Catageory:Normal")
elif bmi<30:
    print("Category:Overweight")
else:
    print("Catageory:Obese")