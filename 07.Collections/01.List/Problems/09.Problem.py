foods=[]
prices=[]
total=0

while True:
    food=input("Enter the Food name or (q for quit ) : ")
    
    if food.lower() == "q":
        break
    else:
        price=float(input(f"Enter the rate for {food} : "))
        foods.append(food)
        prices.append(price)
    
    
print("------ Your cart -------")
print()
for food in foods:
    print( food, end="\n")
for price in prices:
    total+=price
    # print(total)
    
print()

print(f"Your total price is {total} ")


