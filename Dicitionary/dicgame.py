#concession stand program 

menu ={ "pizza":     23,
        "burger":    34,
        "sandwhich": 58,
        "hamburger": 40,
        "nachos":    69,
        "hotdog":    70 }

cart= []
total =0 

print("--------MENU--------")
for key , value  in menu.items():
    print(f"{key:10}: ${value:.2f}")  
print("------------------")


while True:
    food= input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR MENU -------")        
for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f" Total is: ${total} ")