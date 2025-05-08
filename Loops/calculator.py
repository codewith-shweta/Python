import math
print(math.e)
print(math.pi)
#square root 
print(math.sqrt(4))
#ceil (round around) 
print(math.ceil(11.56)) 

choice = 0
while (choice != 5):

    num1 =int(input("ENTER THE VALUE 1:-"))
    num2 =int(input("ENTER THE VALUE 2:-"))

    print ("ENTER THE NUMBER 1= ADDITION")
    print ("ENTER THE NUMBER 2= SUBTRACTION")
    print ("ENTER THE NUMBER 3= MULTIPLICATION")
    print ("ENTER THE NUMBER 4= DIVISION")
    print ("ENTER THE NUMBER 5= TERMINATE")

    choice =int(input("ENTER YOUR CHOICE :"))
     
    match choice:

     case 1:
        print("➕",num1 + num2)

     case 2:
        print("➖",num1-num2)

     case 3:
        print("❌",num1 * num2)

     case 4:
        print("➗",num1 / num2)

     case 5:
        print ("THANK YOU😊")
