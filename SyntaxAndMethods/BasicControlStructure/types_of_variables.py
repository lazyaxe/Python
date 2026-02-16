# Datatypes and variables in Python
"""
~> A variable is a container storing a value that could be a string, integer, float, boolean. Datatype is automatically identified (at run-time)
~> Variables are directly assigned in Python i.e. No declaration only initalization
~> Python can have indentation errors.
~> Semi colons can be used!(but not recommended)
"""
#Stings in Python
firstName = "Harsh"

#f is the f-line|f-string and {variable_name} is the place holder for the variabel
print(f"Hello {firstName}!")

#print function can have single quotes '' or double quotes ""
print(f'single quotes also work {firstName}!')

# Integers/Numeric data-types in Python:

#int datatype
age = 18;
print(f"{firstName} is {age} years old!")

#float datatype: 
float_value = 69.420
print(f"Float = {float_value}")

#boolean, can either be True(1) or False(0):
is_response = True
print(f"Are you a student ? {is_response}.")
is_response = False
print(f"Are you a Teacher? {is_response}.")

#Typecasting is the Process of converting one datatype into another data type
# str() int() float() bool()

#gpa is a float data type
gpa = 5.3 
print(type(age))#checking datatype.

# float=>int typecast
gpa = int(gpa) 
print("now it is ", type(gpa))#checking the type conversion, only type() won't give anything

#int => string typecast
age = str(age)

#check/print the datatype
print(type(age))

#concatenating(joining) strings
#this joins string "1" to string age "28"
age += "1"
print(age)

string = "1"
print("This", string, "also works...")

# converting a string to a bool datatype

#Non-empty string = true, Empty string = false
string = bool(string)

#bool is false when string is empty, it can be used as a empty string detector
print(f"Is the string not empty ? : {string}")