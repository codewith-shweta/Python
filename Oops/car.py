# classes 
class Car:
    def __init__(self,model,number,for_sale,color):     #constructor method
        self.model = model 
        self.number = number
        self.for_sale = for_sale
        self.color = color

#methods
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"Stop the {self.color}  {self.model}")

    def describe(self):
        print(f" {self.model} {self.number} {self.color} {self.for_sale}")



magic = __name__

class Animals: 
    def __init__(self,pet):
        self.pet = "pet "

