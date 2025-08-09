"""
For Input data we use input() registers entered data as a string known as 'str' data type .
"""

name=input("What is your name: ")
age=input("Age = ")
# age will be returned as a string, we can't do arithmetic operations on a string
print("Type of age variable:", type(age))

#so we need to type cast age
age = int(age)
birth_year = 2025 - age
print(f"{name}, your birth year is {birth_year}")

# we can also type cast directly by:   
sample1 = int(input("Input a int:"))#input string will be typecasted into a int semi-automatically
print(f"{name}, sample1 will now store data of",type(sample1))

input("What is your name ? = ")
#This does not store any value in the variable, but it works...