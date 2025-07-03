#string methods and functions in python
#strings are the default data type for input variable
name=input("Enter your full name: ")#for example "harsh Sharma"
result1=len(name)#returns the number of chars including whitespace(s)
print(result1)
result2=name.find("o")#finds the first instance of a given char in a string, counts from 0, returns  -1  if not found, suports a offset index as second arguement 
print("Result 2 = ",result2)
result3=name.rfind("1")#reversefind, finds the last instance of a given char, return -1 if not found, suports a offset index as second arguement
print(result3)
result4=name.capitalize()#Upper cases the first char of given string
print(result4)
result5=name.upper()#Upper cases all the chars in a string
print(result5)
result6=name.lower()#lower case all the chars in a string
print(result6)
result7=name.isdigit()#returns true only if all the chars in string are nums
print(result7)
result8=name.isalpha()#true only if all chars are alphabetic(inclduing whitespaces) 
print(result8)


inputPhoneNumber=input("Enter a phone number:")
result9 = inputPhoneNumber.count("*")#counts the number of time '-' was used
print(result9)
result10=inputPhoneNumber.replace("-","")#replace phone_number dashes(-) with empty chars
print("Now = ",result10)

#print(help(str))
#more string functions/methods can be found by help(str)