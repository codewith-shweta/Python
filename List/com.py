#list comprehnsion = [expression for value in iterable if condition] 

list =[]

for x in range(1,11):
    list.append(x * 2)
    print(list)
print()
# in a better or other way as for comprehension 

doubles = [x * 2 for x in range(1,11)]
print(doubles)
