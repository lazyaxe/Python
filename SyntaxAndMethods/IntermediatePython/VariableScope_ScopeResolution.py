# VARIABLE SCOPE IN Python:
"""
    ~> Variable scope is a field where a variable is visible/accessible or not.
    ~> Variables can have the same name as long as they are in different scope.

Scope resolution follows (L->E->G->B) Local -> Enclosed -> Global -> Built-in
"""

#1. Local Scope: Scope resolution order is (->LEGB)
def function1():
    a = 1 #local to function1()
    print("Function 1's a = ", a)

def function2():
    a = 2 #local to funtion2
    print("Function 2's a = ", a)

#Both function1 and function2 have different value of a same named variable.
function1()
function2()

print()

#2. Enclosed Scope: Scope resolution order is (L->EGB)
"""
Definition: An enclosed variable is a variable that is defined in the scope of an outer (enclosing) function and is then referenced by an inner (nested) function.
"""
print("For Nested functions:(Enclosed scope)")

def function3():
    a = 1 #local to function3
    def function4():
        #if there was no 'a' in function 4 then mro would use the enclosed 'a' of function 3's 'a' variable
        a = 2 #local to funtion 4
        print("Function 4's a = ", a)
    def function5():
        #if there is no 'a' in function5 then mro would use the enclosed 'a' of function3's 'a' variable
        print("Function 5's a = ", a)
    function4()#calling the inner function, inside function3
    function5()
    print("Function 3's a = ", a)

function3()

print()

#3. Global Scope: Scope resolution order is (LE->GB)
print("If no local variables are found, then global variable(s) are used:")

def function5():
    print("Function 5: ", a)
def function6():
    print("Function 6: ", a)

a = 3

#In both functions calls, a = 3 would be used
function5()
function6()
print()

#4. built-in variables: Scope resolution order is (LEG->B)
#built-in variables are varibles that are already in Python, or in Python's modules...
from math import e

print("For built-in variables")

print("before any local initiallization: ", e)

print("If no local variables are found, then global variable(s) are used:")

e = 3

print("after a local initiallization ", e)
print()