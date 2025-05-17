#duck typing 

class Human:
    alive = True

class Boy(Human):
    def __init__(self):
        print("HEY!")

class Girl(Human):
    def __init__(self):
        print("Nevermind!")

class Car():
    alive = False
    def __init__(self):
        print("🚘")

humans = [Boy(), Girl(), Car()]

for human in humans:
    print("--")
    print(Human.alive)
    print(Car.alive0o )


    #um i dont get this understood 