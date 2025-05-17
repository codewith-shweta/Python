# multipal inheritance = inherit s frome more than one class ex:- c(a,b)
# multilevel = inherites from parents which inherits from other parents *
 
class Animal:
    pass 

    def __init__(self,name):
        self.name = name 

    def eat(self):
        print(f" {self.name} is eating")

    def sleep(self):
        print(f" {self.name} is sleeping")

class Prey:
    def flee(self):
        print(f" {self.name} is fleeing")

class Predator:
    def hunt(self):
        print(f" {self.name} is hunting ")

class Fish(Prey,Predator,Animal):
    pass

class Rabbit(Prey,Animal):
    pass

class Panda(Animal):
    pass 

rabbit = Rabbit("Bunny")
fish = Fish("Fairy")
panda = Panda("Visha")

#rabbit.flee()
#fish.flee()

#fish.hunt()

#panda.eat()
#panda.sleep()

#fish.eat()
#rabbit.sleep()

rabbit.flee()