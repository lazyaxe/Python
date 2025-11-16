# WRITING FILES IN Python:.txt, .json, .csv
# Next: .xlsx and .zip

"""
~> Files in Python can be usually accessed by:
1. Using manual: file_object = open(file, mode) method
2. Using Pythonic Context Managers i.e. automate file opening and closing.

There are 5 write modes in Python
1. 'w' : write-only
2. 'w+' : write and read, creates a new file if not found
3. 'wb' : write binary only
4. 'wb+' : write and read binary, creates a new file if not found
5. 'x' : write exclusivly new files only, DOES NOT creates a new file if not found
6. 'a' : append only, creates a new file if not found
7. 'a+' : append and write, creates a new file if not found
8. 'ab' : append binary only, creates a new file if not found
9. 'ab+' : append and read binary, creates a new file if not found

~> Every write mode creates a new file if it does not exist, except for 'x'.

"""

#1. Text files:
txt_data = input("Enter: ")
txt_file_path = "/home/vhvhs/outputOfWrittingFile.txt"

# open(), the first parameter will return as the file object 
# The second parameter, 'w' is the writing mode for existing files, it also creates a new file if file does not exist.
with open(file = txt_file_path, mode = 'w') as file:
        file.write(txt_data)

# The 'x' is EXCLUSIVE to only creating new files and writting them, it WILL raise an error if this file already exists.
with open(file = txt_file_path, mode = 'x') as file:
        file.write(txt_data)
        print(f"text file {txt_file_path} is created now")

print("For appending/updating a file's data. ")
txt_data2=input("Something to append: ")

with open(txt_file_path, 'a') as file:# appened mode
    file.write("\n"+txt_data2+"\n")
    print(f"text file {txt_file_path} is appended/updated now")

#For writting lists 
print("For appending/updating a file's data.")
employee_list = ["Eugene", "Mayweather", "Sourbee"]

with open(txt_file_path, 'a') as file:
    for employee in employee_list:
        file.write(employee + "\n")
    print(f"text file {txt_file_path} is appended/updated now for the list")

#2. JSON
import json

json_file_path = "/home/vhvhs/OutputOfJsonFile.json"
json_data_as_dict = {}
iteration = int(input("How many data entries = "))

for i in range(iteration):
    key = input(f"key {i} = ")
    value = input(f"value of {key} = ")
    json_data_as_dict[key] = value
print("-" * 20)

with open(json_file_path, 'w') as json_file:
    for k, v in json_data_as_dict.items():
        json_file.write(f"{k} = {v}\n")


#3. CSV = comma separated values, they are used for data like Microsoft excel or Google Sheets
import csv
print("For .csv files")

employee_data = [["Name", "Age", "Profession"],
                 ["Harsh", "18", "Unemployed"],
                 ["Mango", "0", "Fruit"]] 

csv_file_path = "/home/vhvhs/OutputOfCSVFile.csv"

with open(csv_file_path, 'w') as file:
        writer = csv.writer(file)

        for employee_data_row in employee_data:
            writer.writerow(employee_data_row)
        print(f"CSV file {csv_file_path} is created now")

    


