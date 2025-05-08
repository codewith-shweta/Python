sum = [12,4,5,6,87,24]
def is_even(n):
    return n % 2==0
even = set(filter(is_even, sum))
print(even)

# through lamda 
sum: int = [12,4,5,6,87,24]
even = tuple(filter(lambda n: n% 2 ==0 ,sum))
print(even)

num = {'evens,evens,out,out,in'}

def count(x):
     if x == 'evens':
          x.count()

count =list(filter(count,num))
print(count)
def main() -> None:
     count()
main()