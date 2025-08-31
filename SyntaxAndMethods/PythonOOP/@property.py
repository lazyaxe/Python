# Property decorator is used to define a method as a property and it can be accessed as an attribute

# by property we can add additional logic when to read write or delete code 

# @property gives you getter setter or deleter method
"""
What is a property() method:
~>The property method lets a method to be called as an attribute.
~> It provides a better way to implement encapsulation i.e. A better way to implement Getter and Setters

Parameters of property():
    ~>fget() used to get the value of attribute.
    ~>fset() used to set the value of attribute.
    ~>fdel() used to delete the attribute value.
    ~>doc() string that contains the documentation (docstring) for the attribute.

What is a @property decorator:
~> The property decorator is a decorator for property method of the class
~> It provides a cleaner way to use property().
"""

# 1. Using property()
class Square:
    def __init__(self, length: int|float) -> None:
        self.__length=length # private instance attribute   
    
    def get_length(self)-> int|float:
        return self.__length
    
    def set_length(self, new_length: int|float):
        if new_length<0:
            print("Lenght cannot be less than zero")
        else:
            self.__length=new_length

    def delete_lenght(self)->None:
        if self.__length<=0:
            print("Nothing to delete")
        else:
            print(f"Deleted: {self.__length}")
            del self.__length
    side=property(fget=get_length, fset=set_length, fdel=delete_lenght)

# 2. Using @property
class Rhombus:
    def __init__(self, length: int|float) -> None:
        self.__length=length
    """
    Syntax of @property:
    ~> All the methods in the @property need have same names.
    ~> With decorators, you're chaining functionality to the property by assigning handlers to that same property name.
    ~> If names differ like get_length and length—Python won't connect them, causing functionality breaks.

    @property
    def attribute(self)->attribute
        return attribute

    @attribute.setter
    def attribute(self, new_value)->None
        self.attribute=new_value

    @attribute.deleter
    def attribute(self)->None
        del self.attribute
    """
    @property
    def length(self)->int|float:
        #length now is the property name, this is the getter method.
        return self.__length
    @length.setter
    def length(self, new_length)->None:
        if new_length>0:
            self.__length=new_length
        else:
            print("Width can't be negative")

    @length.deleter
    def length(self)->None:
        del self.__length
        print("Width Deleted.")
    """
    Why the @lenght.getter isn't needed?
    ~>The @property decorator is basically a syntactic sugar for property(). 
    ~> So the use of @property inits the method property:
        length = property(length)
    ~> Now lenght is property and where the setter is defined. And it is the first method that the @property expects
    ~> Now, there's a @length.getter method but it's for later use when there's a need to re-define/override 
    """

s1= Square(length=10)

print("Lenght of square: ", s1.side)#This will call the fget=get_length

s1.side=56#This will call the fset=set_length

print("New lenght of square: ", s1.side)

del s1.side# will delete the attribute lenght from the memory

r1 = Rhombus(length=2)

r1.length = float(input("Enter the new length = "))
print(r1.length)

r1.length = float(input("Enter a new length = "))
print(r1.length)

del r1.length#rectangle1._width i.e the _width attribute of the instance rectange1 has been deleted
del r1.length
