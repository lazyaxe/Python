"""
super():
    A function used in child class(sub-class) to call methods from a parent class(base-class)

~> It is similar to C++'s way of inheriting constructors from parent classes in Python
~> Also can be used for "Co-operative Polymorphism" and avoid the Diamond Problem.
~> super() is a mro navigator from which

SYNTAX:
class base:

"""
from math import pi


class Shape:
    def __init__(self, shape_colour: str, is_colour_filled: bool)->None:
        self.shape_colour = shape_colour
        self.is_colour_filled = is_colour_filled

class Circle(Shape):
    def __init__(self, shape_colour: str, is_colour_filled: bool, radius: int|float=0)->None:
        super().__init__(shape_colour, is_colour_filled)
        self.radius= float(radius)
    """
        Why super() is used here?:
        Super function is needed here because of two things:
        1. Although the sub-class inherits the constructor from the base-class, but we can't tweak/add/remove something from the base-class's contructor. If we want to, then we need to make a constructor of our own.
        2. We need to remove the need of manually re-assigning the attributes that already inherited from the base class...
        3. We need to make a contructor of a class more "Pythonic".

        ~>So the super() function, goes to the base/parent class of this sub-class and super().__init__() access the __ini__ method of the base class i.e.super() access the Shape class and accesses/calls its constructor and assigns the  given as args. super()__init__() handled the assignment of the inherited attributes neatly.
        ~>So here, super().__init__ is like calling a constructor for a constructor. :O
    """
    
    def calculate_area(self)->int|float:
        return pi*(self.radius**2)

class Triangle(Shape):
    def __init__(self, shape_colour, is_colour_filled, width=0, height=0):
        super().__init__(shape_colour, is_colour_filled)
        self.width = float(width)
        self.height = float(height) 

class Tire(Circle):
    def __init__(self, shape_colour: str, is_colour_filled: bool, radius: int | float = 0, inner_radius: int | float = 0) -> None:
        super().__init__(shape_colour, is_colour_filled, radius)
        self.inner_radius=inner_radius

    def calculate_area(self) -> int|float:
        """
        Because Tire is a sub class of Circle it inherits the attributes, constructor and methods of class Circle.
        Because we have the same nameed method, we are doing method overriding of the base method.
        We can do this overriding in a Pythonic way, by super()...
        The super() accesses the method of the base class but where self is this class's instance... 
        """
        return super().calculate_area() - pi*(self.inner_radius**2)

circle1 = Circle(shape_colour="Red", is_colour_filled=False, radius= 69)
print(circle1.radius, "meters")
print(circle1.shape_colour)
print(f"Is shape filled ?", circle1.is_colour_filled)
print(f"The area of circle {circle1.calculate_area()}")
print()

tire1=Tire(shape_colour="Black", is_colour_filled=False, radius=10, inner_radius=5)
print(f"The area of tire {tire1.calculate_area()}")

triangle1 = Triangle(shape_colour="Purple", is_colour_filled=True, width=96, height=69 )
print(triangle1.width, "meters")
print(triangle1.height, "meters")
print(triangle1.shape_colour)
print(f"Is shape filled ?", triangle1.is_colour_filled)