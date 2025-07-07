#Keyword Arguments == and argument preceded by an identifier
    #helps with readability 
    #order of arguments don't matter in Keyword Args("NON POSITIONAL")
    #A POSTIONAL ARGUMENT COMES FIRST THEN KEYWORD ARGUMENTS

def generate_greet(greeting, title, FirstName, LastName):
    print(f"{greeting}! {title} {LastName} {FirstName}")

#now USING KEYWORD ARGUEMENTS
#syntax:-  function_name(positonal_parameter, parameter1="string", parameter2=1234)
generate_greet("Namaskaram",FirstName="Ainz",title="Sorccer King",LastName="Gown Ool" )
