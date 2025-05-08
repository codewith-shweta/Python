from functools import reduce

digit: int = [31,3,47,99,100]
sum = reduce(lambda a,b: a+b, digit)
print(sum)