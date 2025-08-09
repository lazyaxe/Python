"""
if, elif and else:
"""

"""
A if statement is a user-defined condition to trigger a case or manipulate the control flow of the program
If a specific condition is met then than the the If statement is triggered/True and the code snippet executes...

If not(False) the code snippet's execution is skipped.

elif(short for 'else if') statement is only exceuted when the if condition is false.
There can be multiple elif conditions.
Each elif statement can have its own condition(s).

else condition is exceuted only when the if and elif conditions above it are False.
An else condition can be thought as a safety net if all conditions fail above it.

SYNTAX:
if a_condition:
   #Only when the condition is true.
   /*Code here*/

elif another_condition:
   #Only executed when this condtion is True and if was False
.
.
.
else:
   #only when if and all elif conditions were False
"""

age = int(input("Enter your age: "))
if (age >=100):
   print("You are too old to sign up")
elif (age >=50):
   print("You are a senior citizen, do you need help for signing up ?")
   user_input=input("for YES type 'y' or for NO type 'n' :")
   if (user_input == 'y'):
       print("Okay sending help, please wait...")
   elif(user_input=='n'):
       print("Aight then...")
       print("You are now signed up!")
   else:
       print("not valid respose")
elif (age >= 18):
   print("You are now signed up !")
elif (age <0):
   print("You ain't even born yet, bruh")
else:
   print("You are not eligible for this program")#Execption handling