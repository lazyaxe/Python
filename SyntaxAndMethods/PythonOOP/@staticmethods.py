#static methods = a method that belongs to an class rather than an instance(object of that class) that do not need any class data

#For Operations in instances, Instance methods are used.Instance methods take 'self' as the parameter

class employee:
    def __init__(self, name, job):
        self.name=name
        self.job=job

    def get_employee_info(self):
        return f"{self.name} is a {self.job}" 
    #if we need to check for valid job positions in an office(that do not require class data)
    @staticmethod
    def isValidJob(job):
        vaild_jobs=("Manager", "Engineer", "HR", "Janitor")
        return job in vaild_jobs# this would return a bool
    
emp1=employee(name="Harsh", job="Mage")#Because Mage job is not in valid_job isVaildJob will return False
print(emp1.get_employee_info())
print(f"Is {emp1.job} job vaild ?",employee.isValidJob(emp1.job))#used class name to access the method not the object's name