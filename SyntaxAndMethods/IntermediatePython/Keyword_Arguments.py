"""
Keyword Arguments:
    Keyword Arguments are the arguements preceded by an identifier.
    Keyword Arguments helps with readability.
    Order of arguments don't matter in Keyword Args("NON POSITIONAL")
    A positional arguement comes first before keyword arguments.
    SYNTAX:
        def <function_name>(positonal_parameter1, keyword_parameter1, keyword_parameter2):
            #code

        <function_name>(positonal_parameter1, keyword_parameter2="string", keyword_parameter2=1234)
"""
def generate_greet(greeting, title, FirstName, LastName):
    print(f"{greeting}! {title} {LastName} {FirstName}")

#now using keyword arguements:
generate_greet("Namaskaram",FirstName="Ainz",title="Sorccer King",LastName="Gown Ool" )
