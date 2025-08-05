# Check if a number si even . If yes, check if it is greater than 50

number=int(input("Enter a number : "))

if number%2==0:
    if number>50:
        print(f" {number } is even and greate than 50")
    else:
        print(f"{ number } is even but it is less than 50")
else:
    print(f"{number } is odd")