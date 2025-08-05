# Check if a number is positive . Then check if it is divisible by 3

number = int(input("Enter a number : "))

if number > 0:
    if number%3==0:
        print(f"{number} is divisible by 3. and positive")
    else:
        print(f"{number } is Not divisible by 3. But it is positive")

else:
    print(f"The {number} is negative")