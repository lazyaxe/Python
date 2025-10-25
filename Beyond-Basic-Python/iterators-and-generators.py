#ITERATORS & GENERATORS IN PYTHON

'''
1. What is an Iterable in Python?
~> An object in Python is iterable if it can be iterated by a loop.
~> Precisely, an object which has a __iter__ method is an iterable.
~> We can check if an object's class has am '__iter__' method by using dir()
'''


from random import sample
from typing import Any


def is_iterable(object_name: object) -> bool:
    if '__iter__' in dir(object_name):
        return True
    else:
        return False

sample_1: list[int] = [1, 2, 3]
sample_2: set[int] = {1, 2, 3}
sample_3: tuple = (1, 2, 3)
sample_4: int = 4

print("Is a list iterable? : ", is_iterable(object_name = sample_1))

print("Is a set iterable? : ", is_iterable(object_name = sample_2))

print("Is a tuple iterable? : ", is_iterable(object_name = sample_3))

print("Is an integer iterable? : ", is_iterable(object_name = sample_4))

'''
2. What is an iterator in Python?
~> An object in Python that iterates over an iterable is an iterator.
~> Precisely, an object which has a __next__ method is an iterator.
~> The __iter__ method is used to create an iterator containing iterable object.
~> After an iterator obeject is created, the __next__ method can be used to iterate over an iterable i.e. traverse/access the next elements of the iterable...
~> Once all the elements of iterable are accesed, an execption of StopIteration is raised to stop the iteration.
~> An iterator has an __iter__ method, so every iterator is an iterable but not vice-versa...
~> By __iter__ method the iterator returns itself.
'''

#A function to determine if an object is an iterator or not....
def is_iterator(object_name: object) -> bool:
    if '__iter__' in dir(object_name) and '__next__' in dir(object_name):
        return True
    else:
        return False

iterator = iter(sample_1) #or sample1.__iter__()

print("is it an iterator?: ", is_iterator(object_name = iterator))

while True:
    try:
        item = next(iterator)
        print(item, end = " ")

    except StopIteration as SI:
        #A print statement just for the sake of understanding
        SI = "\nAll elements are iterated over."
        print(SI)
        break

#Making an iterator class w/ custom next method
class Range:
    def __init__(self, end: int, start: int = 0 ) -> None:
        self.value = start
        self.end = end

    def __next__(self):
        if self.value == self.end:
            raise StopIteration
        current_value = self.value
        self.value += 1
        return current_value

    def __iter__(self):
        return self

for i in Range(start = 12, end = 15):
    print(i)

'''
3. What is a generator in Python?
~> Generator is a special type of iterator in Python.
~> It's a Pythonic way to create an iterator without modifying __next__ and __iter__ methods...(it automatically creates the these methods under the hood)
~> To achive this, a generator uses 'yield' keyword.

4. What is 'yield' keyword in Python?
~> When a regular function call ends in Python or in any programming language, the local variables inside the functions are "freed" i.e. wiped out.
~> Now let's imagine a way:
    1. to return local variable, i but don't destroy it.
    2. Keep all local variables frozen in time,
    3. The next time that function is called again resume right where the i was left.
    That's what the yield keyword does!
~> It "freezes/stores" only the last iterated value and continues execution where it was left off...
~> Yield means to produce or to provide in English.

5. Why use generators?
~> Saves memory: it doesn't store all items like a list; it produces them one by one.
~> Constant memory usage: A value is dropped as soon as it's work is over
~> Lazy evaluation: values are computed only when needed.
~> Infinite sequences possible (like reading a file line by line).
~> If a the iterable is very large and we need to do some iteration, we will need to process the whole iterable just to see the first item

example: 

def count_up_to(limit):
    current = 0
    list = []
    while current < limit:
        list.append(current)
        current += 1
    return list

obj = count_up_to(limit = 45)

#Iterating over 
for i in obj:
    print(i)

Now imagine if the list was large dataset or a txt file, we'll have to wait for every item to 
NOTE:
~> The return keyword is not used because the generated object is not yet processed yet, instead python creates a reference to a new chunk in heap memory and processing is done when the iterator is used...
'''

#Simulating a generator
class countUpTo:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

obj = countUpTo(45)

while True:
    try:
        next(obj)
    except StopIteration:
        break

for i in countUpTo(limit = 45):
    print(i)

def count_up_to(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

#returns a generator object's reference
gen_obj = count_up_to(limit = 45)

#Iterating over the generated object
for i in gen_obj:
    print(i)

print("Is generator is an iterator?: ", is_iterator(object_name = gen_obj))

#Reading a large size file:
def read_log(filepath_or_buffer):
    with open(file = filepath_or_buffer, mode = 'r') as log:
        for line in log:
            yield line

sample_filepath = "/path/to/your/file"
 
gen_obj2 = read_log(sample_filepath)

for i in gen_obj2:
    print(i)
 




