 # if elif(else if) and else statments
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