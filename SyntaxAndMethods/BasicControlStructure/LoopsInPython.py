"""
Loops:
    Loops are a block of code which is executed a number of times till a certain condition is met i.e. iterate(repeat) as long as a condition is True.

There are mainly 2 types of loops:
1.Entry-controlled:
    An entry controlled loop is a loop where the iteration of a is controlled by the increment operation at start.
    The iteration is done till the condition is true.

    loop(condition, increment the counter)
    {
        #Iteration
    } 

2. Exit-controlled:
    An exit-contolled loop is a loop where the iteration the is controlled by the increment operation at below
    loop(True)
    {
        #iteration
        if not_condition:
            break
        increment the counter
    }

There are mainly 2 loops in python:
1. For loop(entry-controlled)
2. While loop(entry controlled)
"""

"""
WHILE LOOP: 

    SYNTAX:

    counter=0
    while(condition):
        #code
        counter+=1
"""

i=0
while i<10:
    print(i)
    i+=1

name = input("Enter your name =")
while(name == "" or name==" "):
    name=input("Please enter your name =")
print(f"Hello, {name} !")

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

"""
FOR LOOP:

    SYNTAX:

    for i in range(number):
        #code

    A for loop generally uses a range() function for the counter updation/incrementation.

    1. What is range() function?:
        The range() is an iterable(a varible which can be iterated/looped) form 0 to n-1.

    The range function can have three arguments: range(start, stop, step)
        The range can have theree types
        i). If only one argument is given: range(stop)
            range(31), 0 to (31-1)
        ii). If two args are given:
            range(5, 31), 5 to (31-1).
        iii). for three args: range(start, stop, step)
            step: range(5, 31, 2), 5 to (31-1) but skipping 2 numbers (7, 10, 13, ...)
    For example:
        range(5)=generates list of [0, 1, 2, 3, 4]

        range(1,7)= generates a list of including numbers including 1 but not 7=> [1, 2, 3, 4, 5, 6]

        range(3, 31, 3)= generates a list of numbers including 3 but not 31 and skips by only printing  every 3rd element=> [3, 6, 9, 12, 24, 27, 30]

    2. 'in' is membership operator that checks if the 'i' is IN range of 0 to 'number' or not. If True, loop is iterated successfully. 
    If the 'in' returns False and loop is terminated.
"""
for i in range(4):
    print(i)
print()#for new line

for i in range(5):
    print(i, end=" ")#print i from 0 to 4(5 elements) and append a space(" ") at the end of each iteration
print()

for i in reversed(range(10)):
    print(i, end=" ")
print()

"""
continue and break:
    continue and break are keywords used modify the flow of a loop 

    1. continue:
            Acts as a 'skip' statement.
    
    2. break:
            Used to terminate a loop when a specific condition has met.
"""
for i in range(1,31,2):
    if i==13:
        continue
    elif(i<=29):
        break
    else:
        print(i, end=" ")

print()
  
x = int(input("please enter x not between 1 and 100:"))

for i in range(4):#for each iteration of i [0, 1, 2, 3, 4] iterate some code,4 times
    if(0<x<100):
        print(f"{x} is invaild(0<x<100), try again")
        x = int(input("please enter not x between 1 and 100:"))
    else:
        print(f"{x} is vaild.")
        break

# for more info on for vs while loop. visit: https://www.geeksforgeeks.org/dsa/difference-between-for-loop-and-while-loop-in-programming/

"""
Do-while loop implementation:
"""
i=0
while(True):
    print(i)
    i+=1
    if(i>5):
        break