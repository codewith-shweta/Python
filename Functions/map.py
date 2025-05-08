digit: int = [31,3,47,99,100]

def doubles(x):
    print(x +2)

update= set(map(doubles,digit))
print(update)

#thorugh lambda
digit: int = [31,3,47,99,100]

add = list(map(lambda n: n+2 ,digit ))
print(add)