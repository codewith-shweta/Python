def sums():
    a: int =[1,2,3,4]  
    print(a)


def chechk():
     even, odd  = 2 ,5
     print('even' if even % 2== 0 else'odd' if odd % 2==0 else'Unidentified')
        

values: str=['Hello','This', 'Is','Shwet!']
def reverse(): 
    if values:
     values.reverse()    
     print(values)

def greet():
    name= input('Enter your name: ')
    print(f"HELLO! {name}")

def main() -> None:
    sums()
    chechk()
    reverse()
    greet()
main()