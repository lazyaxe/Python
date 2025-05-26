#Aritmetic Operators (+, -, *, /, **[exponents], % modulus)
#Addition '+'
NumberOfFriends=0
NumberOfFriends = NumberOfFriends + 1
#Addition + , NumberOfFriends => NumberOfFriends + 1
        # is same as (augmented operator)
NumberOfFriends += 1
print(NumberOfFriends)
NumberOfFriends = 10

#Subtraction - , NumberOfFriends=> NumberOfFriends - 1
NumberOfFriends -= 1
print(NumberOfFriends)

#Multiply * 
NumberOfFriends *= 3 #NumberOfFriends= NumberOfFriends*3
print(NumberOfFriends)

NumberOfFriends = 10
#Division / 
NumberOfFriends /= 2
print(NumberOfFriends)

NumberOfFriends=10
#Exponents **
NumberOfFriends = NumberOfFriends**2 #(NumberOfFriends)^2
print(NumberOfFriends)

NumberOfFriends=10
#Moduluo %
Remainder_NumberOfFriends= NumberOfFriends % 2
print(Remainder_NumberOfFriends)

Remainder_NumberOfFriends= NumberOfFriends % 3
print(Remainder_NumberOfFriends)

#Math Functions in Python
x = 3.002548
y = -31
z = 3
round_x = round(x)
print(round_x)
ModOfY= abs(y) # absolute value of x
print(ModOfY)
calculate = pow(2, 3)# calculate 2*2*2 = 16
print("Calculation = ",calculate)
max_find = max(x, y, z)# OR find the maximum value from x, y & z by print(max(x, y, z))
print(max_find)
min_find = min(x, y, z)# OR find the minimum value from x, y, z print(min(x, y, z))
print(min_find)
#works with more than 3 operators also.

import math # importing the math library for more functions(there are more not covered functions)
print(math.pi) #printing value of pi 
math.e# Value of e(exponential constant)
x = 3
result = math.sqrt(x)
print("Square root=",result)
x = 2.99
result = math.ceil(x)#round up the value of x(celing)
print(result)
result = math.floor(x)#round down the value of x(floor)
print(result)


