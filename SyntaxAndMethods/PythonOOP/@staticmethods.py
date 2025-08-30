"""
Static Methods:
~> A static method in a python is a method that is used when some method when a method does not need any class attributes or the instance's attribute.
~> Simply put, A static method is a method which does not uses the attributes of an instance or class.
~> Therefore, static method requires neither a 'cls' or 'self' parameter.
~> It can be put inside a class with the help of @staticmethod.
~>Or can be simply put outside the class.
~> A staticmethod cannot access/modify class attributes.
"""

#Example:
class Calculator:

    def __init__(self, company_name: str, model: str) -> None:
        self.company_name=company_name
        self.model=model
    
    def get_info(self)->str:
        return f"{self.company_name} {self.model}"
    
    @staticmethod
    def add(*numbers: int|float)->int|float:
        total=0
        for number in numbers:
            total+=number
        return total
    
    @staticmethod
    def div(*numbers: int|float)->float:
        if 0 in numbers:
            return 0
        else:
            result=0
            for number in numbers:
                result= numbers[0]/number
            return result

c1: Calculator=Calculator(company_name=
"Casio", model="MJ-120GST")

print(c1.get_info())

print(c1.add(1, 2.5, 3))

print(c1.div(5, 0.5))