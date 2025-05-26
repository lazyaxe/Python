#decorator is a function that extends/adds a behavior of a function without modifying the base function.

#How? Pass the base function as an argument to the decorator.

# How to make a decorator? 

#def add_sprinkles(function_name):
#    def wrapper():
#        return function_name

def add_sprinkles(function_name):# add_sprinkles is now a decorator

    def wrapper(*args, **kwargs):# *args and **kwargs are added to accept any amount/type of argument that the base function i.e. ice_cream might have
        print("You've added sprinkles to your Ice cream!")
        function_name(*args, **kwargs)
    return wrapper

def add_fudge(function_name):# add_fudge is now a decorator
    
    def wrapper(*args, **kwargs):
        print("You've added fudge!")
        function_name(*args, **kwargs)
    return wrapper

def add_whipped_cream(function_name):# add_fudge is now a decorator
    
    def wrapper(*args, **kwargs):
        print("Whipped cream added!")
        function_name(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def ice_cream(flavour="Vanilla"):
    print(f"Here's your {flavour} Ice cream! 🍦")

ice_cream = add_whipped_cream(ice_cream)
ice_cream(flavour="Strawberry")#Calling the function in main
#Alternative of @add_whipped_cream