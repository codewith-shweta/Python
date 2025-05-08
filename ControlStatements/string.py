username = input("Enter a username: ") 
username.find()

if len(username) > 12:
    print("Username can't be more than 12 char")

else:
    print(f"Welcome {username} ")