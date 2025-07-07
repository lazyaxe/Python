#WHILE LOOP 
    #While loops executes some code while some condition is true
name = input("Enter your name =")
while(name == "" or name==" "):
    name=input("Please enter your name =")
print(f"Hello, {name} !")
is_loop = True
while is_loop:
    food= input("Enter a food you like:(nullspace/empty string to exit loop): ")
    print(f"You like {food}")
    if not food=="":
        food= input("Enter a another food you like("" to exit loop):")
    else:
        is_loop=False
print("You exited the program.")

number = int(input("Enter a number between 1 to 10:"))
while not 1<number<10: #while number <(LESSER THAN) 1 or number >(GREATER THAN) 10:(iterate/excecute the loop) 
    print(f"{number} is invaild")
    print("Try again")
    number=int(input("Enter a number between 1 to 10:"))
print(f"This {number} is correct")

print("Enter a number a which is negative and divisble by 3")
number=int(input("Number = "))
while not number<0 and number%3==0:
    print(f"{number} is not divisble by 3 and negative, Try again")
    number = int(input("Number = "))
print(f"This {number}  number checks out")

#Unrelated While loop
i=0
while i<10:
    print(i)
    i+=1

#WHAT IS range() function?
#range(5)=generates list of [0, 1, 2, 3, 4]
#range(1,7)= generates a list of including numbers including 1 but not 7=> [1, 2, 3, 4, 5, 6]
#range(3, 31, 3)= generates a list of numbers including 3 but not 31 and skips by only printing  every 3rd element=> [3, 6, 9, 12, 24, 27, 30]
# 'in' is membership operator that checks if i is IN range of 0 to 4 is range is iterated successfully. If the 'in' returns False and loop is terminated.

#FOR LOOP IN PYTHON
for i in range(4):
    print(i)
    #loop to print items on the same line

for i in range(5):
    print(i, end=" ")#print i from 0 to 4(5 elements) and add a space(" ") at the end of each iteration
print()#for new line

for i in reversed(range(10)):
    print(i, end=" ")#print i from 4 to 0(5 elements) and add a white space char(" ") at the end of each iteration
print()#for new line char

for i in range(1,31,2):#in = membership operator that checks that iteration is in range from 1 to 31 or not and return a boolean i.e if i is in range then while True if not then while False
    if i==13:
        continue
    elif(i<=29):
        break
    else:
        print(i, end=" ")#print i from 1 to 30(31 elements) and count only the 2nd iteration and add a space(" ") at the end of each iteration.

print()#for new line char
  
x = int(input("please enter x not between 1 and 100:"))

for i in range(4):#for each iteration of i [0, 1, 2, 3, 4] iterate some code,4 times
    if(0<x<100):
        print(f"{x} is invaild(0<x<100), try again")
        x = int(input("please enter not x between 1 and 100:"))
    else:
        print(f"{x} is vaild.")
        break