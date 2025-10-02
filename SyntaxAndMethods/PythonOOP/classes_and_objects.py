#CLASSES AND OBJECTS:
"""
   ~> A Class is a blueprint to creating a object
   ~> A class is the blueprint of class members/attributes, class functions/methods, constructor and destructor which the object/instance will have.
   ~> An attribute/class members are basically the variables inside the class...

   example: 
    A class/blueprint of a Student might be:
            Their attributes will be:
                their age, grade, roll number, etc...
            Their methods will be:
                study(), go_to_school() etc..
   An Object/Instance is a bundle of attribute and methods which are implimented by classes.
"""
class Car:
    """
        What is a constructor in Python?
            ~> A constructor in Python is a dunder(double underscore) method by which the initialization of the attributes/class members is done directly when creating am instance of the class via arguements...
            ~> Since constructor is just a method. The default args, keyword args, *args, **kwargs can be used... 
            ~> The Constructor can be initialized by:
                def __init__(self): 
                    #assginment here            
            ~> The assignment of the variables to attributes is done inside the constuctor method. 
                By self.attribute=value
    
        What is the self keyword?
            ~> The self parameter is the identifier for the object 
            ~> 'self' keyword is arbitrary and any keyword can be used but 'self' is the norm.
            ~> So, instead of making instance_name.attribute=value for n different instances, the self keyword is only used the class.
            ~> The parameter names don't have to be same as the attribute names...
    """
    def __init__(self, model:str, colour:str="White", is_car_sale:bool=False):
        self.model = model
        self.colour =  colour
        self.is_for_sale = is_car_sale

    #creating a method i.e. a function inside a class
        """
        ~> The methods require self as a parameter only when defining the method.
        ~> The self.attribute_name is used for accessing the value of an attribute...
        """
    def drive(self)->None:
        print(f"You start driving {self.model}.")

    def stop(self)->None:
        print(f"You stopped driving {self.model}")
    
    def details(self)->None:
        print(f"Model = {self.model}")
        print(f"{self.model}'s Colour = {self.colour}")
        print(f"Sale Status = {self.is_for_sale}")

if __name__=='__main__':

    #Creation of an instance/object
    car1: object = Car(model="Ford Mustang")

    car2: object = Car(model="Ford F-150", colour="Black", is_car_sale=True)
    
    #Modifying the class member: 
    car1.colour="Pink"

    #Accessing the values of an object/instance
    print(f"The colour of {car1.model} is {car1.colour}")

    print(f"The colour of {car2.model} is {car2.colour}")

    #Accessing the methods of an object/instance
    car1.drive()
    car1.stop()
    car1.details()

    car1.drive()
    car2.stop()
    car2.details()