# LOGICAL OPERATORS
"""
~> Logical operators such as 'or', 'and' and 'not' are based on boolean algebra.
~> They can be used in if-elif statements to make conditions more flexible by user-specific demands.

1. and
    if a_condition:
        if another_condition:
            #code

2. or
    if a_condition:
        #code
    elif another_condition:
        #code

3. not
    if a_condition:
        continue # pass
    else:
        #code
"""
temp = 20 
is_weather_good = True
is_friends_available = True
if(temp >= 30 or not is_weather_good):
    print("Either it's HOT or weather is not good")
    print("You cannot go to party")
elif (temp <= 30 and is_weather_good and is_friends_available ):
    print("It is not HOT outside and the weather is good !")
    print("Your Friends are  available!")
    print("Everything checks out !")
    print("You can go to party")
elif (temp >= 30 and not is_friends_available):
    print("Its too HOT outside and Your Friends are not available!")
    print("You cannot go to Party")
elif (30 > temp > 10 and is_friends_available and not is_weather_good):
    print("Temp is good and your friends are available but weather is not good !")
    print("You cannot go to party !")

#Conditional Expressions in Python, similar to TERNARY OPERATOR in other programming languages...
    #for int/float
a = int(input("Enter a Number:"))

even_or_not = (f"{a} is Even") if a % 2 == 0 and a > 0 else (f"{a} is not even")
#even_or_not will store this if or else as a string 
print("Type of even_or_not is ",type(even_or_not))
"""
Equivalent to,

    if a % 2 == 0 and a > 0:
        even_or_not = "is even"
    else:
        even_or_not = "is not even"
"""
print(even_or_not)

user = "admin"
access_level_identifier = "FULL ACCESS" if user == "admin" else "LIMITED ACCESS"
"""
Equivalent to,

    if user == "admin":
        access_level_identifier = "FULL ACCESS"
    else:
        access_level_identifier = "LIMITED ACCESS"
"""
print(access_level_identifier)
