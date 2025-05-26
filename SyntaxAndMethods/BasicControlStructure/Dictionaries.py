#Dictionary is a collection of {key:value} pair ordered and mutable values, but no duplicates
countries_and_capitals= {
                         "India":"New Delhi",
                         "USA":"Washington D.C.",
                         "Japan":"Tokyo",
                         "China":"Beijing"
                         }
#print(dir(countries_and_capitals)) ,to know all the methods
#print(help(countries_and_capitals)) ,

print(countries_and_capitals.get("India"))#get() will find the matching key in dictionary and return the value of the key

print(countries_and_capitals.get("Pakistan"))#because not in dictionary, it will return "None" value.

#to check a key in a dictionary
#This will function like a boolean with if-else
if countries_and_capitals.get("China"):
    print("Captial of China exists in the dictionary")
elif countries_and_capitals.get("China")==None:
     print("Captial of China does not exists in the dictionary")
else:
     print("This is an exeception.")
#FOR APPENDING A NEW ENTRY IN DICTIONARY
countries_and_capitals["Pakistan"] = "Karachi"#append(add) a new key-value

#FOR UPDATING A ENTRY IN DICTIONARY
countries_and_capitals["China"]= "New Beijing"#Update a value of key

print(countries_and_capitals)

#FOR DELETEING A SELECTED ENTRY
print("TO DELETING A KEY:VALUE in Dictionary")
countries_and_capitals.pop("China")#deletes key "China" and "value"

#FOR DELETING THE LATEST ENTRY IN DICTIONARY
print("To delete a latest appending")
countries_and_capitals.popitem()#deletes the latest appended key-value i.e. Pakistan
print(countries_and_capitals)

keys = countries_and_capitals.keys()
print(keys)# prints the keys of the dictionary i.e. prints countries only
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

#user input dictionary
my_dictionary={}
iteration = int(input("How many keys the dictionary"))
for i in range(iteration):
    key = input("Input key of the dictionary")
    value = input(f"Input value for {key}")
    my_dictionary[key]=value
    print("k:v added = ", i+1)
print(my_dictionary)
for k,v in my_dictionary.items():
    print(f"{k}:{v}")