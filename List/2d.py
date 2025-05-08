'''
fruits =    ["apple","banana","strawberry"]
vegetables= ["potato","ladyfinger","tomato"]
meats=      ["eggs","chicks","fish"]

groceries= [fruits,vegetables,meats]
print(groceries[1] [1])
'''
#second nd simple way
carts  =[   ["apple","banana","strawberry"],
           ["potato","ladyfinger","tomato"],
           ["eggs","chicks","fish"]]
#print(carts [0] [2])
for cart in carts:
    for food in cart:
        print(food)
print()
