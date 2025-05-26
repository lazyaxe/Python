#class variables are the variables that share the sam variable value with any object
#class variables are declared before constructor method

#example of such situation, students having different name, age , grades but they share the same class year
class Students:
    # ↓ delcaring a class variable 
    class_year = 2025 # <--this 
    number_of_students = 0 # <--this
    def __init__(self, name, age , grades):
        self.name = name
        self.age = age
        self.grades =grades
        Students.number_of_students+=1 #in the class "Students" access the variable number_of_students and increment by 1 when constructor is accessed by the object

Student1 = Students("Bobby Brown", "18", "A+")

Student2 = Students("Emily Chan", "17", "B-")

print("Student 1's Grades = ",Student1.grades)
print("Student 2's Grades = ",Student2.grades)

#but their Grad Year
print("Student 1's Graduation Year = ",Student1.class_year)
print("Student 2's Graduation Year = ",Student2.class_year)

#Preffered way of using class variables is by accessing it via the name of the class variable NOT BY ITS OBJECTS NAME i.e use Students(class name) NOT Student1(object/instance name)
#because in more complex code its harder to differentiable between a class atribute/member or a variable
print("Student 1's Graduation Year = ",Students.class_year)
print("Student 2's Graduation Year = ",Students.class_year)

#calling number_of_students variable
print(f"Graduating class of {Students.class_year} has {Students.number_of_students} students.")