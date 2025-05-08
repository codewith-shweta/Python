#return used to end function and send result back to caller

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z2 = x - y
    return z2


def multiply(x,y):
    z3 = x * y
    return z3

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))


def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + "" + last

full_name = create_name("hello", "dear")
print(full_name)