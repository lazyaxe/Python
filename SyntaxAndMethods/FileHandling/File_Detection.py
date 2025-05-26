#make a file(.txt) in the same folder(recommended)
#use a relative file path or an absolute file path
print()
import os

file_path = "SyntaxAndMethods/SampleFile.txt"# using is a relative file path, because we are inside a folder which is inside an another folder or at another directory

if os.path.exists(file_path):
    print(f"The location '{file_path}' exits.")

else:
    print("File could not be located.")
print()
#for absolute path

    #use / or \\ or //instead of \ because python has commands like /t for tab etc...which can cause execptions during file detection.
file_path = "//home//vhvhs//Documents//psst_i_foresee_mad_kitten.txt"

if os.path.exists(file_path):
    print(f"Location {file_path} exists!")
else:
    print("Location could not be traced...")
print()

#To check that we are accessing a file or a directory we use isfile() and isdir() functions.
file_path = "/home/vhvhs/AI-ML_Goodies"

if os.path.exists(file_path):
    print(f"Location {file_path} exists!")#no way to check id this a file or a directory, i think
    
    if os.path.isfile(file_path):#this return a boolean
        print("This is a file bro.")
    
    elif os.path.isdir(file_path):
        print("This is a directory.")

    else:
        print("That's not a file or a directory bro.")

else:
    print("Location could not be traced...")
print()