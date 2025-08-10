"""
indexing is the way to access the elements of a string, list, array, tuple etc...
[]=indexing operator
"""

"""
Slicing:
Slicing is a method in Python by which we can extract required data from a string, list, tuple etc...

<name>[start of string:end of string:step of string]
"""
credit_card_number="1212-3264-2184"
print(len(credit_card_number))#14 chars

print(credit_card_number[0])
#prints the first char of string i.e. '1'

print(credit_card_number[0:4])
#prints till the 0th to 4th element i.e. 1212

print(credit_card_number[:4])
#equivalent to credit_card_number[0:4]
#print from the starting char(i.e. credit_card_number[0]) to credit_card_number[4] i.e. 1212

print(credit_card_number[5:])
#this will print from the 5th element to the last element of string i.e. 3264-2184

#Negative indexing
print(credit_card_number[-1])
#this prints the last element i.e. 4

#Step (skip number by a definite pattern)
print(credit_card_number[::2])
#this prints from the 0th element to last element but skips every element of index that is multiple of 2  
#11-2428

#To print the last digits of credit card
last_digits_of_card=credit_card_number[-4:]
#this will print from the last fourth element to the last element
#2184
print(f"XXXX-XXXX-{last_digits_of_card}")

#To reverse the string:
credit_card_number=credit_card_number[::-1]
#This will traverse throught the array but in the reverse order
print(credit_card_number)