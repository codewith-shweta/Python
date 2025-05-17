class Student:
    year = 2024
    std = 0 
    
    def __init__(self,name,age,roll):

        self.name = name
        self.age = age
        Student.roll = roll
        Student.std = +1


student1 = Student("Rohit", "12", "4")
student2 = Student("Mohit", "13" , "10")

print(student1.name)


print(student1.roll)

#print(Student.year) 
print(Student.std)    #accesing the class var direct 

print(f"My graduating class of {Student.year}")