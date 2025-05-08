'''
user = int(input("Enter the number: "))
numbers= (("1","2","3"),
          ("4","5","6"),
          ("7","8","9"),
          ("","0","."))
#print("Enter the {numbers}")
#print(numbers)
#print(numbers[0] [1])

for number in numbers:
    for digit in number:
        print(digit)
   # print(number) 
#print()
'''
numbers= (("1","2","3"),
          ("4","5","6"),
          ("7","8","9"),
          ("","0","."))
print(numbers, end="")
print()

'''
for row in numbers:
    for num in row:
        print(num)
'''