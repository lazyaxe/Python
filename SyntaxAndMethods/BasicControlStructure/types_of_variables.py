#variable = a container storing a value =(string, integer, float, boolean) data type is automatically identified 
# Python has white space indentation errors

#Stings in Python
firstName = "Harsh" #string data type
print(f"Hello {firstName}!")#f is the f-line and {} is the place holder
print(f'single quotes also work {firstName}!')

# Integer in Python
#it shouldn't be in quotes 
age = 18;#semi colons can be used!
print(f"{firstName} is {age} years old!")

#float in python 
float_value=69.420
print(f"Float = {float_value}")

#boolean = True(1) or false(0)
is_response = True
print(f"Are you a student ? {is_response}.")
is_response = False
print(f"Are you a Teacher? {is_response}.")

#Typecasting is the Process of converting one datatype into another data type
# str() int() float() bool()
gpa = 5.3 # gpa is a float data type
#to know the data type of gpa
gpa = int(gpa) # float=>int typecast
print("now it is ", type(gpa))#checking the type conversion, only type() won't give anything
print(f"GPA is now {gpa}")
age = str(age)
print(type(age))#check
print(f"{age} is now a string")
 #concatenating(joining) strings
age += "1"#this joins string "1" to string age "28"
print(age)
# converting a string to a bool datatype
string = "1"
print(f"This", string, "also works...")
string = bool(string)
print("Alternative way to use print ", string)#bool is false when string is empty, it is used as a empty string detector
print(f"is string non-empty ? {string}")