import IfNameMain #importing IfNameMain.py from SYNTAXANDMETHOD folders
print("Sum of Addition: ", IfNameMain.add(1,2))
print()
print("Now i can run functions from this file without executing the main body", IfNameMain.needed_code())
#the code inside __name__=='main' if condition is not executed because it is imported as a module