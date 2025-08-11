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

print(lambda x,y: x+y(4,5))

#Example of a higher order function:
numbers:list[int]=[3, 4, 5, 6, 7]

def map_list(lambda_func, list):
    result=[]
    for item in list:
        new_item=lambda_func(item)
        result.append(new_item)
    return result

print(map_list(lambda_func=lambda x: x**3, list=numbers))