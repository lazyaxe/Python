
"""
Encapsulation protects your classes from accidental changes or deletions in attributes and promote restriced usage for security and data isolation

The Python follows the "We Are All Adults Here" (WAAAH) phillosphy...
This means the encapsulation in python isn't as strict as other OOP paradigm languages like C++, Java...

Access modifers: 
The Access modifers are used to restrict the access of data/methods from objects which do not have privellge... 
    Access Modifiers in Python:
        for private _MemberName(single underscore), this can be acccessed by base-class and its sub-classes
        for private(with name mangling) __MemberName(double underscore), this can be acccessed by only the base-class, '__' triggers the name mangling of the class_name.
    If we access the access modified members of this class outside, we get an AtributeError.

    There are mainly two ways to access the private varible:
        1. Classic getter and setter approach.
        2. By decorators.
        3. Accessing them directly(Python doesn't care)
        """
class Tree:
    def __init__(self, type: str, height: int|float):
        self._height = height
        self.__type= type
        """
            _height due to being a single underscore naming convention it does not triggers Name Mangling.It is used as a reminder that this variable is NOT FOR PUBLIC MODIFICATION.
            __type due to name mangling in python the name of this attribute is now _Tree__type under the hood
        """

    #A getter to fetch the value
    def get_height(self)-> int|float:
        return self._height
    
    #A setter to give the access
    def set_height(self, new_height):
        if 100>new_height>0:
            self._height = new_height#if the condition is true only then setter is initiallizes the value.
    
    #A getter to fetch the value
    def get_type(self)->str:
        return self.__type
    
    #A setter to give the access
    def set_type(self, new_type):
        if new_type:
            self.__type = new_type
    """
        The access modifier can also be applied to methods
    """
    def _protected_method(self)->None:
        print("This is a protected method.")

    def __private_method(self)->None:
        print("This is a private method.")

    def get__private_method(self):
        return self.__private_method()

tree1: object=Tree(type="Pine Tree", height=50)

#Accessing the attributes via name mangling:
print("Type of Tree1 = ",tree1._Tree__type)
#Due to ideology of python's "We are all adults here." Python does not forces us to explicitly use get set methods.


#accessing the attribute of height
print(tree1.get_type())
print(tree1.get_height())

print("Values can be input by:") 

# Increase _height by 5
tree1.set_type("Pepepopo tree")
print(tree1.get_type())
tree1.set_height(89)
print(tree1.get_height())
print()

#If we want to increment the _height by 5
tree1.set_height(int(tree1.get_height()) + 5)
print(tree1.get_height())


print("or for user input")

tree1.set_type(input("Input Tree Type : "))
print(tree1.get_type())
tree1.set_height(int(input("Input Tree height : ")))
print(tree1.get_height())

tree1._protected_method()
tree1._Tree__private_method()
tree1.get__private_method()