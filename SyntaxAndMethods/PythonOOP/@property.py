# Property decorator is used to define a method as a property and it can be accessed as an attribute

# by property we can add additional logic when to read write or delete code 

# @property gives you getter setter or deleter method

class rectangle:

    def __init__(self, width, height):
        self._width=width#set as protected because @property can be used as getter and setters
        self._height=height#set as protected because @property can be used as getter and setters

    @property# this is called to define a getter method
    def width(self):#now width is the property name of this decorator 
        return f"{self._width:.2f}cm"

    @width.setter # @<propertyName>.setter
    def width(self, new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("Width should be positive")

    @width.deleter
    def width(self):
        del self._width
        print("Width Deleted.")

    @property
    def height(self):
        return f"{self._height:.2f}cm"
 

    @height.setter
    def height(self, new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("Height should be positive")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted.")

rectangle1 = rectangle(width=2, height=5)

rectangle1.width = float(input("Enter the new width = "))
print(rectangle1.width)

rectangle1.height = float(input("Enter a new height = "))
print(rectangle1.height)

del rectangle1.width#rectangle1._width i.e the _width attribute of the instance rectange1 has been deleted
del rectangle1.height
