# COLLECTIONS IN PYTHON:
"""
~> Collections in Python are the data structure to store more than one variable.
~> Collections in Python can be heterogenous as they only store the reference of an object not the object.
"""

# 1D Collections in Python:
"""
1. Lists = ["", "", ...] ordered and changeable(mutable), duplicates are allowed and heterogenous for datatypes. 

2. Tuples = ("", "", ...) ordered but unchangble(im-mutable), duplicates allowed and heterogenous for datatypes.

3. Sets = {"", "", ...} unordered, immutable, duplicates not allowed and heterogenous for datatypes
""" 

# 1. Lists

#Initiallizing a empty list named 'fruits'.
fruits = []

#Inserting values:
fruits = ["apple", "apples", "orange", "coconut", 1, True]

# re-intializing the first item in list 
fruits[0] = "pineapple"

#printing the full list
print(fruits)

#NOTE:
#In python unintialized or empty lists cannot be initialized like arrays in C/C++, only append and insert method is used.
# NOT POSSIBLE: fruits[6] = "kiwi"

#add an item in a end of a list
fruits.append("banana")
print(fruits)

#ValueError if value not in the list.
fruits.remove("coconut")
print(fruits)

#add "coconut" as the 0th item of the list
fruits.insert(0, "coconut")
print(fruits)

#SLICING A LIST:

#acessing the first element and printing it
print(fruits[0])
print(fruits)

#alternatively
print(fruits[ : 4])

#reverse print list
print(fruits[ : : -1])

#print list and skip 2nd element 
print(fruits[ : : 2])

print()

print("Printing list by for loop")
""" 
Here fruit = i and fruits = the list elements, i(fruits) holds the value of list's one item for each iteration goes to next item till end of the list.
"""

#for each loop
for fruit in fruits:
    print(fruit, end = ", ")
print()

#To know every method of list: print(dir(fruits))

print(len(fruits))#the number of items in the list

#To sort the list
#NOTE: The list needs to be homogenous in terms of datatypes i.e. every item in the list needs to be of the same data type
print("Sorted list", fruits.sort())

#To sort reverse by the order they were put
fruits.reverse()
print(fruits)

#To check if "apple" is INSIDE a list by searching a list and returns a boolean(True or False)
print("apple" in fruits)

#finds the indexing of coconut from 0 to 
print(fruits.index("coconut"))

#To count number of instances "apple" in the fruits list.
print(fruits.count("apple"))

fruits.clear()
print("List is cleared now, empty (List contains 0 items)")

print(fruits)

#MAKING A USER INPUT LIST BY FOR LOOP:
#~> Attaching every new item in the end of the list by. This does not work on sets and tuples because they are immutable(unchangeable).

#Initializing a empty list
list_nums = []
size = int(input("Enter your list size = "))
for i in range(size):
    list_nums.append(int(input()))
    print("*", end = " ")

print()

#MAKING A USER INPUT LIST BY WHILE LOOP:
user_list = []
i = 0
size = int(input("Enter your list size(While loop 1) = "))

while True:
    user_list.append(input(f"Postion {i+1} element = "))
    if i == size - 1:
        #terminating the while loop 
        break
    i += 1


user_list = []
i = 0
while True:
    user_list.append(input(f"Input element at postion {i+1} element (press enter to exit) = "))
    if user_list[i] == "" or user_list[i] == " ":
        user_list.remove(user_list[i])#removing the appended element.
        break#For terminating the while loop 
    i += 1

#PRINTING THE LIST BY A FOR EACH LOOP: 
for x in user_list:
    print(x, end = " ")

#using insert() method
user_list = []
i = 0
is_loop = True
while is_loop:
    user_list.insert(i ,input(f"Postion {i+1} element = "))
    if user_list[i] == "":
        user_list.remove(user_list[i])#removing the inserted element.
        is_loop = False
    i += 1

#print 
for x in user_list:
    print(x, end = " ")

#2. Tuple = ('', '') ordered, unchangeable(immutable), duplicates allowed and faster than lists

print("TUPLES")
fruits = ('apple', 'tomato', 'cherry', 'banana', 'watermelon', 'watermelon', 17, True)

#print(dir(fruits))
#print(help(fruits)) for additional help

print("pineapple" in fruits)#checks if pineapple is in tuple of fruits, returns boolean

print(len(fruits))

print(fruits.count("watermelon"))# also available for the list

print("FOR LOOP FOR PRINTING TUPLES ↓")
for fruit in fruits:
    print(f"{fruit}", end = " ")#To print horizontally
#fruits.clear() does not work in Tuples

#3. Set = {"",""} unordered and unchangable(immutuable) and any duplicate element(s) is removed.

fruits = {"apple", "pineapple", "orange", "coconut", 78, True}

#print(dir(fruits))

print(len(fruits))

print("cherry" in fruits)#checks if "cherry" is in the set, returns boolean
#print(fruits[0]) won't work on sets because they are unordered i.e. sets do not have an index

fruits.add("cherry")
print(fruits)

fruits.remove("orange")
print(fruits)
    
fruits.pop()#removes the a element, but it could be any element i.e. because they are unordered
print(fruits)

fruits.clear()#removes all the elements.
print(fruits)
print()