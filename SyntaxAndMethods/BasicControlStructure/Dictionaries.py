
"""
Dictionary:
    A dictionary is a mutable data strucure in Python
    It stores data in ordered key-value pairs.
    A key cannot be dupicate.

SYNTAX:
    sample: dict={
                    key1: value1,
                    key2: value2,
                    key3: value3
                        .
                        .
                        .
                    keyN: valueN
                 }
"""
#Creating a dictionary(dict)
countries_and_capitals= {
                         "India":"New Delhi",
                         "USA":"Washington D.C.",
                         "Japan":"Tokyo",
                         "China":"Beijing"
                         }

#print(dir(countries_and_capitals)) ,to know all the methods
#print(help(countries_and_capitals)) ,

#get()
print(countries_and_capitals.get("India"))
#get() will find the matching key in countries_and_capitals and return the value of the key.

print(countries_and_capitals.get("Pakistan"))#because 'Pakistan' is not a key in countries_and_capitals, it will return "None" value.

#This can function like a boolean with if-else statement
if countries_and_capitals.get("China"):
    print("Captial of China exists in the dictionary")
elif countries_and_capitals.get("China")==None:
     print("Captial of China does not exists in the dictionary")
else:
     print("This is an exeception.")

#FOR APPENDING A NEW ENTRY IN DICTIONARY
countries_and_capitals["Pakistan"] = "Karachi"

#FOR UPDATING A ENTRY IN DICTIONARY
countries_and_capitals["China"]= "New Beijing"#Update a value of key
print(countries_and_capitals)

#FOR DELETEING A SELECTED ENTRY
print("TO DELETING A KEY:VALUE in Dictionary")
countries_and_capitals.pop("China")#deletes key "China" and value "Beijing"

#FOR DELETING THE LATEST ENTRY IN DICTIONARY
print("To delete a latest appending")
countries_and_capitals.popitem()
#deletes the latest appended key-value i.e. Pakistan-Karachi
print(countries_and_capitals)

keys = countries_and_capitals.keys()
print(keys)
# prints the keys of the countries_and_capitals i.e. prints countries only
print()

print("Printing each key by loops")
for key in countries_and_capitals.keys():
     print(key)
print()

values=countries_and_capitals.values()
print(values)
print()

print("Printing each value by loops")
for value in countries_and_capitals.values():
     print(value)
print()

#printing items i.e. printing {key} and (value)
for key,value in countries_and_capitals.items():#here the key,value is different than value,key
     print(f"{key}'s capital is {value}")#also here

"""
Updating multiple values of a dictionary:

~>update() method of dictionary datatype is used when one or multiple items in a dictionary need to be updated.

~>It can also be used to make new items in a dictionary.
"""
dict1={
    'A':'Apple',
    'B':'Cinnamon',
    'C':'Car',
    'D':'Donkey'
}
dict1.update(B= 'Banana')

#Updating an item
print("\n")
for key, value in dict1.items():
    print(f"{key}={value}")

#Both updating and adding an item.
dict1.update(C="Carrot", D="Diary")
print(dict1)

#Concatinating another dict:
dict2={
    'D':'Dinosaur',
    'E':'Elephant',
    'F':'Fudge',
    'G':'Guitar'
}

dict1.update(dict2)
"""
Here the dict1's 'D' key-value pair would be overwriiten by dict2 and other non-matching key will be appended to dict1.
"""
print(dict1)


#user input dictionary
my_dictionary={}
iteration = int(input("How many enteries to the dictionary? ="))
for i in range(iteration):
    key = input(f"Input key {i+1} = ")
    value = input(f"Input value for {key} =")
    my_dictionary[key]=value
    print(f"Entry {i+1}")
print(my_dictionary)

for k,v in my_dictionary.items():
    print(f"{k}:{v}")

dict_sample={}
iteration = int(input("How many enteries to the dictionary? ="))
i=0
while i<iteration:
    key = input(f"Input key {i+1} = ")
    value = input(f"Input value for {key} =")
    my_dictionary[key]=value
    #or my_dictionary.update(key=value)
    i+=1
i=0
print(dict_sample)

dict_sample={}
is_loop=True
counter=0
while is_loop:
    key=input(f"Enter the Key {counter+1}[whitespace/enter to exit]=")
    if key=="" or key==" ":
        is_loop=False
    else:
        dict_sample[key]=input(f"Value of {key}= ")
        counter+=1
print(dict_sample)