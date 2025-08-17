"""
Lambda functions:
    Lambda function in pythons is basically a one line function.
    
    Lambda functions are also called anynoumous functions because they usually do not have a identifier/name.
    
    Main use of lambda function is in Higher order functions(When functions are given in other funcions as arg.)

    Lambda 
    SYNTAX:
        lamba <variable1>, <variable2>, ...:<variable1> <operation> <variable2>.... 

        The operation result is always returned.
"""

add=lambda x,y: x+y
print(add(4,5))

result=lambda x,y: x+y(4,5)

"""
Lambda functions with condition checking:
    Lambda function's condition always require an else statement.
"""

number_checker=lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"
print("Result=", number_checker(4))


compare=lambda x, y: f"{x} is greater than {y}" if x>y else f"{y} is greater than {x}"
print(f"Comparision: {compare(x= int(input("Enter the first number: ")), y= int(input("Enter the second number: ")))}")


string = input("Enter a string: ")
operation = lambda char: char.upper() if char.isalpha() else char
result = ''.join(operation(char) for char in string)
print("String operation:", result)

"""
Lambda function with List Comprehension:
"""

sample_list=[lambda arg=x: arg*10 for x in range(1, 5)]
"""
    This is the creation of a list of lambda functions.
    The functions can be used by calling a list's element...
    "arg=x" in lambda arg=x: arg*10 is a default arg that equals to whatever the value of x was during the for loop. 
    Each sample_list item/element stores a diffenrent value of default arg
"""

print(f"Lambda function at 0th item of the list: {sample_list[0]()}")

counter=0
for i in sample_list:
    print(f"Lambda function at item {counter} of the list: {i()}")
    """
    i is a lamda function, not a literal, so it requires a parenthesis and because it a has a default arg equivalent to: sample_list[0]()
    since no args are given, each sample_list item/element stored a value of default arg.

    sample_list[](0)'s default arg: 1    
    sample_list[](1)'s default arg: 2
    sample_list[](2)'s default arg: 3
    sample_list[](3)'s default arg: 4   
    """
    counter+=1

"""
Lambda with Multiple Statements:

    Lambda functions do not allow multiple statements, however, we can create two lambda functions and then call the other lambda function as a parameter to the first function.
"""
multi_val_operation=lambda x, y:(print("x+y=", x+y), print("x*y=", x*y))
multi_val_operation(x=42, y=5)

"""
Using lambda with map():

The map() function in Python takes in a function and a list as an argument. 
The function is called with a lambda function and a new list is returned which contains all the lambda-modified items returned by that function for each item. 
"""

a_list=[1, 2, 3, 4, 5]
a_list=map(lambda x:x**2, a_list)
a_list=list(a_list)
print(a_list)

string="input string"
string=map(lambda char: char.upper() if char.isalpha() else char, string)
string = ''.join(string)
print(string)

#Example of a higher order function:
numbers:list[int]=[3, 4, 5, 6, 7]

def map_list(lambda_func, list):
    result=[]
    for item in list:
        new_item=lambda_func(item)
        result.append(new_item)
    return result

print(map_list(lambda_func=lambda x: x**3, list=numbers))