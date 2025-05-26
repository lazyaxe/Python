#Reading files of ().txt , .json, .csv)

file_path="/home/vhvhs/outputOfWrittingFile.txt"
print()
try:
    with open(file_path, "r") as file:
        content_of_file = file.read()
        print(content_of_file)

except FileNotFoundError:
    print("File not found, Read Error")

except PermissionError:
    print("File Read Error, Permission denied.")
print()

import json
print("for json file")
file_path1="/home/vhvhs/OutputOfJsonFile.json"
print()
try:
    with open(file_path1, "r") as file:
        content_of_file = json.load(file)
        print(content_of_file["name"])
        print(content_of_file["age"])
        print(content_of_file["Profession"])

except FileNotFoundError:
    print("File not found, Read Error")

except PermissionError:
    print("File Read Error, Permission denied.")

except json.decoder.JSONDecodeError:
    print("Bruh Why the error !")
print()

import csv
print("for csv file")
file_path2="/home/vhvhs/OutputOfCSVFile.csv"
print()
try:
    with open(file_path1, "r") as file:
        content_of_file = csv.reader(file)
        for line in content_of_file:
            print(line)
            #or
        for line in content_of_file:
            print(line[0])
except FileNotFoundError:
    print("File not found, Read Error")

except PermissionError:
    print("File Read Error, Permission denied.")
print()

