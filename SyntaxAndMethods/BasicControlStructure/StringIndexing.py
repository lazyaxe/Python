#index = acessing elements of a sequence using [], []=indexing operator
#   [start of string:end of string:step of string]

credit_card_number="1212-3264-2184"
print(credit_card_number[0])#prints the first char of string(0-13)
        #1
        
print(credit_card_number[0:4])#prints till the 0th to 4th elements
        #1212

print(credit_card_number[:4])#this will print from the start(0th) to 4th element
        #1212

print(credit_card_number[5:])#this will print from the 5th element to the last element of string
        #3264-2184

#we can also use the negative indexing
print(credit_card_number[-1])#this prints the last element
        #4

#we can also step (skip number by a pattern)
print(credit_card_number[::2])#this prints from the 0th element to last element but only prints every 2nd element
        #11-2428

#to print the last digits of credit card
last_digits_of_card=credit_card_number[-4:]#this will print from the last fourth element to last element
        #2184
print(f"XXXX-XXXX-{last_digits_of_card}")

#reverse the string
credit_card_number=credit_card_number[::-1]
print(credit_card_number)
print("or")
print(credit_card_number[::-1])