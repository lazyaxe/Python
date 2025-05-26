#A multi value return function(kinda)
def function_create_name1():
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name:")
    first_name=first_name.lower().capitalize()
    last_name=last_name.lower().capitalize()
    return first_name + " " + last_name# Or return temp_string, where temp_string=first_name + " " + last_name

MyFullName=function_create_name1()
print(f"Is your full name {MyFullName}?")
print()

#with function's arguments
def function_create_name(first_name,last_name):
    first_name=first_name.lower().capitalize()
    last_name=last_name.lower().capitalize()
    return first_name + " " + last_name
print("Function's can have same names in same scope as long as they have different arguments and position")


MyFullName=function_create_name("hARSH","sHARMA")
print(f"Is your full name {MyFullName}?")