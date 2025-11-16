# LAMBDA FUNCTIONS IN PYTHON:
"""
    ~> Lambda function in Python is basically a one line function.
    ~> The lambda function always returns the value.
    ~> Lambda functions are also called anynoumous functions because they usually do not have a identifier/name.
    ~> So, they usally used as an one-time-function.
    ~> If you want to recall a lambda function, initialize it with a name. Now the lamba function can be called as a regular function
    ~> Main use of lambda function is in Higher order functions(When functions are given in other funcions as arg.)
    ~> Lambda functions support name-rebinding which is similar to overriding.
    SYNTAX for an anynomous lambda function:
        lambda <parameter1>, <parameter2>, ...<parameter_N>: <parameter1> <operation> <parameter2>....<parameter_N>(argument_1, argument_2, ... argument_N)

    SYNTAX for defining a lambda function:
        #defining the lamda function
        function_name = lambda <parameter1>, <parameter2>, ...<parameter_N>: <parameter1> <operation> <parameter2>....<parameter_N>

        #calling the function
        function_name(argument_1, argument_2, ... argument_N)
    
"""

#Using lambda function as an anynomous funtion:
print("result", lambda x, y: x + y(4, 5))

#storing the lamda function:
add = lambda x, y: x + y
print(add(4, 5))

#LAMDA FUNCTIONS W/ CONDITIONS:
"""   
    ~> Lambda function's condition always require an else statement
    ~> elif are not allowed here
"""

compare = lambda x, y: (f"{x} is greater than {y}") if x > y else (f"{y} is greater than {x}")

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

print(f"Comparision: {compare(x = num_1, y = num_2)}")

#Nested if else chain:

number_checker = lambda x : (f"{x} is a positive integer") if x > 0 else (f"{x} is a negative integer") if x < 0 else ("Zero")
print("Result = ", number_checker(4))
'''
EQUIVALENT TO:
    def number_checker(x):
        if x > 0:
            return f"{x} is a positive integer"
        else:
            if x < 0:
                return f"{x} is a negative integer" 
            else: 
                return "Zero"

print("Result = ", number_checker(4))
'''

#STRING OPERATIONS IN LAMBDA FUNCTIONS:
string = input("Enter a string : ")

upper_case_operation = lambda char : char.upper() if char.isalpha() else char

result = ''.join(upper_case_operation(char) for char in string)

print("String operation:", result)
"""
EQUIVALENT TO:
    string = input("Enter a string: ")

    def upper_case_operation(char):
        if char.isalpha():
            return char.upper()
        else:
            return char

    result = ''

    for char in string:
        ''.join(upper_case_operation(char)
"""


#USING LAMBDA FUNCTIONS IN LIST COMPREHENSIONS:

list_of_lamda_function = [lambda arg = x : arg * 10 for x in range(1, 5)]
"""
NOTE:
    ~> This is a list of lambda functions [lambda arg = 1 : arg * 10, lambda arg = 2 : arg * 10, lambda arg = 3 : arg * 10, lambda arg = 4 : arg * 10]
    ~> The functions can be used by calling a list's element...
    ~> "arg = x" in lambda arg = x : arg * 10 is a default arg that equals to whatever the value of x was during the for loop. 
    ~> This can be confirmed by calling function: sample list[index_number](integer)
    ~> Each list_of_lamda_function item/element stores a different value of default arg due to i being incremented by the for loop.
"""

print(f"Lambda function at 0th item of the list: {list_of_lamda_function[0]()}")

counter = 0
for lamda_function in list_of_lamda_function:
    print(f"Lambda function at index {counter} of the list: {lamda_function()}")
    counter += 1

    """
    ~> list_of_lamda_function is a list of lambda functions.
    ~> lambda_function is not a literal, so it requires a parenthesis and because it a has a default arg equivalent to: list_of_lamda_function[0]()
    ~> since no args are given, each list_of_lamda_function item/element stored a value of default arg.

    list_of_lamda_function[0]()'s default arg: 1 -> 1 * 10
    list_of_lamda_function[1]()'s default arg: 2 -> 2 * 10
    list_of_lamda_function[2]()'s default arg: 3 -> 3 * 10
    list_of_lamda_function[3]()'s default arg: 4 -> 4 * 10
    """

#EXECUTING MULTIPLE STATEMENTS IN LAMBDA FUNCTIONS:
"""
    ~> Lambda functions does typically not allow execution of multiple statements, however, we can do as many operations as we want as long as they are parenthesis.
"""
multi_val_operation = lambda x, y : (print("x + y = ", x + y), print("x - y = ", x - y), print("x * y = ", x * y, print("x / y = ", x / y)))

multi_val_operation(x = 42, y = 5)

#USING LAMDA FUNCTION W/ map():
"""
    ~> The map() function in Python takes in a function and a iterable as an argument. 
    ~> A map function is an iterator that vectorizes each element in the iterable i.e. list here and aplies the given function on each element without the need of a loop and returns a map object 
    ~> Here we use map to apply a lambda function to each element w/out looping/iterating over it.

    map(function, iterable) -> map_object
"""

a_list = [1, 2, 3, 4, 5]
mapped_object = map(lambda x : x ** 2, a_list)

#Now, type cast from map-object to list
a_list = list(mapped_object) 

print(a_list)

string = "input string"
string = (map(lambda char : char.upper() if char.isalpha() else char, string))
string = ''.join(string)
print(string)

#USING LAMDA FUNCTIONS IN HIGHER ORDER FUNCTIONS:
numbers = [3, 4, 5, 6, 7]

#Let's the make a DIY map function:
map_list = lambda function, input_list : [function(item) for item in input_list]

print(map_list(function = lambda x: x ** 3, input_list = numbers))

#EQUIVALENT TO: 
def map_list(function, input_list):
    result = [] #could be any iterable(list, string, tuple, dict) etc...
    for item in input_list:
        result.append(function(item))
    return result

print(map_list(function = lambda x : x ** 3, input_list = numbers))