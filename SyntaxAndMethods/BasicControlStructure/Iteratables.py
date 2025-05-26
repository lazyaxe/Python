#AN OBJECT/COLLECTION THAT *CAN* BE ITERATED IS CALLED AN ITERATABLE 
#LISTS is ITERATABLE(forwards, backwards, any pattern)
#TUPLES is ITERATABLE(forwards, backwards, any pattern)
#SETS are ITERATABLE(forward only), because they are unordered
#chars, int, float are ITERATABLE

#An object is "iterable" if it can be gone through element by element.


#DICTIONARIES :
my_dictionary = {"A": 1, 
                 "B": 2, 
                 "C": 3}

for i in my_dictionary:#this will only give keys not it's value 
    print(i)
print()

    #for VALUES
for i in my_dictionary.values():#this will only give VALUE NOT it's KEY 
    print(i)
print()

    #for KEYS AND VALUES
for i, j in my_dictionary.items():#this will give KEYS AS WELL AS VALUE
    print(i, j)
print()

for i, j in my_dictionary.items():
    print(f"{i}:{j}")
print()