"""
List comprehension:
    List comprehension is the shorter and simpler way to create a list
Syntax:- 
    list_name = [<element> for <counter> in range() if <condition>] 
    list_name = [<element> for <item> in <another_list> if <condition>] 
"""
doubles_list = [number*2 for number in range(1, 11)]#this will iterate till number== 1 to 11 and return number*2
print(doubles_list)

print("For lists")
fruits = ["apple", "banana", "cherry", "coconut"]
fruits=[fruit.capitalize() for fruit in fruits]
print(fruits)


fruit_chars=[fruit_name[0] for fruit_name in ["apple", "banana", "cherry", "coconut"]]#fruit_name[0]=first char in the fruit_name
print(fruit_chars)
print()

#With IF CONDITIONS
integers=[1, 0, 2, 4, 6, 7, 89, -2, -3, 41]
whole_numbers=[abs(integer) for integer in integers if integer >=0]
print(whole_numbers)
print()
even_numbers = [integer for integer in integers if integer%2==0 and integer>0]
print(even_numbers)
print()
odd_numbers = [integer for integer in integers if not integer%2==0 and integer>0]
print(odd_numbers)

grades = [89, 81, 59, 78]
print("Passing grades")
passing_grades= [grade for grade in grades if grade>60]
print(passing_grades)