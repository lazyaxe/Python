#IF NAME == "MAIN" CONDITION
"""
~> The if __name__ == "__main__" is needed when we need to use a program as a module/library for another program.
~> This condition helps us to encapsulate 
"""
def add(x, y):
    return x + y

def program_name():
    #If running this program alone, the program its name is '__main__' i.e. it's the main program, if i import then run it it will be the file's name(i.e. IfNameMain.py)

    print("The program's name : ", __name__)

#Defining a main function in Python:
#Create a Function Called main() to Contain the Code You Want to Run
def main():
    program_name()
    print("I only need this code, when i use this as as the main program")
    print(add(1, 2))
"""
    This is executed if condition is only true when its the main program, not when it used as a module.
"""
if __name__=='__main__':
    main()

    #OR don't use the main function.
    program_name()
    print("I only need this code, when i use this as as the main program")
    print(add(1, 2))

#OR modify the main function such that it only executes in if __name__ == '__main__'

"""
def main():
    if __name__ == "__main__":
        program_name()
        print("I only need this code, when i use this as as the main program")
        print(add(1, 2))
    else:
        pass

main()
"""