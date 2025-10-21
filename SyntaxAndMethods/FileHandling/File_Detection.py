"""
FILE DETECTION IN Python:
~> File detection is used to detect the existence of files/directory.
~> A path to the file is needed for the check.
~> A method os.path.exists() is needed to check.
~> Both libraries and directories can be checked.
~> Both a relative file path (filename) or an absolute file path (/path/to/location) can be used.
"""
import os

# Using is a relative file path, because we are inside a folder which is inside an another folder or at another directory
file_path1 = "SyntaxAndMethods/SampleFile.txt"

if os.path.exists(file_path1):
    print(f"The location '{file_path1}' exits.")

else:
    print("File could not be located.")

#2. Absolute Path

# NOTE:
# ~> Use / or \\ or //instead of \ because python has commands like \t for tab etc...which can cause execptions during file detection.

file_path2="/home/vhvhs/python/SyntaxAndMethods/SampleFile.txt" 

try:
   if not os.path.exists(file_path2):
       raise FileNotFoundError
   
except FileNotFoundError as FNF:
    FNF = f"{file_path2} does not exist!"
    print(FNF)

else:
    print(f"File path={file_path2} exists!")

#3. Check if it's a file or a directory(dir) by isfile() and isdir():
dir_path = "/home/vhvhs/python"

try:
    if os.path.exists(dir_path):
        print(f"Location {dir_path} exists!")

    #Now to check if this a file of directory
        if os.path.isfile(dir_path):
            print("This is a file.")

        elif os.path.isdir(dir_path):
            print("This is a directory.")
        
        else:
            raise FileNotFoundError("There's no File/Directory here.")

except FileNotFoundError as FNF:
    print(FNF)

except PermissionError:
    print("Permission Denied!")

except Exception:
    print("Unknown Error Occured.")

finally:
    print("Execution completed.")