# Check if user islogged in . If yes, Check if they are admin or user. Solve this problem by  using nested if
 

is_logged_in=input("Are you Logged in ? (yes/No): ")
if is_logged_in=="yes":
    user_role=input("Are you (admin/user): ")
    if user_role=="admin":
        print("You are admin you have full acces")
    elif user_role=="user":
        print("You are user you have limited acces")
    else:
        print("unknow role")
else:
    print("Please logged in to continue")
    