#or , not logical operators
name = input("Enter your name:")
while name =="":
    print("You did not enter your name")
    name = input("Enter your name:")
else:
    print(f"Hello {name}")


age = int(input("Enter your age:"))
while age < 0:
        print("Age shouldn't be negative value")
        age = int(input("Enter your age:"))

        print(f"your age {age} is")

programe = input("Hello once again honey (q to quit): ")
while not programe == "q":
    print(f"{programe} Love!")
    programe=input("Not happy (q to quit)")

    print("Bye")

num= input("Enter your choice(Between 1 and 10):")
while num < 1 or  num > 10:
    print(f"{num} is not valid")
    num= int(input("Enter your choice"))

    print(f("Your number is {num}"))