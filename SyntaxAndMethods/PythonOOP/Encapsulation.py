#Encapsulation protects your classes from accidental changes or deletions in attributes and promotes code reusability and maintainability.

    #Access Modifiers in Python
        # for protected _MemberName(single underscore), this can be acccessed by base-class and its sub-classes
        # for private __MemberName(double underscore), this can be acccessed by only the base-class
    #if we access the access modified members of this class outside, we get an AtributeError.

    #ways to access the modified members
class Tree:
    def __init__(self, type, height):
        self.__type= type#due to name mangling in python the name of this attribute is now _Tree__type under the hood
        self._height = height # or you can do  self._height = int(height) to avoid type convert in line 42
        #due to being a single underscore naming convention it does not triggers Name Mangling.It is used as a reminder that this variable is NOT FOR PUBLIC MODIFICATION.
    
    #making up a getter to fetch the value
    def get_height(self):
        return self._height
    
    #making up a setter to give the access
    def set_height(self, new_height):
        if 100>new_height>0:
            self._height = new_height#if the condition is true only then setter is initiallizes the value.
    
    #making up a getter to fetch the value
    def get_type(self):
        return self.__type
    
    #making up a setter to give the access
    def set_type(self, new_type):
        if new_type:
            self.__type = new_type

tree1 = Tree("Pine Tree", "50")

print("Type of Tree1 = ",tree1._Tree__type)#Due to ideology of python's "We are all adults here." Python does not forces us to explicitly use get set methods

#accessing the attribute of height
print(tree1.get_type())
print(tree1.get_height())

print("Values can be input by:") 

# Increase height by 5
tree1.set_type("Pepepopo tree")
print(tree1.get_type())
tree1.set_height(89)
print(tree1.get_height())
print()

#If we want to increment the height by 5
tree1.set_height(int(tree1.get_height()) + 5)
print(tree1.get_height())


print("or for user input")

tree1.set_type(input("Input Tree Type : "))
print(tree1.get_type())
tree1.set_height(int(input("Input Tree height : ")))
print(tree1.get_height())