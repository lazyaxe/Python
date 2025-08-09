"""
A variable is a container storing a value =(string, integer, float, boolean) data type is automatically identified 
Python can have indentation errors.
"""
#Stings in Python
firstName = "Harsh" #string data type
print(f"Hello {firstName}!")#f is the f-line|f-string and {} is the place holder
print(f'single quotes also work {firstName}!')

# Integers/Numeric data-types in Python:

#int datatype
age = 18;#semi colons can be used!(but not recommended)

print(f"{firstName} is {age} years old!")

#float datatype: 
float_value=69.420
print(f"Float = {float_value}")

#boolean, can either be True(1) or False(0):
is_response = True
print(f"Are you a student ? {is_response}.")
is_response = False
print(f"Are you a Teacher? {is_response}.")

#Typecasting is the Process of converting one datatype into another data type
# str() int() float() bool()

gpa = 5.3 
"""
gpa is a float data type
"""
print(type(age))#checking datatype.

# float=>int typecast
gpa = int(gpa) 
print("now it is ", type(gpa))#checking the type conversion, only type() won't give anything

age = str(age)
print(type(age))#check

 #concatenating(joining) strings
age += "1"#this joins string "1" to string age "28"
print(age)

# converting a string to a bool datatype
string = "1"
print(f"This", string, "also works...")

string = bool(string)#Non-empty string =True, Empty string=False
#bool is false when string is empty, it can be used as a empty string detector
print(f"is string non-empty ? {string}")