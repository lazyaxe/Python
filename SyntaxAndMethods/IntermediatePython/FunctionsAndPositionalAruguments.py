#Functions in python
'''
    A Function is a re-usable block of code created for conveniance of programmer.
    A Function can be called any where in program, as many times as needed.

    There are 3 parts in making a function in Python:
    1. Declaration
    2. Setting Parameters(if needed)
    3. Return value(if needed)

'''

'''
Declaration of Function

def function_name_here(parameter_var1, parameter_var2, ...):
    # reusable code here

'''
def invoice_display(username, amount, DueDate):
    print(f"Hello {username} !")
    print(f"Your bill is {amount:,.2f} rupees")
    print(f"Bill  must be paid before {DueDate}")
    print()

'''
Calling a function

function_name_here(arguement_var1, arguement_var2)

the order/position in which arguements are passed matters, so these are positional arguements.
'''

invoice_display("Harsh", 20154.56,"21/03/25")#feeding the 3 different arguments to function

'''
There are 4 types of Functions in Python
    1. NO arguements, NO returns

        def function_name_here():
            # reusable code here
    
    2. NO arguements, WITH return

        def function_name_here():
            # reusable code here
            return result

    
    3. WITH arugements, NO return

        def function_name_here(parameter_var1, parameter_var2, ...):
            # reusable code here

    
    4. WITH arguements, WITH return

        def function_name_here(parameter_var1, parameter_var2, ...):
            # reusable code here
            return result
'''
def divide(parameter1, parameter2):
    if parameter2<0:
        print("Invaild value of denomiator")
    else:
        result=parameter1/parameter2    #operation
        return result #sends value of z

x=divide(1,2)
print("x = ",x)
#or
print(divide(2,6))