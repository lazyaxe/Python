# *args = allows to pass non-keyword arguements
# '*'  this is unpacking operator 
#they store arguments and their values as tuples
def add_numbers(*nums):#coventionally *args 
    total = 0
    for num in nums:
        total += num
    return total
print(add_numbers(11, 2, 1, 6))#This can hold has AS MANY ARGUEMENTS as needed due to *args OF SAME DATA TYPES BECAUSE THEY ARE TUPLES
print()
def display_name(*args):
    print(type(args))
    for arg in args:
        print(arg, end=" ")
display_name("Dr.", "Sung", "Jing", "Woo", "II")#position matters for non-keyword arguements
print()

# **kwargs = allows to pass keyword arguements
# **kwargs is a dictionary collection
def prints_address(**keyword_args):
    print(type(keyword_args))
    for key,value in keyword_args.items():
        print(f"{key} = {value}")
        
prints_address( steet="123 Fake" 
               ,city="Real City"
               ,state="Estate"
               ,zip_code=54878)#This can hold as many arguments as needed due to *kwargs collection of different primitive data types

