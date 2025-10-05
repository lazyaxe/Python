"""
Dictionary Comprehensions:
    Dictionary comprehensions are a shorter way to create dictionary.
    It is very similar to list comprehensions.

A Dictionary Comprehension requires two lists.
One for key and other for value and a zip() 

SYNTAX:
 dict = = {<key>: <value> for <key>, <value> in zip(<key>, <value>) if <condition> }
"""
#Similar to List Comprehension

keys_or_names = ["Patrick", "Pro", "Itachi", "Aura"]
values_or_grades=["A", "S", "A+", "F"]

dictionary_or_dataset = {key: value for key, value in zip(keys_or_names, values_or_grades) if value and key.isalpha()}
"""
What is zip?:
    The zip object yields n-length tuples, where n is the number of iterables
    passed as positional arguments to zip(). 

    The i-th element in every tuple comes from the i-th iterable argument to zip(). 
    
    This continues until the shortest argument is exhausted.
"""
print(dictionary_or_dataset)