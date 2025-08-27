class car:
    #to create a constructor(dunder method) in py
    def __init__(self, model, colour, is_car_sale):
        #to include the object itself in the constructor as name 'self'.
        #we need self to access other attributes(parameter for the constructor function) or its members
        #self.attribute_name = recived_attribute
        self.model = model
        self.colour =  colour
        self.is_car_sale = is_car_sale
    #creating functions inside a class
    def drive(self):
        print(f"You start driving {self.model}.")
    def stop(self):
        print(f"You stopped driving {self.model}")
    def details(self):
        print(f"Model {self.model}")
        print(f"{self.model}'s Colour = {self.colour}")
        print(f"Sale Status = {self.is_car_sale}")