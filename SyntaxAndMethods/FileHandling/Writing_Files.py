#Writing files in python .txt, .json, .csv
#Pending .xlsx and .zip

#1. Text files:
txt_data = input("Enter: ")
txt_file_path = "/home/vhvhs/outputOfWrittingFile.txt"

    # open(), the first parameter will return as the file object 
    # the second parameter, 'w' is the writing mode for existing files, it also creates a new file if file does not exist.
with open(txt_file_path, 'w') as file:# with is statement used to wrap the code i.e. closes the file as soon as it's done reading
        file.write(txt_data)

with open(txt_file_path, 'x') as file:
    # open(), the first parameter will return as the file object 
    # the 'x' is EXCLUSIVE to only creating new files and writting them, it WILL raise an error if this file already exists.
        file.write(txt_data)
        print(f"text file {txt_file_path} is created now")

print("For appending/updating a file's data. ")
txt_data2=input("Something to append: ")

with open(txt_file_path, 'a') as file:# appened mode
    file.write("\n"+txt_data2+"\n")
    print(f"text file {txt_file_path} is appended/updated now")
#for lists 
print("For appending/updating a file's data.")
employee_list = ["Eugene", "Mayweather", "Sourbee"]

with open(txt_file_path, 'a') as file:
    for employee in employee_list:
        file.write(employee+"\n")
    print(f"text file {txt_file_path} is appended/updated now for the list")

#2. JSON
import json
json_file_path="/home/vhvhs/OutputOfJsonFile.json"
json_data={}
iteration=int(input("How many data entries = "))

for i in range(iteration):#setting up a user-input dictionary named json_data.
    key = input(f"key {i} = ")
    value= input(f"value of {key} = ")
    json_data[key]=value
print("-"*20)

with open(json_file_path, 'w') as json_file:
    for k, v in json_data.items():
        json_file.write(f"{k}={v}\n")


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

    


