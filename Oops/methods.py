#class methods = instance (self) methods(clr)

class Student:

    count = 0 
    total  = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa 
        Student.count += 1
        Student.total += 0.1

    def get_info():
        return f"{self.name}  {self.gpa}"


    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count} "


    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0 
        else: 
            return f"Average gpa{cls.total / cls.count:.2f}"


student1 = Student("Shwet", "9.8")
student1 = Student("Komal", "9.3")
student1 = Student("Diya", "9.5")

print(Student.get_count())
print(Student.get_average())  #this is accesing the class data


