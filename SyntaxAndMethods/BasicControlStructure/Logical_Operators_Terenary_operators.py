#operate operations by boolean algebra
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
elif (temp>= 30 and not is_friends_available):
    print("Its too HOT outside and Your Friends are not available!")
    print("You cannot go to Party")
#inequality comparisions can also be done by
elif (30>temp>10 and is_friends_available and not is_weather_good):
    print("Temp is good and your friends are available but weather is not good !")
    print("You cannot go to party !")

#Conditional Expressions in Python, similar to TERNARY OPERATOR
    #for int/float
a=int(input("Enter a Number:"))
#(f"")is not necessary here only "" is required
even_or_odd = (f"{a} is Even") if a%2==0 else (f"{a} is Odd")#even_or_odd will store this if or else as a string 
print(even_or_odd)
print("Type of even_or_odd is ",type(even_or_odd))
    #string 

user = "admin"
access_level_identifier = "FULL ACCESS" if user=="admin" else "LIMITED ACCESS"
print(access_level_identifier)