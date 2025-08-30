"""
CLASS METHOD DECORATOR:
~> @classmethod is a decorator declared before decalring a method for class i.e. a classmethod().

What is a class method?:
~> Class method here refers to method which is bound/for a class rather than it's instance/object.
~> Because it's bound to class, it takes 'cls' short for class as the first parameter rather than the 'self'.
~> The @classmethod decorator calls the classmethod() internally.
~> A class method can access or modify the class's attributes/variables while a static method can't access or modify it.
~>class variables/attributes can be accessed directly but its recommended to use a classmethod as a factory method

What is a Factory method:
~>A factory method returns the class objects(like a constructor/__init__ method).
"""


class Student:
#Class variables|attributes:
    student_count = 0

    def __init__(self, name: str="Unknown", gpa: int|float=0)->None:
    #instance attributes:
        self.name = name
        self.gpa = gpa 
        Student.student_count += 1
    
#classmethod to access the class variable 'student_count'.
    @classmethod
    def get_student_count(cls)-> int:
        return cls.student_count

class Undergraduate(Student):
#The class attributes and classmethod are inherrited by sub-class from base-class
# i.e Undergraduate inherits student_count, get_student_count() by Student
    
    degree="B.Tech in Computer Engineering Specialization in Artifical Intelligence and Machine Learning"
    
    ug_count=0

    def __init__(self, name: str="Unknown", gpa: int|float=0)->None:
        super().__init__(name, gpa)
        Undergraduate.ug_count+=1

    @classmethod
    def get_degree(cls)-> str:
        return cls.degree

student1=Student(name="Prem", gpa=9.4)#the class variable will be incremented by 1. Now student_count=1
print(Student.student_count)

student2=Student(name="Vivek", gpa=9.5)#Now student_count=2
print(Student.student_count)

student3=Student(name="Sheprie", gpa=7)#Now student_count=3
print(Student.student_count)

print(Undergraduate.ug_count)

student4=Undergraduate(name="Harsh Sharma", gpa=9.1)
print(Student.student_count)
"""
FYI:
~> The student_count attribute will be incremented, even if an instance from Undergraduate class will be created.
~> Why? Because the Undergraduate class used the constructor of Students class using the super().__init__(). The super function access the constructor method which triggers the increment of student_count.
~> The Undergraduate.student_count() will be lesser or equal to Student.student_count().
"""
print(Undergraduate.ug_count)


