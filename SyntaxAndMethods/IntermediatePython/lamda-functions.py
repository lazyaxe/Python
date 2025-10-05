"""
Lambda functions:
    ~>Lambda function in pythons is basically a one line function.
    ~>The lambda function always returns the value
    ~>Lambda functions are also called anynoumous functions because they usually do not have a identifier/name.
    ~>So, they usally used as an one-time-call-function.
    ~>If you want to recall a lambda function, you should initialize it with a name. Now the lamba function can be called as a regular function
    ~>Main use of lambda function is in Higher order functions(When functions are given in other funcions as arg.)

    SYNTAX:
        lamba <variable1>, <variable2>, ...: <variable1> <operation> <variable2>.... 
"""

add=lambda x,y: x+y
print(add(4,5))

result=lambda x,y: x+y(4,5)

#Lambda functions with condition checking:
"""   Lambda function's condition always require an else statement."""

compare=lambda x, y: f"{x} is greater than {y}" if x>y else f"{y} is greater than {x}"
print(f"Comparision: {compare(x= int(input("Enter the first number: ")), y= int(input("Enter the second number: ")))}")

#Nested if else chain
number_checker=lambda x: f"{x} is a positive integer" if x>0 else f"{x} is a negative integer" if x<0 else "Zero"
print("Result=", number_checker(4))
'''
EQUIVALENT TO:
    def number_checker(x):
        if x>0:
            return f"{x} is a positive integer"
        else:
            if x<0:
                f"{x} is a negative integer" 
            else "Zero"

print("Result=", number_checker(4))
'''

#String operations 
string = input("Enter a string: ")
upper_operation = lambda char: char.upper() if char.isalpha() else char
upper_result= ''.join(upper_operation(char) for char in string)
print("String operation:", upper_result)

#Using lambda function in list Comprehension:
"""
    ~>The functions can be used by calling a list's element...
    "arg=x" in lambda arg=x: arg*10 is a default arg that equals to whatever the value of x was during the for loop. 
    Each sample_list item/element stores a different value of default arg
"""

sample_list=[lambda arg=x: arg*10 for x in range(1, 5)]

print(f"Lambda function at 0th item of the list: {sample_list[0]()}")

counter=0
for lamda_function in sample_list:
    """
        ~> sample_list is a list of lambda functions.
        ~>lambda_function is not a literal, so it requires a parenthesis and because it a has a default arg equivalent to: sample_list[0]()
        ~> since no args are given, each sample_list item/element stored a value of default arg.

    sample_list[0]()'s default arg: 1    
    sample_list[1]()'s default arg: 2
    sample_list[2]()'s default arg: 3
    sample_list[3]()'s default arg: 4   
    """
    print(f"Lambda function at item {counter} of the list: {lamda_function()}")
    counter+=1

"""
Lambda with Multiple Statements:

    ~>Lambda functions do not allow execution of multiple statements, however, we can create two lambda functions and then call the other lambda function as a parameter to the first function.
"""
multi_val_operation=lambda x, y:(print("x+y=", x+y), print("x*y=", x*y))
multi_val_operation(x=42, y=5)

"""
Using lambda with map():

    ~>The map() function in Python takes in a function and a iterable as an argument. 
    ~>A map function is an iterator that vectorizes each element in the iterable i.e. list here and aplies the given function on each element without the need of a loop and returns a map object 
"""

a_list=[1, 2, 3, 4, 5]
a_list=map(lambda x:x**2, a_list)
a_list=list(a_list) #type cast from map-object to list
print(a_list)

string="input string"
string=map(lambda char: char.upper() if char.isalpha() else char, string)
string = ''.join(string)
print(string)

#Using lambda in a higher order function:
numbers:list[int]=[3, 4, 5, 6, 7]

#Let's the make a DIY map function
def map_list(function, input_list):
    result=[] #could be any iterable(list, string, tuple, dict) etc...
    for item in input_list:
        new_item=function(item)
        result.append(new_item)
    return result

print(map_list(function=lambda x: x**3, input_list=numbers))