#A sub class(child class) that inherits certain attributes and constructors from a base-class(parent class)


class animal:
    def  __init__(self, name, age=0):
        self.isAlive=True
        self.name=name
        self._age= int(age)

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is mimimi")

    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if self._age>=0:
            self._age=new_age
            
    def  display_age(self):
        print(f"{self.name} is {self._age} yrs old")

class dog(animal): # class SubClassName(BaseClass)
    pass

class cat(animal): # class SubClassName(BaseClass)
    pass

class mouse(animal): # class SubClassName(BaseClass)
    pass

#these subclasses inherit from animal class they also inherit the attributes/members getters/setters and constructors too
dog1 = dog("Bob")
print(dog1.isAlive)
print(dog1.name)
dog1.eat()
dog1.sleep()
dog1.set_age(input(f"Enter Age of {dog1.name}: "))
print(dog1.get_age())
dog1.display_age()
print()

cat1 = cat("Tom", 23)
print(cat1.isAlive)
print(cat1.name)
cat1.eat()
cat1.sleep()
print()

mouse1= mouse("Jerry", 23)
print(mouse1.isAlive)
print(mouse1.name)
mouse1.eat()
mouse1.sleep()

#in explanation of Multiple Inheritance in short:
# animal class-->(prey, predator)-->(dog, cat, mouse)