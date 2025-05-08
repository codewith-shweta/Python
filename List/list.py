#collection = single "variable" used to store mulitple values list,set,tuple
#list in square brackets 
#List (append,remove,len,insert,sort,reverse,index,count)
fruits = ["apple","coconut","grapes"]
print(fruits)
#print(fruits[1])
#print(dir(fruits))   #to see all attribute
#print(help(fruits))  #to see all methods 
#fruits[0] = "pineapple"
fruits.sort()
fruits.append("orange")
fruits.insert(2,"Bananana")

print("apple" in fruits)
'''cars = ["BMW", "skoda","kn","creta"]

for car in cars:
    print(cars[::2])
'''
for fruit in fruits:
    print(fruit)
