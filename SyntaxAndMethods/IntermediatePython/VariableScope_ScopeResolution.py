#Variable scope = where a variable is visible and accessible
#variables can share the same name as long as they are in different scope 
#Scope resolution follows (L->E->G->B) Local->Enclosed->Global->Built-in

def function1():
    a=1 #local to function1()
    print(a)
def function2():
    a=2 #local to funtion2
    print(a)

function1()
function2()
print()

print("For Nested functions:(Enclosed scope)")
#Scope resolution order (L->EGB)
#Definition: An enclosed variable is a variable that is defined in the scope of an outer (enclosing) function and is then referenced by an inner (nested) function
def function3():
    a=1 #local to function1()
    print("The O.G Value = ",a)
    def function4():
        a=2 #local to funtion2, there was no 'a' in func2 then we would use the enclosed 'a' of func1 Variable scope
        print("The Nested function's value = ",a)
    function4()#calling the inner function, inside function3
    print("The Final Value = ",a)
function3()
print()

print("for Global Scope(LE->GB)")
print("If no local variables are found, then global variable(s) are used:")
def function5():
    print(a)
def function6():
    print(a)
a=3
function5()
function6()
print()

print("If enclosed variables are found, then they are used:")
def function7():
    a=1
    print(a)
def function8():
    a=2
    print(a)
a=3
function7()
function8()
print()

print("For built-in variables")
from math import e
print("before any local initiallization: ",e)
print("If no local variables are found, then global variable(s) are used:")
e=3  
print("after a local initiallization ",e)
print()