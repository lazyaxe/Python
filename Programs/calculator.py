#python calulator program
#for addition multiplication substraction division
import math
print("PYTHON CALCULATOR")
a = float(input("Enter a:"))
b = float(input("Enter b:"))
print("+ or - or * or / ?")
user_response = input()
if (user_response == '+'):
    c = a + b
    print(f"{a}+{b}={c}")
elif(user_response=='-'):
    c= a - b
    print(f"{a} - {b}= {c}")
elif(user_response=='*'):
    c= a * b 
    print(f"{a} * {b}= {c}")
elif(user_response=='/'):
    if(b>0):
        c=a/b
        print(f"{a} / {b}= {c}")
    else:
        print(f"b = {b} was converted to positive")
        b = abs(b)
        c = a/b
        print(f"{a} * {b}= {c}")
else:
    print("ERROR ! CHOOSE FROM : + - * /")