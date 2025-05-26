# For Input data we use input() registers entered data as a string known as 'str' data type to make use of data we need to type cast it into a desired data type.

name=input("What is your name: ")
age=input("Age = ")

#this also works if you, don't want to store/access the user input anymore
input("What is your name ? = ")

# age will be returned as a string, we can't do arithmetic operations on a string
#so we need to type cast age
age = int(age)
birth_year = 2025 - age
print(f"{name}, your birth year is {birth_year}")
# we can also type cast by :   
sample1 = int(input("Is this more readable, 1 or 0 ?"))#input string will be typecasted into a int semi-automatically
print(f"{name}, sample1 will now store data of",type(sample1))