#compound interest calculator
principal =0
rate =0 
time =0
while principal <=0:
    principal = int(input("Enter the principal amount: "))
    if principal <=0:
        print("The principal amount cant be zero")
    print()

while rate <=0:
    rate = int(input("Enter the rate interest: "))
    if rate <=0:
        print("The rate interest cant be zero")

while time:
    time =("Enter the time period: ")
    if time:
        print("The time is period id mandetory")
print(principal)
print(rate)
print(time)

#pending