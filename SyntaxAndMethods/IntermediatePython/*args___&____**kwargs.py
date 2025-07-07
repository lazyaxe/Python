'''
 *args
    ~> *arguement_name = allows to pass as many as positional/non-keyword arguements
    ~> '*'  this is the unpacking operator 
    ~> They store arguments and their values as tuples

'''
def add_numbers(*numbers):#coventionally *args 
    total = 0
    print("Type of *nums", type(numbers))
    for number in numbers:
        total += number
    return total

print(add_numbers(11, 2, 1, 6))#This can hold has AS MANY ARGUEMENTS as needed due to *args OF SAME DATA TYPES BECAUSE THEY ARE TUPLES
print()


#An example for strings
def display_name(*args):
    print(type(args))
    for arg in args:
        print(arg, end=" ")
display_name("Dr.", "Sung", "Jing", "Woo", "II")#position matters for non-keyword arguements
print()

'''
 **kwargs
    ~> **arguement_name = allows to pass as many keyword arguements to a function's call 
    ~> **kwargs is a dictionary collection
    ~> the kwargs= acts as a "key", and passed arguement acts as a "value" of key

    def function(**kwargs)
        #code
    
    function(some_kwarg_as_key = some_arguement_as_value)

'''
def prints_address(**keyword_args):
    print()
    print("Type of **kwargs = ", type(keyword_args), end="\n \n")
    for key,value in keyword_args.items():
        print(f"{key} = {value}")
        
prints_address( steet="123 Fake" 
               ,city="Real City"
               ,state="Estate"
               ,zip_code=54878)#This can hold as many arguments as needed due to *kwargs collection of different primitive data types

#Passing a dictionary as kwarg
dict_kwarg_example={
    "steet":"123 Fake" 
    ,"city":"Real City"
    ,"state":"Estate"
    ,"zip_code":54878
}
def prints_dict(**kwargs):
    print()
    for key, words in kwargs.items():#because kw is passed as an argument for kwargs
        print("Key:",key, "=", "Value:", words)
        
prints_dict(a_dictionary=dict_kwarg_example
            ,street="<Name_Of_A_Street>")
'''
    NOTE:
             1. 'dict_kwarg_example' will be passed as a value to key a named 'a_dictionary'.
              
             2. In the enclosed for loop of the function 'prints_dict' the print statement treat the    'a_dictionary' as a key and 'dict_kwarg_example' as a value.
             3. This makes 'kwargs' a "dictionary of dictionary"
'''