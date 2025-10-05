#Duck Typing is another method to achevive polymorphism besides Inheritance
#It follows the principle "If it looks like a duck, If it quacks like a duck, it must be a duck"

#In order to be duck typed, an object must require attributes

class Animal:
    alive = True
    def __init__(self, speech):
        self.speech = speech

    def speak(self):
        print(self.speech)
class Dog(Animal):
    def __init__(self, speech="Bark!"):
        super().__init__(speech)

    def __str__(self):
        return "Dog"
    
class Cat(Animal):
    def __init__(self, speech="Meow!"):
        super().__init__(speech)

    def __str__(self):
        return "Cat"
    
#now making a non Animal inherited class, Car
class Car:
    alive = False
    def __init__(self , speech="Honk!"):
        self.speech = speech

    def speak(self):
        print(self.speech)

    def __str__(self):
        return "Car"
    #animals list is different from the Animal class
animals: list[object] = [Car(), Cat(), Dog() ]

for animal in animals:
    print(animal.__str__())
    print(animal," = ", animal.alive)
    animal.speak()
    print()