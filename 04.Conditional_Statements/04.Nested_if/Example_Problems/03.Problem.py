# If a student passed (mark >=40 ),check if they got distinction (>=75)

mark=int(input("Enter your make: "))

if mark>=40:
    if mark>=75:
        print(f"Your mark is {mark}  and You got distinction")
    else:
        print(f"Your mark is {mark} and you are Pass ")
else:
    print("Your are fail")
