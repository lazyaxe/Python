"""
Functions in python:
    ~> Functions are a re-usable block of code.
    ~> A function can be called anywhere and at anytime as many times as needed.
    ~>'def' keyword is used to define a function
"""

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

def invoice_display(user_name, amount, due_date):#def function_name(parameter1, parameter2)
    print(f"Hello {user_name} !")
    print(f"Your bill is {amount:,.2f} rupees")
    print(f"Bill must be paid before: {due_date}")
    print()
invoice_display("Harsh", 20154.56,"21/03/25")#feeding the arguements to function

#return = used to send a value back to the caller.
def divide(x, y):
    if y<0:
        print("Invaild value of y")
    else:
        z=x/y
        return z

#Using a varibale to store the return value
division_ans=divide(1,2)
print(division_ans) 
print()

#or
print(divide(2,6))