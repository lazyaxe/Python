"""
    Inheritance:
    ~> Inheritance is OOP paradigm in which the functionality of a class i.e. it's methods, attributes and constructor(requires super function) can be inherited/transferred to other class(inherrited class)...
    
    ~> The class which does the inheritance is the Parent/(Super/Base) class and the class with inherits is the Child/Sub class.
    
    ~> Inheritance promotes code resuablity as the methods and attributes can be used by other class.
    
    ~> Only the inherrited class can access the protected and private atrributes and methods.

    Types of inherritance:
    1. Simple Inherritance
    2. Multi-level Inherritance
    3. Multiple Inherritance
    4. Hybrid inherritance
    5.Duck Typing(not covered in this file)
"""

#these subclasses inherit from animal class they also inherit the attributes/members getters/setters and constructors too
class Animal:
    def  __init__(self, name:str , age: int=0)->None:
        self.isAlive=True
        self.name=name
        self._age= int(age)

    def eat(self)->None:
        print(f"{self.name} is eating now.")

    def sleep(self)->None:
        print(f"{self.name} is sleeping now.")

    def get_age(self)->None:
        return self._age
    
    def set_age(self, new_age)->None:
        if self._age>=0:
            self._age=new_age
            
    def  display_age(self)->None:
        print(f"{self.name} is {self._age} yrs old")

#1. Simple inheritance:
class Dog(Animal): # class SubClassName(BaseClass)
    def make_sound(self)->None:
        print("Barks...")

dog1 = Dog("Bob")
print(dog1.isAlive)
print(dog1.name)
dog1.eat()
dog1.sleep()
dog1.set_age(input(f"Enter Age of {dog1.name}: "))
print(dog1.get_age())
dog1.display_age()
print()

#2.Heirarchial Inheritance, because now there are more than one child-class...
class Horse(Animal): # class SubClassName(BaseClass)
    def make_sound(self)->None:
        print("Neighs...")


class Donkey(Animal): # class SubClassName(BaseClass)
    def make_sound(self)->None:
        print("Brays...")

#3. Multiple inherritance 
class Mule(Horse, Donkey):
    pass
    """
        ~>Because this class inherits from two classes which have same methods(but different execution i.e. different sound) there would be clash.
        ~>Python resolves this by: Which class is the first argument will overwrite the other class method i.e. Mule will neigh.
    """

#4. Hybrid Inheritance
"""
~> The animal class performing hybrid inheritance which does heirarchial inheritance(Dog, Horse Mule). 
~> Also does Multi-level inheritance with Animal->Horse->Mule.
~> Abomination inherits from an independent class Bug and inherited class Horse 
"""
class Bug:
    def make_sound(self)->None:
        print("Thraxxan noises...")

class Abomination(Bug, Horse):
    pass

horse1 = Horse("Tom", 23)
print(horse1.isAlive)
print(horse1.name)
horse1.eat()
horse1.sleep()
print()

donkey1= Donkey("Jerry", 23)
print(donkey1.isAlive)
print(donkey1.name)
donkey1.eat()
donkey1.sleep()

mule1 =Mule(name="Nibs", age=5)
print(mule1.name)
mule1.make_sound()

a=Abomination(name="A mistake", age=18)
print(a.name)
a.make_sound()
