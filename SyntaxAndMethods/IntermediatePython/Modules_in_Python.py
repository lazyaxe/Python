#Modules is a file that you want to include in your program
# To include a module use 'import'(a bulit-in one or your own)
#Modules are useful for breaking up a large program into resusable separate files

    #Different methods of import 

#import math # (recommended)
#print(math.pi)

import math as m # 'math' has now alias of 'm'.
print(m.pi)
from math import e #not recommended in general
print(e)

#to create a module, make a new file in python:
#file has to be in same folder
#terminial has to be at same directory(file), SAME FOLDER
import testing_module as example #testing_module has a alias of 'example' 
    # now recalling its defined functions inside this module 
print(example.square_root(256))
print(example.cube_root(8))
print(example.circumference(1))
print(example.π)

#from testing_module import π as pi ,THIS DOES NOT WORK
#print(example.pi)
