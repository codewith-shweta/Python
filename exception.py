#exception = event occurs the flow of programme 
#(zerodivision error ,type error and value error)
#try,except,finally

#  1/0
#  1 + "1"
#  int("pizzaz")

try:
    num = int(input("Enter number: "))
    print(1/num)

except ZeroDivisionError:
    print("Number cant be divide by zero: ")

except TypeError:
    print("Enter only numbers plzz! ")

except Exception:          #basically a catcher 
    print("oops! something went wrong😣")

finally:         #mandatory 
    print("Do clean up here! ")


    

