#variable scope= visible nd acessible 
 # scope resolution = (local-> enclosed-> global-> built-in) 
def func1():
    x=2
    print(x)

def func2():
    x=4
    print(x)        #local                                                                                                                 

func1()
func2()

def class1():
    total=23

    def classA():
        total=42
        print(total)
    classA()

class1()

def func1():
    print(x)

    def func2():
        print(x)
    func2()
x = 3               #global
func1()


from math import e 

def func1():
    print(e)

e = 0
func1()        #built in 