"""
Functions in python:
    Functions are a re-usable block of code.
    A function can be called anywhere and at anytime as many times as needed.

    def <function_name>(parameter_1, parameter_2, ...):
        #re-usuable code here
        return variable

    #function call
    <function_name>(arguement1, arguement2, ...)
    
    A function has two requirements: Arguements and return
    SYNTAX:
    
    So there can be four vaild function combinations:
    1. No Arguments(args), No return

        def <function_name>():
        #re-usuable code here

    2. Agruements, No return
    
        def <function_name>(parameter_1, parameter_2, ...):
        #re-usuable code here
        

    3. No arguments, return
    
        def <function_name>():
        #re-usuable code here
        return variable

    4. Arguement, return 

        def <function_name>(parameter_1, parameter_2, ...):
        #re-usuable code here
        return variable
"""

def invoice_display(username, amount, DueDate):#def <function_name>(parameter1, parameter2)
    print(f"Hello {username} !")
    print(f"Your bill is {amount:,.2f} rupees")
    print(f"Bill must be paid before: {DueDate}")
    print()
invoice_display("Harsh", 20154.56,"21/03/25")#feeding the arguements to function

#return = used to send a value back to the caller.
def divide(x, y):
    if y<0:
        print("Invaild value of y")
    else:
        z=x/y
        return z
division_ans=divide(1,2)
print(division_ans) 
print()
#or
print(divide(2,6))