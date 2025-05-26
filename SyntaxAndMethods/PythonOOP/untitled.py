class animal:
    def __init__(self, name, age=1):
        self.name=name
        self.age=age
    def eat(self):
        print(f"{self.name} is eating something.")
    def sleeping(self):
        print(f"{self.name} is sleeping.")
class prey(animal):
    def flee(self):
        print(f"{self.name} has flee away.")
    def eat(self):
        print(f"{self.name} is eating grass.")
class predator(animal):
    def hunt(self):
        print(f"{self.name} is hunting.")
    def eat(self):
        print(f"{self.name} is eating meat.")
class Tiger(predator):
    pass
class Cow(prey):
    pass
class fish(prey, predator):
    pass
animal1=fish(name="Nemo")
animal1.eat()
