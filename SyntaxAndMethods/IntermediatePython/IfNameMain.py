def importable_function():#you can also name it main():
    print("This is the only part we need to run inside another file")
    print("I only need this code, when i use this as a module ")
def add(x,y):
    return x+y#I also need this part of code
print("Name of program = ",__name__)#when i am running this program alone program its name is '__main__' 
               #i.e. it's the main program, if i import then run it it will be the file's name(i.e. IfNameMain.py)
if __name__=='__main__':
    print("BLABLABLA!, THIS PART OF CODE IS NOT NEEDED FOR MODULES")
    print("So this if condtion is true ONLY when its the main program, not when its run by a module")
    importable_function()
    print(add(1, 2))