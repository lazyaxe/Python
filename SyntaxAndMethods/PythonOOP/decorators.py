"""
What is a decorator:
~> In Python, decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code.

~> A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.

~> Decorators can be:
    1. used alone as functions i.e. @function_decorator 
    2. used for classes i.e. @class_decorator
    3. or used for methods i.e. @method_decorator

~> Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

~>The decorator function/method takes the function which functionality needs to be modified as a argument. 

~> Many times the wrapper method has *args and **kwargs to accept any number of arguments.

SYNTAX:
def decorator(function_name):
    def wrapper(*args, **kwargs):
        return function_name

@decorator//function decorator
def function()
    pass
    
@decorator//class decorator
class C:
    pass
    
    @decorator//method deorator (not so common)
    def method()
        pass
"""

"""
EXAMPLE:
Evaluation of time for execution of a function
by start time - ending time.
"""
from time import time, sleep
from unittest import result

start_time=time()
def print_number()->None:
    sleep(2)#delayed execution
    print(69)

print_number()
print(f"print_number {time()-start_time}")


"""
This is a not an efficient method since every function would it's own difference time thingy.

We can use the two ways to generalize it:
    1. Make a timer function 
    2. Use decorators
"""
def timer(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        print(f"{function.__name__} took {time() - start_time:.2f}s")
        return result
    return wrapper

"""
1. Timer function 
"""
print_number = timer(function=print_number)
"""
Explaination: 
~>print_number is the function object not a function, kind of a reference to the function.
~>the print_number object now references to timer(print_number) which has argument of print_number
~> Now the timer(print_number) is executed and the the return value wrapper is passed to print_number object
~>*args, **kwargs arguments of wrapper may seem useless because, there are no arguments in print_number. But *args, **kwargs are just for a safety case here, they will be ignored.
~>Now print_number references to wrapper(*args, **kwargs).
~> so in the end, 
print_number()=wrapper():
                start_time = time()
                result = function()
                print(f"{function.__name__} took {time() - start_time:.2f}s")
                return result

~>Now we have successfully "re-defined/modified" the print_number() function to also measure the time. 

What about the wrapper function: 
~> Because we didn't "call" the wrapper function, it we just returned the function's reference to print_number
"""
print_number()

"""
2. timer decorator

This is just syntactic sugar the interpreter converts this @decorator to function=decorator(function)
"""
@timer
def print_num()->None:
    sleep(2)
    print(420)

print_num()

"""
Example 2: displaying the arguments passed in a function
"""
def args_info(function):
    def wrapper(*args, **kwargs):
        result=function(*args, **kwargs)#greet(*name, greeting)
        print(f"{function.__name__}:")
        print("Args used: ", args)#because args are basically a list of arguments...
        print("kwargs used ", kwargs)#because kwargs are basically a dict of arguments
        return result
    return wrapper

@timer
@args_info
def greet(*name, greeting):
    sleep(2)
    full_name=""
    for word in name:
        full_name=full_name + " " + word
    return f"{greeting}{full_name}"

"""
The @args_info is executed first because it's like inverted stack.

It's functionally equivalent to: 

greet=timer(args_info(function=greet))
"""
print(greet("Harsh", "Sharma", greeting="Hello"))