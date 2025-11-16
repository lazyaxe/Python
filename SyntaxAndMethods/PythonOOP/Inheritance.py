#Inheritance in Python:
"""
    What is Inheritance?
    ~> Inheritance is OOP paradigm in which the functionality of a class i.e. it's methods, attributes and constructor(requires super function) can be inherited/transferred to other class(inherrited class)...
    
    ~> The class which does the inheritance is the Parent/(Super/Base) class and the class with inherits is the Child/Sub class.
    
    ~> Inheritance promotes code resuablity as the methods and attributes can be used by other class.
    
    ~> Only the inherrited class can access the protected atrributes and methods.

    Types of inherritance:
    1. Simple Inherritance
    2. Heirarchial Inheritance
    3. Multi-level Inherritance
    4. Multiple Inherritance
    5. Hybrid inherritance
"""

#Sub-classes that inherit from Animal class also inherit its attributes/members, methods and constructor too
class Animal:
    def  __init__(self, name: str , age: int = 0) -> None:
        self.isAlive = True
        self.name = name
        self._age = age

    def eat(self) -> None:
        print(f"{self.name} is eating now.")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping now.")

    def get_age(self) -> int:
        return self._age
    
    def set_age(self, new_age) -> None:
        if self._age >= 0:
            self._age = new_age
            
    def  display_age(self) -> None:
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

#2.Heirarchial Inheritance
#When more than one class inherrit from the same parent class.

#Horse Class also inherits Animal Class 
class Horse(Animal):
    def make_sound(self)->None:
        print("Neighs...")

horse1 = Horse("Tom", 23)
print(horse1.isAlive)
print(horse1.name)
horse1.eat()
horse1.sleep()
print()

#Donkey Class also inherits Animal Class 
#So Animal class is the base class of 3 classes.
class Donkey(Animal):
    def make_sound(self)->None:
        print("Brays...")

donkey1 = Donkey("Jerry", 23)
print(donkey1.isAlive)
print(donkey1.name)
donkey1.eat()
donkey1.sleep()

#3. Multiple inherritance 
"""
    ~> When a class inherits from two different classes which have same methods(but different execution i.e. different make_sound method) there would be a clash of which class's method should be used.
    ~> This known as the "Diamond Problem".
    ~> Python resolves Diamond Problem by: "The class which is the first argument will override the other class method of the same method name" i.e. Mule will "Neigh" not "Bray"...
"""
class Mule(Horse, Donkey):
    pass

mule1 = Mule(name = "Terry", age = 5)
print(mule1.name)
mule1.make_sound()

#4. Hybrid Inheritance
"""
~> The animal class performing hybrid inheritance which does heirarchial inheritance(Dog, Horse Mule). 
~> Also does Multi-level inheritance with Animal->Horse->Mule.
~> Abomination inherits from an independent class Insect and inherited class Horse 
"""
class Insect:
    def make_sound(self) -> None:
        print("Thraxxan noises...")

class Abomination(Insect, Horse):
    pass

a = Abomination(name = "A mistake", age = 18)
print(a.name)
a.make_sound()
