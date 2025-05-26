#Allow operations related to class itself, mostly operations on class variables                                                               
# takes 'cls' as the first parameter, represents the class itself .

class student:
    student_count = 0
    total_gpa=0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa 
        student.student_count += 1
        student.total_gpa+=gpa #student.total_gpa = student.total_gpa + gpa
    #now we need a instance method to show info 
    def get_info(self):
        return f"{self.name} = {self.gpa}"
    
    #now we need class method to access the class variable
    @classmethod
    def get_count_students(cls):
        return f"Total number of students = {cls.student_count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.student_count <= 0:
            return 0;
        else:
            return f"{cls.total_gpa/cls.student_count}"
    
student1=student(name="H1N1", gpa=4.5)
print(student.student_count)
print(student.total_gpa)

student2=student(name="V8", gpa=8)
print(student.student_count)
print(student.total_gpa)

student3=student(name="Snapdragon", gpa=7)
print(student.student_count)
print(student.total_gpa)

print(student.get_count_students())
print(student.get_average_gpa())