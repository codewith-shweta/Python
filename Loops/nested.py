#nested loop = a loop within a loop
#               outer loop:
#                 inner loop:

for x in range(3):
    for y in range(1,9):
        print(y)
    print()


rows = int(input("How many rows: "))
coloumns = int(input("How many coloumns: "))
symbol = input("Enter a symbol to use: ")

for x in range (rows):
    for y in range(coloumns):
        print(symbol,end="")
    print()    
