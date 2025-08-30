"""
   A Class is a blueprint to creating a object
   A class has class members/attributes, class functions/methods, constructor and destructor...which the object/instance will have.
   An attribute/A class members are basically the variables inside the class...

   example: A class/blueprint of a Student might be:
            Attributes/class
                Their age, grade, roll number, etc...
            Their methods will be study(), go_to_school() etc..
   An Object/Instance is a bundle of methods and functions and class members which are implimented by classes 
"""
class Car:
    def __init__(self, model:str, colour:str="White", is_car_sale:bool=True):
        """
            What is a constructor in python?
            ~> A constructor in Python is a dunder(double underscore) method by which the initialization of the attributes/class members is done directly when creating am instance of the class via arguements...
            
            ~>Since constructor is just a method i.e. A function inside a class default, keyword, *args, **kwargs can be used... 
            
            ~>The assignment of the values to attributes is done inside the constuctor method. 
              By self.attribute=value
            
            ~> The self parameter is the identifier for the object 

            ~> 'self' keyword is arbitrary and any keyword can be used but 'self' is the norm.

            ~> So, instead of making instance_name.attribute=value for n different instances, the self keyword is only used the class.
            ~>The parameter names don't have to be same as the attribute names...
        """
        self.model = model
        self.colour =  colour
        self.is_for_sale = is_car_sale

    #creating methods (functions inside a class)
    def drive(self)->None:
        """
            ~> The methods require self as a parameter only when defining the method.
            ~> The self.attribute_name is used for accessing the value of an attribute...
        """
        print(f"You start driving {self.model}.")
    def stop(self)->None:
        print(f"You stopped driving {self.model}")
    def details(self)->None:
        print(f"Model = {self.model}")
        print(f"{self.model}'s Colour = {self.colour}")
        print(f"Sale Status = {self.is_for_sale}")

if __name__=='__main__':
    """
    Creation of an instance/object
    """
    car1: object=Car(model="Ford Mustang")

    car2: object= Car(model="Ford F-150", colour="Black", is_car_sale=True)
    """
    Accessing the values of an object/instance
    SYNTAX: 
        instance_name.attribute
    """
    car1.colour="Pink"
    print(f"The colour of {car1.model} is {car1.colour}")

    print(f"The colour of {car2.model} is {car2.colour}")

    """
    Accessing the methods of an object/instance
    SYNTAX: 
        instance_name.method()
    """
    car1.drive()
    car2.stop()
    car1.details()