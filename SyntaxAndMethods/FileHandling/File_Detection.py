#make a file(.txt) in the same folder(recommended)
#use a relative file path or an absolute file path
print()
import os

file_path = "SyntaxAndMethods/SampleFile.txt"# using is a relative file path, because we are inside a folder which is inside an another folder or at another directory

if os.path.exists(file_path):
    print(f"The location '{file_path}' exits.")

else:
    print("File could not be located.")

#for absolute path
filepath="/home/vhvhs/python/SyntaxAndMethods/SampleFile.txt" #use / or \\ or //instead of \ because python has commands like \t for tab etc...which can cause execptions during file detection.
try:
   if not os.path.exists(filepath):
       raise FileNotFoundError("The file path does not exist!")
except FileNotFoundError as fileNotFound:
    print(fileNotFound)
else:
    print(f"File path={filepath} exists!")

#To check that we are accessing a file or a directory we use isfile() and isdir() functions.
file_path2 = "/home/vhvhs/python"
try:
    if os.path.exists(file_path2):
        print(f"Location {file_path2} exists!")#there's no way to check id this a file or a directory.

        if os.path.isfile(file_path2):#this return a boolean
            print("This is a file.")

        elif os.path.isdir(file_path2):
            print("This is a directory.")
        
        else:
            raise FileNotFoundError("There's no File/Directory here.")

except FileNotFoundError as fileNotFound:
    print(fileNotFound)

except PermissionError:
    print("Permission Denied!")

except Exception:
    print("Unknown Error Occured.")

finally:
    print("Execution completed.")