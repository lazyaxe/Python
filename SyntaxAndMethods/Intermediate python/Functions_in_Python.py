#Functions in python
def invoice_display(username, amount, DueDate):#def function_name("parameter1",parameter2)
    print(f"Hello {username} !")
    print(f"Your bill is {amount:,.2f} rupees")
    print(f"Bill  must be paid before {DueDate}")
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