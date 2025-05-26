#Multiple Inheritance = Inherits from more than one parent(base) class 
#Multilevel Inheritance is when a class inherits from a parent(sub-base) class which in herits from another parent (grandparent/base) class

class animal:
    def  __init__(self, name, age=0):
        self.isAlive=True
        self.name=name
        self.__age= int(age)

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is mimimi")
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if self.__age>=0:
            self.__age=new_age
    
    def  display_age(self):
        print(f"{self.name} is {self.__age} yrs old")

class prey(animal):#a parent class inheriting from animal class
    def flee(self):
        print(f"Prey {self.name} is fleeing")
    def eat(self):
        print(f"{self.name} is eating grass")
class predator(animal):#another parent class inheriting from animal class
    def hunt(self):    
        print(f"Predator {self.name} is hunting")
    def eat(self):
        print(f"{self.name} is eating meat.")

#rabbits are prey
class rabbit(prey):
    pass
#and Eagles hunt
class eagle(predator):#Animal->Prey->Eagle
    pass

#but Fishes are Shark(Preadator) and clown fish(Prey) too
#so we use Multiple Inheritance then,
class fish(prey, predator):
    pass

#now fish is the sub-class of both Prey and predator meaning it can use attributes and methods and contructors of both of them
#Here we encounter a diamond problem in which both parent classes have a method of the same name but diffrent behavior.
#Because we did not explicitly mentioned to fish class which eat method to use.Python will follow the mro(method resolution operator) by which the first parent's class will be taken as the method of the child class.
# but it can be solved by user input(if elif), by mro or by super() funtion.
rabbit1 = rabbit("Moonkin")
print(f"{rabbit1.name} is Alive ? {rabbit1.isAlive}.")
rabbit1.eat()#by using multi level in heritance
rabbit1.sleep()
rabbit1.flee()
rabbit1.set_age(input(f"Enter age for {rabbit1.name} : "))
print(rabbit1.get_age())
rabbit1.display_age()
print()

eagle1 = eagle("Sunraku")
print(f"{eagle1.name} is Alive ? {eagle1.isAlive}.")
eagle1.eat()
eagle1.sleep()
eagle1.hunt()
eagle1.set_age(input(f"Enter age for {eagle1.name} : "))
print(eagle1.get_age())
eagle1.display_age()
print()

#fish1 object can do both here
fish1 = fish("Swimmi")
print(f"{fish1.name} is Alive ? {fish1.isAlive}.")
fish1.eat()
fish1.sleep()
fish1.flee()
fish1.hunt()
fish1.set_age(input(f"Enter age for {fish1.name} : "))
print(fish1.get_age())
fish1.display_age()
print(fish.mro())#this checks the method resolution operator,hereby the the <class '__main__.prey'>  has more precedence because it is the first.
