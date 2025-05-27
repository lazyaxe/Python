#1D Collections in Python

    #Lists = ["", ""] ordered and changeable(mutable), duplicates are allowed.
fruits=[]# Declaring and Initiallizing a empty list.
fruits = ["apple", "apples", "orange", "coconut"]
fruits[0] = "pineapple"# re-intializing the first item in list 
print(fruits)        #prints the full list

#Note: in python unintialized or empty lists cannot be initialized like arrays in C/C++, only append and insert method is used?
fruits.append("banana")#add an item in a end of a list
print(fruits)

fruits.remove("coconut")#ValueError if value not in the list.
print(fruits)

fruits.insert(0, "coconut")#add "coconut" as the 0th item of the list
print(fruits)

print(fruits[0])   #acessing the first element and printing it
print(fruits)
print(fruits[:4])  #alternatively
print(fruits[::-1])#reverse print list
print(fruits[::2]) #print list and skip 2nd element 
print()
print("lists by FOR LOOPS")
for fruit in fruits: #here fruit=i and fruits=the list elements, i(fruits) holds the value of list's one item for each iteration goes to next item till end of the list.
    print(fruit, end=", ")
print()
#print(dir(fruits))
print(len(fruits))#the number of items in the list
           
fruits.sort()#sorts alphabetically
print(fruits) 

print("lists sorted alphabetically")
fruits.sort()#sorts alphabetically
print("reverse alphabetically sorted:", end="")
fruits.reverse()#sorts reverse by the order they were put
print(fruits)

print("apple" in fruits)#checks if "apple" is INSIDE a list by searching a list and returns a boolean(True or False)
print(fruits.index("coconut"))#finds the indexing of coconut from 0 to 
print(fruits.count("apple"))

fruits.clear()
print("List is cleared now, empty (List contains 0 items)")
print(fruits)

#How to store and print a user inputed list
list_nums = []#initializing a empty list
size=int(input("Enter your list size = "))
for i in range(size):
    list_nums.append(int(input()))#attaching every new 'int' in the end of the list by. This does not works on sets and tuples because they are immutable(unchangeable).
    print("*", end=" ")
print()
for i in range(size):
    print(list_nums[i], end=" ")

user_list=[]
i=0
is_loop=True
while is_loop:
    user_list.append(input(f"Postion {i+1} element = "))
    if user_list[i]=="":
        is_loop=False#For terminating the while loop 
    i+=1
#print 
for x in user_list:
    print(x, end=" ")

#using insert() method
user_list=[]
i=0
is_loop=True
while is_loop:
    user_list.insert(i ,input(f"Postion {i+1} element = "))
    if user_list[i]=="":
        user_list.remove(user_list[i])
        is_loop=False
    i+=1

#print 
for x in user_list:
    print(x, end=" ")


#Set = {"",""} unordered and unchangable(immutuable) and any duplicate element(s) is removed.
fruits = {"apple", "pineapple", "orange", "coconut"}
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

fruits.clear()
print(fruits)
print()

#Tuple = ('', '') oredered unchangeable(immutable), duplicates allowed and faster than lists
print("TUPLES")
fruits=('apple', 'tomato', 'cherry', 'banana', 'watermelon', 'watermelon')
#print(dir(fruits))
#print(help(fruits)) for additional help
print("pineapple" in fruits)#checks if pineapple is in tuple of fruits, returns boolean
print(len(fruits))
print(fruits.count("watermelon"))# also available for the list

print("FOR LOOP FOR TUPLES ↓")
for fruit in fruits:
    print(f"{fruit}", end=" ")#To print horizontally
#fruits.clear() does not work in Tuples