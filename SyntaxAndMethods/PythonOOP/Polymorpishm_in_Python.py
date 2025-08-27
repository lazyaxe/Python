#Two ways to achieve Polymorphism 
#   1. Inheritance = An object could be treated of the same type as a parent class
#   2. Duck Typing = Object mustc= have necessary attributes/methods

from abc import ABC, abstractmethod #abc is abstractbaseclass and ABC is  ans abstractmethod is a decorator

class Shape(ABC):
    @abstractmethod#<--decorator
    def area(self):
        pass

class circle(Shape):
    def __init__(self, radius):#no super() used here because parent class does not have any constructor to inherit/use
        self.radius=radius
    def area(self):
        return self.radius*self.radius*(22/7)
    def __str__(self):
        return "Circle"
class triangle(Shape):
    def __init__(self, witdh, height):
        self.width= witdh
        self.height=height
    def area(self):
        return self.width*self.height*(1/2)
    def __str__(self):
        return "Triangle"
class pizza(circle):#multi level inheritance and also circle class has a constructor which we need to borrow and we don't need to make our own area method because circle already has it and it's not abstract
    def __init__(self, topping_name, radius):#achived polymorphism by making its own constructor 
        super().__init__(radius)
        self.topping_name=topping_name
    def __str__(self):#returns a string to print function if instance/object is printed
        return "Pizza"

Shapes_list: list[object] =[circle(radius=5), triangle(height=17, witdh=23), pizza(topping_name="pineapple", radius=12)]

for shape_obj in Shapes_list:
    print(f"Area of {shape_obj} = {shape_obj.area()} sq cm.")#shape_obj temporaily hold as the instance/object


pizza1=pizza("pepe", 12)
print(pizza1)



