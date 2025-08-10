"""
FORMAT SPECIFIERS:
Python string formating is done with the help of f-string.

SYNTAX:
Format specifiers = {value:flags}, 
"""
price1= 3.14579626626565622
price2= -65.322500
price3= 12.32

print(f"Price 1 = {price1:.2f}$")#truncate after 2 floating digits
print(f"Price 2 = {price2:.3f}$")
print(f"Price 3 = {price3:.10f}$")
print()

#to provide whitespace in output
print(f"Price 1 = {price1:10}")#allocate 10 whitespaces for the print(including chars) 
print(f"Price 2 = {price2:10}")
print(f"Price 3 = {price3:10}")
print()

#pre-seed a value with zero
print(f"Print with preseed zero = {price1:010}")
print()

#paragraph allignment
print(f"Price 1 = {price1:<10}")#left - align and allocate 10 spaces for the print(including chars) 
print(f"Price 2 = {price2:>10}")#right align and ""
print(f"Price 3 = {price3:^10}")#center align and ""
print()

#to display + sign
print(f"Price 1 = {price1:+}")#display + sign infront of price1 
print(f"Price 2 = {price2:+}")#it does not apply of negative numbers
print(f"Price 3 = {price3: }")#alternative way of above
print()

#thousands digit separator(,)
price1=166661616
print(f"Price = {price1: ,}")#this separate digits in units, tenths, hundredths etc.....
print()

#mix and match
print(f"Price 1 = {price1:+,}")#display + sign infront of price1 and also seprate them 
print(f"Price 2 = {price2:+,.5f}")#display + sign infront of price2 and separate and and floating point limit till 5th decimal
print(f"Price 3 = {price3:>+10,}")#right allignment display + sign infront of price2 and separate and and allocate space till 10 chars
