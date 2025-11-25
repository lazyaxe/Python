#SUPER FUNCTION IN Python
"""
    ~>A function used in child class(sub-class) to call methods (usually the constructor & base/super class's methods) from a parent class(base/super-class)
    ~> It is similar to C++'s way of inheriting constructors from parent classes in Python
    ~> Also can be used for "Co-operative Polymorphism" and can help in avoiding the Diamond Problem
        ~> super() can be a mro navigator so if a class SubClass(BaseClass1, BaseClass2)
        ~> The super function will call the BaseClass1's method then BaseClass2's method. 

SYNTAX:
    class Base:
        def method(self, *attributes):
            #code here
    
    class Sub(Base/Super):
        def method(self, *attributes):
            super().method(*inherited_attributes)
"""
from math import pi

class Shape:
    def __init__(self, shape_colour : str, is_colour_filled : bool)->None:
        self.shape_colour = shape_colour
        self.is_colour_filled = is_colour_filled
    
#Simple Inheritance
"""
super() for constructors __init__:
    ~>Super function is needed here because of two reasons:
        1. Although, the sub-class inherits the constructor from the base/super-class, but we can't tweak/add/remove something in the inherited base/super-class's contructor. If we want to do that, we need to make a constructor of our own.
        2. We need to remove the need of manually re-assigning the attributes that already inherited from the base/super class...and make the process Pythonic.
    ~>So the super() function, goes to the base/super/parent class of this sub-class and super().__init__() access the __init__ method of the base/super class i.e.super() accesses the Shape class and calls its constructor and assigns the  given as args. super()__init__() handled the assignment of the inherited attributes neatly.
    ~>So, here super().__init__() is like calling a constructor for a constructor. O_O
"""
class Circle(Shape):
    def __init__(self, shape_colour : str, is_colour_filled : bool, radius : int | float = 0) -> None:
        super().__init__(shape_colour, is_colour_filled)
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * (self.radius ** 2)

circle1 = Circle(shape_colour = "Red", is_colour_filled = False, radius = 69)
print(circle1.radius, "meters")
print(circle1.shape_colour)
print(f"Is shape filled ?", circle1.is_colour_filled)
print(f"The area of circle {circle1.calculate_area()}")
print()

#Multi-level Inheritance
class Tire(Circle):
    def __init__(self, shape_colour: str, is_colour_filled: bool, radius: int | float = 0, inner_radius: int | float = 0) -> None:
        super().__init__(shape_colour, is_colour_filled, radius)
        self.inner_radius = inner_radius

    def calculate_area(self)-> float:
        """
        ~> Because Tire inherits the attributes, constructor and methods of class Circle.
        ~> We have the same named method in the base/super class, therefore we are doing method overriding of the base/super method calculate_area.
        ~> We can do this overriding in the Pythonic way, by super function
        ~> The super() accesses the method of the base/super class but uses the 'self' of this class's instance 
        """
        return super().calculate_area() - (pi * self.inner_radius ** 2)

tire1 = Tire(shape_colour = "Black", is_colour_filled = False, radius = 10, inner_radius = 5)
print(f"The area of tire {tire1.calculate_area()}")