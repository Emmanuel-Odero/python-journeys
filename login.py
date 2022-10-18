user_name = input("Entre youe username: ")
user_password = input("Entre your password: ")

if(user_name != "Admin"):
    print(f"Hello {user_name} please entre your correct details")
elif(user_password != "1234@admin"):
    print(f"Hello {user_name} please entre the correct details")
else:
    print("You are logged in")