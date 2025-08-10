"""
String methods and functions in Python:
len()
find()
"""

name=input("Enter your full name: ")#for example "harsh Sharma"

result1=len(name)#returns the number of chars including whitespace(s), i.e. 12 for "harsh Sharma".
print(result1)

result2=name.find("o")
"""
Finds the first instance/usage of a given char in a string, counts from 0, returns -1 if not found, suports a offset index as second arguement.

For example, name="harsh Sharma"
The find will start the finding of char 'o' from left to right. 
Since there is no 'o' in the string, find() will return a -1.

It also supports a start index and a stop index .i.e. from which index to start looking and from which index to stop.
"""
print("Result 2 = ",result2)

result3=name.rfind("1")
"""
Finds the last instance/usage of a given char in a string, counts from 0, returns -1 if not found, suports a offset index as second arguement.

For example, name="harsh Sharma"
The rfind() will start the finding of char 'o' from right to left. 
Since there is no 'o' in the string, rfind() will return a -1.

It also supports a start index and a stop index .i.e. from which index to start looking and from which index to stop.
"""
print(result3)

result4=name.capitalize()#Upper cases the first char of given string
print(result4)

result5=name.upper()#Upper cases all the chars in a string
print(result5)

result6=name.lower()#lower case all the chars in a string
print(result6)

result7=name.isdigit()
#isdigit() returns true only if all the chars in string are nums
print(result7)

result8=name.isalpha()
#isalpha() returns true only if all chars are alphabetic(inclduing whitespaces) 
print(result8)

#count() method
inputPhoneNumber=input("Enter a phone number:")#for example 9898-565-565

result9 = inputPhoneNumber.count("-")
"""
count() method counts the number of times '-' was used, i.e. 2 times.

It also supports a start index and a stop index .i.e. from which index to start counting and from which index to stop.
"""
print(result9)

result10=inputPhoneNumber.replace("-","")
"""
The replace() method here, replaces dashes(-) with empty chars. i.e. 9898-565-565 --> 9898565565
"""
print("Now = ",result10)

print(inputPhoneNumber.replace(""," (._.) ", count=1))
"""
replace() method also has a 'count' arguement.

Determines how many times will the replacement is happening i.e. if count=1 then 9898-565-565-->9898-565565.
"""


"""
print(help(str))
more string functions/methods can be found by help(str)
"""