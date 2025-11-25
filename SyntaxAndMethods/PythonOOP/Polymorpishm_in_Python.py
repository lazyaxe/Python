# POLYMORPHISM IN Python:
"""
~> Polymorphism means "many-forms" in context of programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

Types of polymorphism:
1. Method overloading | Compile-time | Static Polymorphsim
    ~> Not directly supported in Python

2. Method overriding | Run-time | Dynamic Polymorphism
    ~> Polymorphism with Inheritance
    ~> Python does not allow the same method to be re-written else where unless it is inherrited by a class .
    ~> Not directly supported in Python

3. Polymorphism with Class Methods:
    ~> Duck Typing
"""

#Two ways to achieve Polymorphism 
    # 1. Classic Inheritance
    # 2. Duck Typing = "If it walks like a duck, speaks like a duck. It must a duck"

"""
There are two ways to do the classic polymorphism.
1. With Abstract Classes/Virtual Classes ("Formal polymorphism")
    ~> The formal polymorphism is required in other OOP languages like C++, C# and Java but it's seen as a formalilty in Python.
2. Without Abstract classes/Vitual Classes
"""

#Method-Overriding:
# 1. With Abstract Classes/Virtual Classes
# 2. Without Abstract Classes/Virtual Classes(already did in super_function.py)

#'abc' is 'abstractbaseclass' module and 'ABC' a class & 'abstractmethod' is a decorator.
from abc import ABC, abstractmethod 

#Making a "virtual" class
    # ~> A virtual class is class that has a virtual method.
class Shape(ABC):

    #Making a "virtual" method
    # ~> A virtual method is "non-functional" but it compulsory for the inheritted class to make their own non-virtual/regular method.

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    # No super() will be used here because parent class does not have any constructor nor any method to use/modify.
    def __init__(self, radius):
        self.radius = radius

    #The real method implementation for Circle
    def area(self):
        return self.radius * self.radius * (22 / 7)
    
    def __str__(self):
        return "Circle"
    
class Triangle(Shape):
    def __init__(self, witdh, height):
        self.width = witdh
        self.height = height

    #The real method implementation for Triangle
    def area(self):
        return self.width * self.height * (1 / 2)
    
    def __str__(self):
        return "Triangle"
    
# Multi level inheritance:
# Circle class has a constructor which we need to borrow but we don't need to make our own area method because circle already has real-method.

class Pizza(Circle):
    def __init__(self, topping_name, radius):
        super().__init__(radius)
        self.topping_name = topping_name

    def __str__(self) -> str:
        #returns a string to print function if instance/object is printed
        return f"{self.topping_name}" + " Pizza"

#Creating the a list of instances:
Shapes_list : list[Shape] = [Circle(radius = 5), Triangle(height = 17, witdh = 23), Pizza(topping_name = "Pineapple", radius = 12)]

#Testing out the Polymorphism by calling the area() method of each instance:
for shape_obj in Shapes_list:
    print(f"Area of {shape_obj} = {shape_obj.area()} sq cm.")#shape_obj temporaily hold as the instance/object

pizza1 = Pizza("Pepperoni", 12)
print("The name of the pizza: ", pizza1)

# Function/Method-Overloading: 
"""
~> Though not primarily supported, Python supports method overloading as long as the function/methods of same name have
different arguments.
~> If a function/method has written more than once only the latest declaration will be considered for function calls
"""
#There are two ways to simulate overloading in Python:

# By making if conditions in a single function function/method:

class Swiss_foo:
    def __add__(self, a_list, datatype: str):

        datatype = datatype.lower()
        if datatype == 'int':
            result = 0
            for number in a_list:
                result += number
            print(result)

        elif datatype == 'str' or datatype == 'string':
            result = ''
            for char in a_list:
                result += char + " "
            print(result)

s1 = Swiss_foo()

s1.__add__(a_list = [1, 4], datatype = 'int')

s1.__add__(a_list = ['Harsh', 'Sharma'], datatype = 'str')