#Duck Typing is another method to achevive polymorphism besides Inheritance
#It follows the principle "If it looks like a duck, If it quacks like a duck, it must be a duck"

#In order to be duck typed an object must required attributes

class Animal:
    def __init__(self, speech):
        self.alive = True
        self.speech = speech
    def speak(self):
        print(self.speech)
class dog(Animal):
    def __init__(self, speech="Bark!"):
        super().__init__(speech)

    def __str__(self):
        return "Dog"
    
class cat(Animal):
    def __init__(self, speech="Meow!"):
        super().__init__(speech)

    def __str__(self):
        return "Cat"
    
#now making a non-inherited class, car
class car:
    alive = False
    def __init__(self, speech="Honk!"):
        self.speech = speech

    def speak(self):
        print(self.speech)

    def __str__(self):
        return "MF Car"
animals = [car(), cat(), dog() ]#animals list is different from the Animal class

for animal in animals:
    print(animal," = ",animal.alive)
    animal.speak()
    print()