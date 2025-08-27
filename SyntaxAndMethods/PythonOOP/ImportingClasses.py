#An Object is a bundle of methods and functions and variables example: phonebook and book or Student
#A Class is a blueprint of creating a object

from classes_and_objects import car
# or import CLASSexample as CLASS

#creating a object named "car_1"
car_1=car(model="Skibidi", colour="brown", is_car_sale=True)#Initalizing the constructor value using keyword arugments

#printing the attributes
print(car_1.model)
print(car_1.colour)
print(car_1.is_car_sale)

car_2= car("Alto 500", "Red", False)#Initalizing the constructor value

#printing the attributes
print(car_2.model)
print(car_2.colour)
print(car_2.is_car_sale)

#object 1 accesing the class's methods 
car_1.drive()
car_1.stop()
car_1.details()

#object 2 accessing the class's methods
car_2.drive()
car_2.stop()
car_2.details()